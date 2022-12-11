def BothParts(motions, length_of_rope):
    positions = set([(0,0)])
    R = [[0,0] for _ in range(length_of_rope + 1)]
    moves = { 'U': 1, 'D': -1, 'R': 1, 'L': -1 }

    for motion in motions:
        direction,amount = motion.split()
        amount = int(amount)

        for _ in range(amount):
            R[0][0] += moves[direction] if direction in 'LR' else 0
            R[0][1] += moves[direction] if direction in 'UD' else 0

            for i in range(length_of_rope):
                H = R[i]
                T = R[i+1]

                diff_x = H[0] - T[0]
                diff_y = H[1] - T[1]

                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    if diff_x == 0:
                        T[1] += 1 if diff_y > 0 else -1
                    elif diff_y == 0:
                        T[0] += 1 if diff_x > 0 else -1
                    else:
                        T[0] += 1 if diff_x > 0 else -1
                        T[1] += 1 if diff_y > 0 else -1

            positions.add(tuple(R[-1]))
            
    print(len(positions))

if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read().splitlines()
        BothParts(input, 1)
        BothParts(input, 9)