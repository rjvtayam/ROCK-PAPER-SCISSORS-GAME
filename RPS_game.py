import random

def play(player1, player2, num_games, verbose=False):
    p1_wins = 0
    p2_wins = 0
    prev_play = ""

    for _ in range(num_games):
        p1_move = player1(prev_play)
        p2_move = player2(prev_play)

        if p1_move == p2_move:
            result = "Tie"
        elif (p1_move == "R" and p2_move == "S") or (p1_move == "P" and p2_move == "R") or (p1_move == "S" and p2_move == "P"):
            result = "Player 1 wins"
            p1_wins += 1
        else:
            result = "Player 2 wins"
            p2_wins += 1

        if verbose:
            print(f"Player 1: {p1_move}, Player 2: {p2_move} -> {result}")

        prev_play = p2_move

    print(f"Player 1 wins: {p1_wins}, Player 2 wins: {p2_wins}")

def quincy(prev_play):
    return "P"

def mrugesh(prev_play):
    return "R"

def kris(prev_play):
    return "S"

def abbey(prev_play):
    return random.choice(["R", "P", "S"])
