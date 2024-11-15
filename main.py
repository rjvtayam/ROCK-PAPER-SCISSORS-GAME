from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Test the player function against different bots
print("Playing against quincy:")
play(player, quincy, 1000, verbose=True)

print("\nPlaying against mrugesh:")
play(player, mrugesh, 1000, verbose=True)

print("\nPlaying against kris:")
play(player, kris, 1000, verbose=True)

print("\nPlaying against abbey:")
play(player, abbey, 1000, verbose=True)

# Uncomment the line below to run unit tests
# from test_module import run_tests
# run_tests()
