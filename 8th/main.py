

def Part1(grid):
    amount_of_visible = ((len(grid) - 1) * 2) + ((len(grid[0]) - 1) * 2)

    for i, row in enumerate(grid[1:-1]):
        for y, col in enumerate(row[1:-1]):
            ups = list(map(lambda cell: grid[cell+1][y+1], range(-1, i)))
            downs = list(map(lambda cell: grid[cell+1][y+1], range(i+1, len(grid) - 1)))
            lefts = list(map(lambda cell: grid[i+1][cell+1], range(-1, y)))
            rights = list(map(lambda cell: grid[i+1][cell+1], range(y+1, len(row) - 1)))

            if all(col > cell for cell in ups):
                amount_of_visible += 1
                continue

            if all(col > cell for cell in downs):
                amount_of_visible += 1
                continue
            
            if all(col > cell for cell in lefts):
                amount_of_visible += 1
                continue
            
            if all(col > cell for cell in rights):
                amount_of_visible += 1
                continue

    print(amount_of_visible)

def Part2(grid):
    scores = []

    for i, row in enumerate(grid[1:-1]):
        for y, col in enumerate(row[1:-1]):
            ups = list(map(lambda cell: grid[cell+1][y+1], range(-1, i)))
            downs = list(map(lambda cell: grid[cell+1][y+1], range(i+1, len(grid) - 1)))
            lefts = list(map(lambda cell: grid[i+1][cell+1], range(-1, y)))
            rights = list(map(lambda cell: grid[i+1][cell+1], range(y+1, len(row) - 1)))
            
            ups.reverse()
            lefts.reverse()

            l = count_trees(lefts, col)
            r = count_trees(rights, col)
            u = count_trees(ups, col)
            d = count_trees(downs, col)

            scores.append(u * l * d * r)

    print(max(scores))


def count_trees(arr, col):
    amount = 0
    for item in arr:
        if item >= col:
            amount += 1
            return amount
        else:
            amount += 1
    return amount


if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read().splitlines()
        Part1(input)
        Part2(input)