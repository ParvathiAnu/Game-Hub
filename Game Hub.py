import random

class TicTacToeGame:
    def __init__(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("+-+-+-+")

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. That position is already taken.")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]  # Return the winning player symbol
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]  # Return the winning player symbol
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]  # Return the winning player symbol
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]  # Return the winning player symbol

        # If no winner is found
        return None

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            print(f"\n{self.current_player}'s turn:")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            self.make_move(row, col)
            self.print_board()
            winner = self.check_winner()
            if winner:
                print(f"Congratulations! {winner} wins!")
                return
            elif all(self.board[row][col] != " " for row in range(3) for col in range(3)):
                print("It's a tie!")
                return



class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        print("Welcome to the Quiz!")
        for question, answer in self.questions.items():
            print(question)
            user_answer = input("Your answer: ").lower()
            if user_answer == answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is {answer}.")
        print(f"You scored {self.score} out of {len(self.questions)}.")
        return self.score

class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 5

    def play(self):
        print("Welcome to Guess the Number!")
        print("I'm thinking of a number between 1 and 100.")
        while self.guesses_left > 0:
            print(f"\nGuesses left: {self.guesses_left}")
            guess = int(input("Enter your guess: "))
            if guess == self.secret_number:
                print("Congratulations! You guessed the number.")
                return
            elif guess < self.secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
            self.guesses_left -= 1
        print(f"Sorry, you ran out of guesses. The secret number was {self.secret_number}.")

class HangmanGame:
    def __init__(self):
        self.words = ["python", "java", "ruby", "javascript", "php"]
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = set()
        self.current_state = ["_"] * len(self.secret_word)

    def print_current_state(self):
        print(" ".join(self.current_state))

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return
        self.guessed_letters.add(letter)
        if letter in self.secret_word:
            print("Correct guess!")
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.current_state[i] = letter
        else:
            self.guesses_left -= 1
            print("Wrong guess!")
            print(f"Guesses left: {self.guesses_left}")

    def play(self):
        print("Welcome to Hangman!")
        while self.guesses_left > 0:
            print("\nSecret word:")
            self.print_current_state()
            if "_" not in self.current_state:
                print("Congratulations! You guessed the word.")
                return
            print(f"\nGuesses left: {self.guesses_left}")
            letter = input("Guess a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            self.guess_letter(letter)
        print(f"Sorry, you ran out of guesses. The secret word was '{self.secret_word}'.")

def chatbot():
    print("Welcome to Chatbot!")
    while True:
        user_input = input("You: ").lower()
        if "hello" in user_input:
            print("Bot: Hi there!")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but thanks for asking!")
        elif "exit" in user_input:
            print("Bot: Goodbye!")
            break
        elif "who created you" in user_input:
            print("Bot: I was created by OpenAI.")
        else:
            print("Bot: I'm not sure I understand. Can you rephrase or ask something else?")

def main():
    tic_tac_toe_game = TicTacToeGame()
    quiz1 = Quiz({
        "What is PEP 8?": "style guide for Python code",
        "What is the output of '2' + '3'?": "23",
        "What does the 'len()' function return when called on an empty list?": "0",
        "What is the result of 'Python'[1:4]?": "yth",
        "What is the main difference between tuples and lists in Python?": "mutability"
    })
    quiz2 = Quiz({
        "What is the capital of France?": "paris",
        "What is the largest planet in our solar system?": "jupiter",
        "What is the chemical symbol for water?": "h2o",
        "What is the capital of Japan?": "tokyo",
        "What is the fastest land animal?": "cheetah"
    })
    guess_the_number_game = GuessTheNumberGame()
    hangman_game = HangmanGame()

    print("Welcome to the Game Hub!")
    while True:
        print("\nChoose a game to play:")
        print("1. Tic-Tac-Toe")
        print("2. Quiz 1")
        print("3. Quiz 2")
        print("4. Guess the Number")
        print("5. Hangman")
        print("6. Chatbot")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tic_tac_toe_game.play()
        elif choice == "2":
            quiz1.play()
        elif choice == "3":
            quiz2.play()
        elif choice == "4":
            guess_the_number_game.play()
        elif choice == "5":
            hangman_game.play()
        elif choice == "6":
            chatbot()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

