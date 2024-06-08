# Game-Hub
Welcome to the Game Hub! This repository contains several simple Python games and a chatbot that you can run and play in the terminal. The games included are:
1.Tic-Tac-Toe
2.Quiz 1
3.Quiz 2
4.Guess the Number
5.Hangman
6.Chatbot
Games and Features
TIC TAC TOE
A classic 3x3 tic-tac-toe game where two players take turns marking "X" or "O" on the board. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
Class: TicTacToeGame
Methods:
__init__: Initializes the game board and sets the current player.
print_board: Prints the current state of the game board.
make_move: Allows the current player to make a move at the specified position.
check_winner: Checks if there is a winner.
play: Starts the game loop.
Quiz
Two sets of quizzes with questions and answers. The user answers the questions, and their score is calculated based on correct answers.

QUIZ
Methods:
__init__: Initializes the quiz with a set of questions.
play: Starts the quiz and processes user input.
Guess the Number
A number guessing game where the player has to guess a randomly chosen number between 1 and 100 within a limited number of attempts.

GUESS THE NUMBER
Methods:
__init__: Initializes the secret number and sets the number of guesses left.
play: Starts the game loop and processes user guesses.
Hangman
A word guessing game where the player tries to guess a secret word by suggesting letters within a limited number of guesses.

HANGMAN
Methods:
__init__: Initializes the game with a random secret word and sets the number of guesses left.
print_current_state: Prints the current state of the guessed word.
guess_letter: Processes a guessed letter.
play: Starts the game loop.


CHATBOT
A simple chatbot that responds to specific phrases entered by the user.

Function: chatbot
Behavior: Responds to user inputs with predefined responses.
