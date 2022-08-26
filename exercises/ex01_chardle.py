"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730598599"

chardle_word: str = input("Enter a 5-character word: ")
if len(chardle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chardle_letter: str = input("Enter a single character: ")
if len(chardle_letter) != 1:
    print("Error: Character must be a single character")
    exit()
chardle_count: int = 0
print("Searching for " + chardle_letter + " in " + chardle_word)

if chardle_word[0] == chardle_letter:
    print(chardle_letter + " found at index 0")
    chardle_count: int = chardle_count + 1

if chardle_word[1] == chardle_letter:
    print(chardle_letter + " found at index 1")
    chardle_count: int = chardle_count + 1

if chardle_word[2] == chardle_letter:
    print(chardle_letter + " found at index 2")
    chardle_count: int = chardle_count + 1

if chardle_word[3] == chardle_letter:
    print(chardle_letter + " found at index 3")
    chardle_count: int = chardle_count + 1

if chardle_word[4] == chardle_letter:
    print(chardle_letter + " found at index 4")
    chardle_count: int = chardle_count + 1

if chardle_count == 0:
    print("No intances of " + chardle_letter + " found in " + chardle_word)

if chardle_count == 1:
    print("1 instance of " + chardle_letter + " found in " + chardle_word)

if chardle_count > 1:
    print(str(chardle_count) + " instances of " + chardle_letter + " found in " + chardle_word)
