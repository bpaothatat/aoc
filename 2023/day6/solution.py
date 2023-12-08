import re

def get_number_of_ways_to_win(dist: int, time: int) -> int:
    min = None
    max = None
    for i in range(time + 1):
        if not min:
            speed = time - i
            if dist < speed * i:
                min = i
        if not max:
            speed = time - i
            if dist < speed * i:
                max = time - i
        if min and max:
            break
    return max - min + 1


def get_part_1(filename: str) -> int:
    result = 1
    with open(filename, 'r+') as file:
        time, dist = [re.findall(r'\d+', line.strip()) for line in file if line.strip()]
        for i in range(len(time)):
            result *= get_number_of_ways_to_win(int(dist[i]), int(time[i]))
    return result


def get_part_2(filename: str) -> int:
    with open(filename, 'r+') as file:
        time, dist = [re.findall(r'\d+', line.strip().replace(' ', '')) for line in file if line.strip()]
    return get_number_of_ways_to_win(int(dist[0]), int(time[0]))

if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_part_1('example.txt')))
    print('Example value part 1: {}'.format(get_part_1('input.txt')))
    print('Example value part 1: {}'.format(get_part_2('example.txt')))
    print('Example value part 1: {}'.format(get_part_2('input.txt')))