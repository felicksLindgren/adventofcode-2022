def BothParts(lines):
    dict = {}
    path = []

    for line in lines:
        all_words = line.split()

        if line[0] == '$':
            if '..' in line:
                path = path[:-1]
            elif 'cd' in line:
                if path: 
                    path.append(path[-1] + '/' + all_words[2])
                else:
                    path.append(all_words[2])

                if all_words[2] not in dict:
                    dict[all_words[2]] = 0
                
        elif all_words[0] != 'dir':
            for dir in path:
                if dir in dict:
                    dict[dir] += int(all_words[0])
                else:
                    dict[dir] = int(all_words[0])

    sum_of_sizes = sum([item for item in dict.values() if item <= 100_000])
    min_size = min(s for s in dict.values() if s >= 30_000_000 - (70_000_000 - dict['/']))

    print(sum_of_sizes)
    print(min_size)

if __name__ == "__main__":
    with open('./input.txt') as f:
        input = f.read().splitlines()
        BothParts(input)