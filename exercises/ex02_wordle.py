"""Creating the wordle game"""

__author__: str = "730655988"


def contains_char(search_word: str, character: str) -> bool:
    """looks within a word for a specific character"""
    assert len(character) == 1, f"len('{character}') is not 1"

    i = 0
    while i < len(search_word):
        if search_word[i] == character:
            return True
        i += 1
    return False


"""Colors for the emojified function"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Tells what char is correct between guess and secret word for each letter"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    feedback = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            feedback += GREEN_BOX
        elif contains_char(secret, guess[i]):
            feedback += YELLOW_BOX
        else:
            feedback += WHITE_BOX
        i += 1
    return feedback


def input_guess(expected_length: int) -> str:
    """makes sure that guesses are the correct length"""
    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    """initial varibles at the beginning of the games"""
    turns_left = 6
    won = False
    attempts = 0

    while turns_left > 0 and not won:
        """main game loop"""
        """runs until you run out of turns or win"""
        print(f"=== Turn {attempts + 1}/6 ===")

        guess = input_guess(len(secret))  # estabishes the length of the secret
        attempts += 1

        feedback = emojified(guess, secret)
        print(feedback)

        if guess == secret:
            won = True

        turns_left -= 1
    """ allows winning or losing messages and stops game play"""
    if won:
        print(f"You won in {attempts}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


"""snippit or soemthing (idk)"""
if __name__ == "__main__":
    main(secret="codes")
