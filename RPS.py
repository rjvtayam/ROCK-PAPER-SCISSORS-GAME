import random

def player(prev_play, opponent_history=[]):
    # If this is the first game, return a random move
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Append the opponent's last move to the history
    opponent_history.append(prev_play)

    # Analyze the opponent's move patterns
    if len(opponent_history) > 3:
        last_four_moves = "".join(opponent_history[-4:])
        possible_moves = ["RRRR", "PPPP", "SSSS", "RRPP", "PPSS", "SSRR", "RPRP", "PSPS", "SRSR"]

        for pattern in possible_moves:
            if pattern in last_four_moves:
                # If a pattern is detected, play the move that beats the next move in the pattern
                if pattern == "RRRR" or pattern == "PPPP" or pattern == "SSSS":
                    return "P" if pattern == "RRRR" else "S" if pattern == "PPPP" else "R"
                elif pattern == "RRPP" or pattern == "PPSS" or pattern == "SSRR":
                    return "P" if pattern == "RRPP" else "S" if pattern == "PPSS" else "R"
                elif pattern == "RPRP" or pattern == "PSPS" or pattern == "SRSR":
                    return "P" if pattern == "RPRP" else "S" if pattern == "PSPS" else "R"

    # If no pattern is detected, play the move that would beat the opponent's last move
    if prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    elif prev_play == "S":
        return "R"

    # If the opponent's last move is not recognized, return a random move
    return random.choice(["R", "P", "S"])
