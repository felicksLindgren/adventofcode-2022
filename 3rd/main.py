import string

def Part1(backpacks):
    sumOfPriorities = 0

    for backpack in backpacks:
        halfwaypoint = int(len(backpack) / 2)
        first = list(backpack[:halfwaypoint])
        second = list(backpack[halfwaypoint:])

        for character in first:
            if character in second:
                sumOfPriorities += string.ascii_letters.index(character) + 1
                break

    print(sumOfPriorities)

def Part2(backpacks):
    sumOfBadges = 0

    for group in (backpacks[pos:pos + 3] for pos in range(0, len(backpacks), 3)):
        badge = set(group[0]) & set(group[1]) & set(group[2])
        sumOfBadges += string.ascii_letters.index(list(badge)[0]) + 1

    print(sumOfBadges)

if __name__ == "__main__":
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        Part1(lines)
        Part2(lines)