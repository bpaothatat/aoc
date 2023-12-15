import math

def getDict(line: str) -> dict:
    split = line.replace('(', '').replace(')', '').split(' = ')
    key = split[0]
    result = {}
    internal_split = split[1].split(', ')
    internal_dict = {'L': internal_split[0], 'R': internal_split[1]}
    result = {key:internal_dict}
    return result  

def part_1(filename: str) -> int:
    result = 0
    dict = {}
    direction = ''
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file]
        direction = lines[0]
        for line in lines[2:]:
            dict.update(getDict(line))

    current = 'AAA'
    counter = 0
    index = 0
    while current != 'ZZZ':
        counter += 1
        current = dict[current][direction[index]]
        index = (index + 1) % len(direction)
    return counter

def get_starting(keys: list) -> list:
    return [key for key in keys if key[-1:] == 'A']

def part_2(filename: str) -> int:
    result = 0
    dict = {}
    direction = ''
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file]
        direction = lines[0]
        for line in lines[2:]:
            dict.update(getDict(line))

    index = 0
    steps = 0
    current = get_starting(dict)
    least_steps = [0] * len(current)
    while 0 in  least_steps:
        for i, item in enumerate(current):
            if item.endswith('Z') and least_steps[i] == 0:
                least_steps[i] = steps
        current = [dict[item][direction[index]] for item in current]
        index = (index + 1) % len(direction)
        steps += 1
    print(least_steps)
    return math.lcm(*least_steps)


if __name__ == "__main__":
    print('Example value part 1: {}'.format(part_1('example.txt')))
    print('Example value part 1: {}'.format(part_1('input.txt')))
    print('Example value part 2: {}'.format(part_2('example.txt')))
    print('Example value part 2: {}'.format(part_2('input.txt')))