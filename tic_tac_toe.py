import streamlit as st
import numpy as np

# Initialize game board
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current_player = 1

# Reset game
def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current_player = 1

# Check for a win
def check_win(board):
    for i in range(3):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != 0:
            return board[i, 0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != 0:
            return board[0, i]
    if np.all(np.diag(board) == board[0, 0]) and board[0, 0] != 0:
        return board[0, 0]
    if np.all(np.diag(np.fliplr(board)) == board[0, 2]) and board[0, 2] != 0:
        return board[0, 2]
    return 0

# Game logic
def play_move(row, col):
    if st.session_state.board[row, col] == 0:
        st.session_state.board[row, col] = st.session_state.current_player
        winner = check_win(st.session_state.board)
        if winner != 0:
            st.session_state.winner = winner
        else:
            st.session_state.current_player = 3 - st.session_state.current_player

# UI
st.title("Tic Tac Toe")
st.write("Player 1: X\nPlayer 2: O")

if st.button('Reset Game'):
    reset_game()

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        if st.session_state.board[i, j] == 1:
            label = 'X'
        elif st.session_state.board[i, j] == 2:
            label = 'O'
        else:
            label = ''
        cols[j].button(label, key=f"{i}{j}", on_click=play_move, args=(i, j))

if 'winner' in st.session_state and st.session_state.winner != 0:
    st.write(f"Player {st.session_state.winner} wins!")
elif np.all(st.session_state.board != 0):
    st.write("It's a draw!")
