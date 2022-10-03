"""Defeat the Beast!"""

__author__ = "730598599"

# The lines of code below 1) import the randint function to be used later. 2) Establishes the global variables that keep track of the player's name, the player's health, and the beast's health.
from random import randint
player: str = ""
points: int = 0
beast: int = 0


def greet() -> None:
    """Establishes the name of the player and gives them a greeting."""
    global player
    # This is where the player will input what they would like the game to call them.
    player = input("What would you like to be called? ")
    # Below is an introduction given to the player where the purpose and rules of the game are established.
    print(f"Hello {player}, welcome to the battle! It's up to you to defeat the beast! You will each take turns performing actions. \nWhile playing, you can choose to attack, heal, or retreat. If you choose attack, you will have the option to either perform a regular attack or a magic attack. But be careful, while magic attacks are more powerful, they can also backfire and hurt you instead! Good luck!")


def fight(player_input: str) -> int:
    """This function determines what happens if the player chooses to attack."""
    global player
    global points
    global beast
    # Below, the variables that represent the strings, emojis, and random number generator are established.
    mag_atk: str = "magic attack"
    reg_atk: str = "regular attack"
    MAGIC_ATTACK: str = "\U0001F52E"
    REGULAR_ATTACK: str = "\U00002694"
    FAILED_ATTACK: str = "\U0001F4A5"
    chance: int = randint(0, 9)
    # The game will ask whether the player wants to perform a "magic attack" or a "regular attack."
    action: str = input(f"{player}, you have chosen to {player_input}! \nWould you like to perform a regular attack or a magic attack? ")
    # If the player enters an invalid input, the game will prompt them to try again.
    while action != mag_atk and action != reg_atk:
        action = input("That was not a valid action, please try again. ")
    # If the player chooses a "magic attack," a random number will be generated to determine the outcome of it.
    if action == mag_atk:
        chance = randint(0, 9)
        # If "chance" is less than 5, the attack will have backfired and the player will lose 15 points.
        if chance < 5:
            points -= 15
            print(f"{FAILED_ATTACK} Oh no! Your magic attack backfired! Your health is now at {points}.")
            # If chance is greater than or equal to 5, the attack will have been successful and the beast will lose 20 points.
        else:
            beast -= 20
            print(f"{MAGIC_ATTACK} Nice shot {player}! The beast's health is now at {beast}!")
    # if the player chooses a "regular attack," the beast will lose 10 points.
    if action == reg_atk:
        beast -= 10
        print(f"{REGULAR_ATTACK} Nice hit {player}! The beast's health is now at {beast}!")
    return points, beast


def heal(health: int, gain: int) -> int:
    """This function establishes what happens of the player chooses to heal."""
    global player
    global points
    # Below, the variables that represent the emojis used later are established.
    REG_HEALTH: str = "\U00002728"
    STRONG_HEALTH: str = "\U0001F4AB"
    # If the gain value, which is randomly generated (0, 100) is greater than the players current health, than the player will receieve a larger amount of health.
    if gain > health:
        print(f"{STRONG_HEALTH} Wow! That heal was extra effective! You gained 20 health!")
        points += 20
        # If the gain value is less than the players current health, then they will recieve a regular amount of health.
    else:
        print(f"{REG_HEALTH} Nice heal {player}! You gained 15 health!")
        points += 15
    # This ensures that the player's health will never exceed 100.
    if points > 100:
        points = 100
    return points


def main() -> None:
    """This is the main game loop, where the different paths and outcomes of the game are established."""
    global points
    global beast
    # Below, the variables that represent the strings that will be used later and the initial amount of points are established.
    a: str = "attack"
    h: str = "heal"
    r: str = "retreat"
    points = 100
    beast = 100
    # The greet function is called to introduce the game.
    greeting: str = greet()
    # While either the player or beast have health, the game will continue to run.
    while points > 0 and beast > 0:
        # The game will ask the player what action they would like to take.
        action: str = input(f"{player}: {points} \nBeast: {beast} \nWould you like to attack, heal, or retreat? ")
        # If the player inputs an invalid action, the game will ask them to try again.
        while action != a and action != h and action != r:
            action = input("That was not a valid action, please try again. ")
        # If the player chooses to retreat, the game will print a message telling the player bye and the program will end.
        if action == r:
            print(f"You retreated from the beast. You'll get 'em next time!")
            return None
        # If the player chooses to attack, the fight function will be called.
        if action == a:
            points, beast = fight(action)
        # If the player chooses to heal, the heal function will be called.
        if action == h:
            points == heal(points, randint(0, 100))
        # If the beast still has health, it will go through a round of attack where it will either inflict damage on the player or miss.
        if beast > 0:
            # Whether the beast succeeds or not is determined by a random number generator.
            beast_attack: int = randint(0, 9)
            # If the number is less than 7, the beast will have inflicted damage.
            if beast_attack < 7:
                print("The beast attacked! You lost 20 health.")
                points -= 20
                # If the number is greater than or equal to 7, the beast will have missed.
            else:
                print("The beast missed!")
    # if the player's health hits 0 or a negative number, the game will let them know they have lost and the program will end.
    if points <= 0:
        print(f"Sorry {player}, looks like the beast has bested you. Better luck next time!")
    # If the beast's health hits 0 or a negative number, the game will let the player know they have won and the program will end.
    if beast <= 0:
        print(f"Congratulations {player}! You have defeated the beast! See you next time!")


# Establishes that the main function will be the function ran when the program starts.
if __name__ == "__main__":
    main()
