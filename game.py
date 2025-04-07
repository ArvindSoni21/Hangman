from typing import List
import random


class Hangman:
    """
    Hangman game class to manage game state and logic.
    """

    def __init__(self) -> None:
        """
        Initializes the Hangman game attributes.
        """
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = list(random.choice(self.possible_words))
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ['_' for _ in self.word_to_find]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self) -> None:
        """
        Handles a single round of the game by asking the user for a guess
        and updating the game state.
        """
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Please enter exactly one alphabetical character.")
                continue
            if guess in self.correctly_guessed_letters or guess in self.wrongly_guessed_letters:
                print("⚠️ You already guessed that letter. Try a new one.")
                continue
            break

        self.turn_count += 1

        if guess in self.word_to_find:
            print(f"✅ Good job! '{guess}' is in the word.")
            for i, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[i] = guess
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            self.wrongly_guessed_letters.append(guess)
            self.error_count += 1
            self.lives -= 1

    def start_game(self) -> None:
        """
        Starts and runs the game loop until win or loss condition is met.
        """
        print("\n🎮 Welcome to Object-Oriented Hangman!\n")

        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            print("\n" + " ".join(self.correctly_guessed_letters))
            print(f"Wrong guesses: {', '.join(self.wrongly_guessed_letters)}")
            print(f"Lives left: {self.lives}")
            self.play()

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self) -> None:
        """
        Ends the game and shows game over message.
        """
        print("\n💀 Game Over!")
        print(f"The word was: {''.join(self.word_to_find)}")

    def well_played(self) -> None:
        """
        Congratulates the player for winning.
        """
        print("\n🎉 You found the word: {} in {} turns with {} errors!".format(
            ''.join(self.word_to_find), self.turn_count, self.error_count))