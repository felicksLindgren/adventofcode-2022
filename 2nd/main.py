# Loss = 0, Draw = 3, Win = 6
# Rock = 1, Paper = 2, Scissor = 3

# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win

def Part1(rounds):
    totalScore = 0

    for round in rounds:
        opponent = round[0]
        player = round[2]

        if opponent == 'A':
            if player == 'X':
                totalScore += 4
            if player == 'Y':
                totalScore += 8
            if player == 'Z':
                totalScore += 3
        if opponent == 'B':
            if player == 'X':
                totalScore += 1
            if player == 'Y':
                totalScore += 5
            if player == 'Z':
                totalScore += 9
        if opponent == 'C':
            if player == 'X':
                totalScore += 7
            if player == 'Y':
                totalScore += 2
            if player == 'Z':
                totalScore += 6
    
    print(totalScore)


def Part2(rounds):
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
        Part1(lines)
        Part2(lines)