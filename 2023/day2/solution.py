def is_valid_set(set: str) -> bool:
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    current_cubes = {'red': 0, 'green': 0, 'blue': 0}
    draws = set.split(',')
    for draw in draws:
        value, color = draw.strip().split(" ")
        value = int(value)
        value += current_cubes.get(color)
        current_cubes.update({color: value})
    return cubes.get('red') >= current_cubes.get('red') and cubes.get('green') >= current_cubes.get('green') and cubes.get('blue') >= current_cubes.get('blue')


def get_sum_of_ids(filename: str) -> int:
    id_sum = 0
    with open(filename, 'r+') as file:
        lines = [line for line in file]
        for line in lines:
            game, sets = line.split(':')
            id = int("".join(filter(str.isdigit, game)))
            sets = sets.split(";")
            valid = True
            for set in sets:
                if not is_valid_set(set):
                    valid = False
            if valid:
                id_sum += id
    return id_sum

def get_power(line: str) -> int:
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for set in line.split(';'):
        for draw in set.split(','):
            value, color = draw.strip().split(" ")
            value = int(value)
            if value > min_cubes.get(color):
                min_cubes.update({color: value})
    return min_cubes.get('red') * min_cubes.get('green') * min_cubes.get('blue')

def get_power_sum(filename: str) -> int:
    power_sum = 0
    with open(filename, 'r+') as file:
        lines = [line for line in file]
        for line in lines:
            power_sum += get_power(line.split(':')[1])
    return power_sum


if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_sum_of_ids('example.txt')))
    print('Part 1 value: {}'.format(get_sum_of_ids('input.txt')))
    print('Example value part 2: {}'.format(get_power_sum('example.txt')))
    print('Part 1 value: {}'.format(get_power_sum('input.txt')))