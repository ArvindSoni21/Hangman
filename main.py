from utils.game import Hangman

def main() -> None:
    """
    Entry point for the Hangman game.
    """
    game = Hangman()
    game.start_game()

if __name__ == "__main__":
    main()