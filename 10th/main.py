def Part1(commands):
    cycle = 0
    index = 0
    next_checkpoint = 20
    register = 1
    signal_strengths = []

    for command in commands:
        cycle += 1 if command == 'noop' else 2

        while (cycle > 0):
            index += 1
            cycle -= 1

            if index == next_checkpoint:
                signal_strengths.append(register * next_checkpoint)
                next_checkpoint += 40

        if 'addx' in command:
            register += int(command.split()[1])

    print(sum(signal_strengths))


def Part2(commands):
    cycle = 0
    index = 0
    next_checkpoint = 40
    row_in_grid = 0
    grid = [['.' for _ in range(40)] for _ in range(6)]
    sprite_position = 1

    for command in commands:
        cycle += 1 if command == 'noop' else 2

        while (cycle > 0):
            if index == sprite_position - 1:
                grid[row_in_grid][sprite_position - 1] = '#'
            elif index == sprite_position:
                grid[row_in_grid][sprite_position] = '#'
            elif index == sprite_position + 1:
                grid[row_in_grid][sprite_position + 1] = '#'

            index += 1
            cycle -= 1

            if index == next_checkpoint:
                row_in_grid += 1
                index = 0
        
        if 'addx' in command:
            sprite_position += int(command.split()[1])

    for row in grid:
        print(row)


if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read().splitlines()
        Part1(input)
        Part2(input)