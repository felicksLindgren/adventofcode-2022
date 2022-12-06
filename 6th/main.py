def solution(buffer, amount):
    for index, character in enumerate(buffer[1:]):
        next_amount_of_characters = buffer[index:index+amount]
        if len(set(next_amount_of_characters)) == amount:
            return index + amount

if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read()
        print(solution(input, 4))
        print(solution(input, 14))