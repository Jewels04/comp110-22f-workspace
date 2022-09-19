"""EX03 - Structured Wordle."""

__author__ = "730598599"


# This defined function searches to see if a specific character is found in a specific string.
def contains_char(string_searched: str, search: str) -> bool:
    """Generates a bool value that determines if a character is found in a string."""
    # This assertion makes sure that the function will only search for one specific character.
    assert len(search) == 1
    counter: int = 0
    while counter < len(string_searched):
        # If a character is found in a string, the function will return True. If not, the counter will increase until the loop ends and it will return False.
        if search == string_searched[counter]:
            return True
        else:
            counter += 1
    return False


# This function will return a string of emojis based on whether the characters of the "guess" string are in the correct spot, incorrect spot, or not present compared to the "secret" string.
def emojified(guess: str, secret: str) -> str:
    """Generates the necessary emojis based on the user's guess."""
    # This assertion makes sure that the lengths of the "guess" and "secret" strings are the same.
    assert len(guess) == len(secret)
    # These next three variables correspond to codes for the necessary emojis.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count_two: int = 0
    emoji: str = ""
    # In this loop, while the conter equals the length of the "secret" string, the program will determine whether a green, yellow, or white square emoji is needed.
    while count_two < len(secret):
        if guess[count_two] == secret[count_two]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[count_two]) is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        count_two += 1
    # Once the loop is completed, the function will return the string of emojis it created.
    return emoji


# This defined function establishes that a string must be a certain length in order to be returned.
def input_guess(word_len: int) -> str:
    """Establishes the length of the word needing to be guessed."""
    user_word: str = input(f"Enter a {word_len} character word: ")
    while len(user_word) != word_len:
        user_word = input(f"That wasn't {word_len} chars! Try again: ")
    return user_word


# This defined function establishes what the secret word is, as well as pulls together the previous functions in order to make a full-fledged game.
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # These variables establish the word needing to be guessed, the turn number the player is on, and whether the player has won or not.
    secret_wordle: str = "codes"
    user_turns: int = 1
    win: bool = False
    # This while loop establishes that the player only has six turns to play while also ensuring that the game ends if they guess correctly.
    while user_turns <= 6 and win is False:
        # The code below tells the player what turn they are on.
        print(f"=== Turn {user_turns}/6 ===")
        # The two lines of code below call the "input_guess" and "emojified" functions in order to use them in the "main" function.
        num_guess: str = input_guess(len(secret_wordle))
        print(emojified(num_guess, secret_wordle))
        # If the guessed word matches the secret word, a message saying the player won is printed and the function is completed.
        if num_guess == secret_wordle:
            print(f"You won in {user_turns}/6 turns!")
            win = True
            # If the guessed word does not match the secret word, the turn number is increased and the loop is restarted.
        else:
            user_turns += 1
        # If the player has played six turns and still has not guessed correctly, a message saying they lost is printed and the function is completed.
        if user_turns > 6:
            print("X/6 - Sorry, try again tomorrow!")


# These last lines of code make it so that the "main" function can be played as a module, as well as making it so that it can be imported in other modules.
if __name__ == "__main__":
    main()