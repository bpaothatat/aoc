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


if __name__ == "__main__":
    print('Example value part 1: {}'.format(part_1('example.txt')))
    print('Example value part 1: {}'.format(part_1('input.txt')))
