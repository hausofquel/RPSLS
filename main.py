# As a developer, I want to make at least 10 commits with descriptive messages.
# As a developer, I want to find a way to properly incorporate inheritance to my game.
# AS a developer, I want to account ffor and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
# As a devloper, I want to store all the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (dislplay gesture options, assign player gesture, etc.)

# As a player, I want the corrext player to win a given round based on the chocues made by each player.
# As a player, I want the game of RPSLS tp be at a minumum a 'best of three' to decide a winner.
# As a player, I want the option of a single player (human vs Ai) or a multiplayer (human vs human) game.


from game import Game
if __name__ == '__main__':
    game = Game()
    game.run_game()
