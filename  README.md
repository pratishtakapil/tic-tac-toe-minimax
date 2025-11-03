# 🎮 Tic-Tac-Toe AI (Minimax Algorithm)

A simple Python project that lets you play **Tic-Tac-Toe against an AI** powered by the **Minimax adversarial search algorithm**.  
Built for beginners who want to understand how AI can make optimal moves in a simple game.

---

## 🧩 Features

- Play as **X or O** against an intelligent AI
- Uses **Minimax algorithm** for decision making
- Text-based, works right inside the **terminal**
- Lightweight and easy to understand (only 3 Python files)

---

## 🛠️ Requirements

- Python 3.8 or above  
  (No external libraries needed)

---

## 📁 Folder Structure

tic-tac-toe-minimax/
│
├── game.py # Game logic and board handling
├── ai.py # Minimax algorithm for AI
└── main.py # Game runner (CLI)
2️⃣ Run the Game
python main.py

3️⃣ Play!

Choose your symbol (X or O)

Enter a move number from 0–8 (positions are like this):

0 | 1 | 2
--+---+--
3 | 4 | 5
--+---+--
6 | 7 | 8

The AI will automatically calculate and make the best move.

🧮 How It Works

The Minimax algorithm simulates all possible moves and their outcomes:

Maximizing player (AI) tries to maximize its chances of winning.

Minimizing player (Human) tries to minimize the AI’s chances.

Each move is given a score:

+1 → AI wins

0 → Draw

-1 → Human wins

The AI picks the move with the best overall score after exploring all possibilities.

🏆 Example Gameplay
Choose your symbol (X or O): X

| |  
--+---+--
| |  
--+---+--
| |

Enter your move (0-8): 0
AI plays 4

X | |  
--+---+--
| O |  
--+---+--
| |

🧑‍💻 Author

Pratishta Kapil
📍 Saharanpur, India
