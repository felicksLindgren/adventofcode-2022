def solution(buffer, amount):
    for index, character in enumerate(buffer[1:]):
        nextFour = buffer[index:index+amount]
        if len(set(nextFour)) == amount:
            return index + amount

if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read()
        print(solution(input, 4))
        print(solution(input, 14))