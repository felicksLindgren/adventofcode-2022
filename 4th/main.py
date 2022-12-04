
def Part1(pairs): 
    total = 0

    for pair in pairs:
        arr = pair.split(',')
        first =  [int(numeric_string) for numeric_string in arr[0].split('-')]     
        second =  [int(numeric_string) for numeric_string in arr[1].split('-')]

        lengthOfFirst = int(first[1]) - int(first[0])
        lengthOfSecond = int(second[1]) - int(second[0])


        if lengthOfFirst == lengthOfSecond:
            if first[0] == second[0]:
                total += 1
        if lengthOfFirst > lengthOfSecond:
            if second[0] >= first[0] and second[1] <= first[1]:
                total += 1
        if lengthOfFirst < lengthOfSecond:
            if first[0] >= second[0] and first[1] <= second[1]:
                total += 1

    print(total)

def Part2(pairs):
    total = 0

    for pair in pairs:
        arr = pair.split(',')
        first =  [int(numeric_string) for numeric_string in arr[0].split('-')]     
        second =  [int(numeric_string) for numeric_string in arr[1].split('-')]

        firstNumbers = list(range(first[0], first[1] + 1))
        secondNumbers = list(range(second[0], second[1] + 1))

        matches = set(firstNumbers) & set(secondNumbers)

        if matches:
            total += 1

    print(total)

if __name__ == "__main__":
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        Part1(lines)
        Part2(lines)