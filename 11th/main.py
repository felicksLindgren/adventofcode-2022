import re
import math

def BothParts(monkeys, r, worry_level_divider=1):
    mod = 1
    l = list()

    for monkey in monkeys:
        test = int(monkey[3][monkey[3].index('by') + 2:])
        mod *= test
        m = {
            'starting_items': re.findall(r'\b\d+\b', monkey[1]),
            'operation': monkey[2][monkey[2].index('=') + 6:].split()[0],
            'amount': monkey[2][monkey[2].index('=') + 6:].split()[1],
            'test': test,
            'test_true': re.findall(r'\b\d+\b', monkey[4])[0],
            'test_false': re.findall(r'\b\d+\b', monkey[5])[0],
            'inspected_items': 0,
        }
        l.append(m)
    
    for _ in range(r):
        for monkey in l:
            for item in monkey['starting_items']:
                amount = int(monkey['amount'] if monkey['amount'] != 'old' else item)
                i = int(item)
                worry_level = (i * amount) if monkey['operation'] == "*" else i + amount
                worry_level %= mod

                if worry_level_divider > 1:
                    worry_level = math.floor(worry_level / worry_level_divider)

                if worry_level % monkey['test'] == 0:
                    l[int(monkey['test_true'])]['starting_items'].append(worry_level)
                else:
                    l[int(monkey['test_false'])]['starting_items'].append(worry_level)
            
            monkey['inspected_items'] += len(monkey['starting_items'])
            monkey['starting_items'] = []

    inspected_items = [monkey['inspected_items'] for monkey in l]
    inspected_items.sort(reverse=True)
    print(math.prod(inspected_items[:2]))

    
            
if __name__ == "__main__":
    with open('./input.txt') as f:
        input = [monkey.split('\n') for monkey in f.read().split('\n\n')]
        BothParts(input, 20, 3)
        BothParts(input, 10_000)
