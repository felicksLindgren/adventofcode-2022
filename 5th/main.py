def Part1(rearrangements, crates):
    for rearrangement in rearrangements:
        words = rearrangement.split(' ')
        amount = int(words[1])
        fromValue = int(words[3])
        to = int(words[5])

        for i in range(amount):
            crateToMove = crates[fromValue - 1].pop()
            crates[to - 1].append(crateToMove)

    topLayer = []
    for crate in crates:
        topLayer.append(crate[-1])

    print(''.join(topLayer))

def Part2(rearrangements, crates):
    for rearrangement in rearrangements:
        words = rearrangement.split(' ')
        amount = int(words[1])
        fromValue = int(words[3])
        to = int(words[5])

        cratesToMove = crates[fromValue - 1][-amount:]
        crates[fromValue - 1] = crates[fromValue - 1][:-amount]
        crates[to - 1].extend(cratesToMove)

    topLayer = []
    for crate in crates:
        topLayer.append(crate[-1])

    print(''.join(topLayer))



if __name__ == "__main__":
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        crates = [
            ['Z','T','F','R','W','J','G'],
            ['G','W','M'],
            ['J','N','H','G'],
            ['J','R','C','N','W'],
            ['W','F','S','B','G','Q','V','M'],
            ['S','R','T','D','V','W','C'],
            ['H','B','N','C','D','Z','G','V'],
            ['S','J','N','M','G','C'],
            ['G','P','N','W','C','J','J','D','L']
        ]
        # Stupid referencing in python
        crates2 = [
            ['Z','T','F','R','W','J','G'],
            ['G','W','M'],
            ['J','N','H','G'],
            ['J','R','C','N','W'],
            ['W','F','S','B','G','Q','V','M'],
            ['S','R','T','D','V','W','C'],
            ['H','B','N','C','D','Z','G','V'],
            ['S','J','N','M','G','C'],
            ['G','P','N','W','C','J','J','D','L']
        ]
        Part1(lines, crates)
        Part2(lines, crates2)
        