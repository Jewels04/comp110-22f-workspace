"""EX02 - One Shot Wordle."""

__author__ = "730598599"


#Below are most of my variable declarations.
secret_wordle: str = "python"
number: int = len(secret_wordle)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
counter: int = 0
emoji: str = ""

#This is where the user would input their guessed word, which will be established under the variable "guess."
guess: str = input(f"What is your {number}-letter guess? ")

#If the user enters an incorrect amount of letters, this line will prompt them to retry.
while len(guess) != number:
    guess = input(f"That was not {number} letters! Try again: ")

#This is where the program will begin to identify letter matches if the guess doesn't match the secret word.
if guess != secret_wordle:
    while counter < len(guess):
        #Below is a code that will establish whether a letter is in the correct area;
        if guess[counter] == secret_wordle[counter]:
            emoji += GREEN_BOX
            #if not, the else statement will begin the process of seeing whether a yellow or white box is needed.
        else:
            alt_count: int = 0
            locate: bool = False
            #While the alternate counter is less than the current index of the secret word, it will run through the indexes to see if a white or yellow square should be put down in the current emoji index.
            while alt_count < len(secret_wordle):
                if guess[counter] == secret_wordle[alt_count]:
                    locate = True
                alt_count += 1
                #If the boolean expression is True, meaning the character exists in the secret word, a yellow square is put down;
            if locate == True:
                emoji += YELLOW_BOX
                #if not, a white square is put down.
            else:
                emoji += WHITE_BOX
        counter += 1
        #After all that, the emoji string is is printed and the user is told that they guessed incorrectly.
    print(emoji)
    print("Not quite. Play again soon!")
    #if the user guessed correctly, then the correct amount of green square emojis are declared and printed, and the player is congratulated.
else:
    while counter < len(guess):
        emoji += GREEN_BOX
        counter += 1
    print(emoji)
    print("Woo! you got it!")
