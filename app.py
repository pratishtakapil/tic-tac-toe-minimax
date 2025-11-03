import streamlit as st
from game import Board, ai_move

st.set_page_config(page_title="Tic Tac Toe AI", page_icon="🎮", layout="centered")

# --- Initialize session state ---
if "board" not in st.session_state:
    st.session_state.board = Board()
    st.session_state.turn = "X"
    st.session_state.game_over = False
    st.session_state.human_symbol = None
    st.session_state.ai_symbol = None

board = st.session_state.board

# --- Title ---
st.title("🎮 Tic Tac Toe AI (Minimax)")

# --- Choose symbol ---
if st.session_state.human_symbol is None:
    st.write("### Choose your symbol:")
    col1, col2 = st.columns(2)
    if col1.button("❌ Play as X"):
        st.session_state.human_symbol = "X"
        st.session_state.ai_symbol = "O"
        st.rerun()
    if col2.button("⭕ Play as O"):
        st.session_state.human_symbol = "O"
        st.session_state.ai_symbol = "X"
        st.session_state.turn = "X"  # X always starts
        st.rerun()

else:
    human = st.session_state.human_symbol
    ai = st.session_state.ai_symbol
    st.write(f"You are **{human}**. AI is **{ai}**")

    # --- Display board ---
    cols = st.columns(3)
    for i in range(9):
        if board.cells[i] == " ":
            if st.session_state.turn == human and not st.session_state.game_over:
                if cols[i % 3].button(" ", key=i, use_container_width=True):
                    board.cells[i] = human
                    if board.winner() or board.is_full():
                        st.session_state.game_over = True
                    else:
                        st.session_state.turn = ai
                    st.rerun()
            else:
                cols[i % 3].button(" ", key=i, disabled=True, use_container_width=True)
        else:
            cols[i % 3].button(board.cells[i], key=i, disabled=True, use_container_width=True)

        if i % 3 == 2 and i < 8:
            cols = st.columns(3)

    # --- AI Move ---
    if st.session_state.turn == ai and not st.session_state.game_over:
        move = ai_move(board, ai, human)
        if move is not None:
            board.cells[move] = ai
        if board.winner() or board.is_full():
            st.session_state.game_over = True
        else:
            st.session_state.turn = human
        st.rerun()

    # --- Game Over ---
    if st.session_state.game_over:
        winner = board.winner()
        if winner == human:
            st.success("🎉 You win!")
        elif winner == ai:
            st.error("💻 AI wins!")
        else:
            st.info("🤝 It's a draw!")

        if st.button("🔁 Restart Game"):
            st.session_state.board = Board()
            st.session_state.turn = "X"
            st.session_state.game_over = False
            st.session_state.human_symbol = None
            st.session_state.ai_symbol = None
            st.rerun()
