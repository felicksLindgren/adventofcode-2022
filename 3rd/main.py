import string

def Part1(backpacks):
    sumOfPriorities = 0

    for backpack in backpacks:
        halfwaypoint = int(len(backpack) / 2)
        first = list(backpack[:halfwaypoint])
        second = list(backpack[halfwaypoint:])

        match = set(first) & set(second)
        
        if match:
            sumOfPriorities += string.ascii_letters.index(list(match)[0]) + 1

    print(sumOfPriorities)

def Part2(backpacks):
    sumOfBadges = 0

    for group in (backpacks[pos:pos + 3] for pos in range(0, len(backpacks), 3)):
        first = group[0]
        second = group[1]
        third = group[2]

        badge = set(first) & set(second) & set(third)
        sumOfBadges += string.ascii_letters.index(list(badge)[0]) + 1

    print(sumOfBadges)

if __name__ == "__main__":
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        Part1(lines)
        Part2(lines)