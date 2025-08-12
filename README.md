# Tic-Tac-Toe

A **command-line Tic-Tac-Toe game** built in **Python** using **Visual Studio Code**.  
Designed for **two players**, the game alternates turns between **X** and **O**.

## 🎮 How It Works
- 🟦 Played on a **3×3 grid** displayed in the terminal.  
- ⌨️ Players select a cell by entering its corresponding number.  
- 🏆 The first player to align **three identical marks**—vertically, horizontally, or diagonally—wins.  
- 🤝 If all cells are filled with no winner, the game results in a draw.

## ✨ Features
- 🖥️ Clean and intuitive command-line interface.  
- ⚡ Instant game state updates after each move.  
- ✅ Input validation to prevent invalid or duplicate moves.  
- 🔄 Option to replay the game after completion.  
- 🧪 Dedicated unit test script to ensure game logic reliability.

## 📂 Project Files

### `Main Game.py`
The **primary playable Tic-Tac-Toe program**.  
This script launches an interactive command-line game where two players alternate turns. It includes:
- A complete game loop to manage turn-taking between **X** and **O**.
- Input handling with validation for incorrect or already-occupied positions.
- Logic for detecting win conditions and tie outcomes.
- A replay function to reset the board and start a new match without restarting the program.

### `Main Game (Test).py`
A **unit testing script** that verifies the functionality of the game’s core logic using Python’s `unittest` framework.  
This file does not run a playable game; instead, it:
- Confirms move validation works as intended (`validateMove()`).
- Ensures correct placement of marks on the board (`markBoard()`).
- Tests all winning conditions for both players (`checkWin()`).
- Validates the detection of tie games (`checkFull()`).

The test script serves as a quality assurance layer, ensuring that the game logic in `Main Game.py` operates correctly before execution.

## 🛠️ Built With
- **Python** – core game logic and execution  
- **Visual Studio Code** – development and testing environment  
- **unittest** – automated testing of game functions
