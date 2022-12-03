# Loss = 0, Draw = 3, Win = 6
# Rock = 1, Paper = 2, Scissor = 3

# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win

def CalculateTournament(rounds):
    totalScore = 0

    for round in rounds:
        opponent = round[0]
        outcome = round[2]

        if outcome == 'X':
            if opponent == 'A':
                totalScore += 3
            if opponent == 'B':
                totalScore += 1
            if opponent == 'C':
                totalScore += 2
        if outcome == 'Y':
            if opponent == 'A':
                totalScore += 4
            if opponent == 'B':
                totalScore += 5
            if opponent == 'C':
                totalScore += 6
        if outcome == 'Z':
            if opponent == 'A':
                totalScore += 8
            if opponent == 'B':
                totalScore += 9
            if opponent == 'C':
                totalScore += 7

    print(totalScore)


if __name__ == "__main__":
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        CalculateTournament(lines)