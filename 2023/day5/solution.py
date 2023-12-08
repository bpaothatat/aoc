import re

class Range:
    def __init__(self, destination_start: int, source_start: int, length: int) -> None:
        self.destination_start = destination_start
        self.source_start = source_start
        self.length = length

    def __str__(self) -> str:
        return str(self.destination_start) + str(self.source_start) + str(self.length)

    def in_range(self, number: int) -> bool:
        return number >= self.source_start and number < (self.source_start + self.length)
    
    def get_destination_value(self, number: int) -> int:
        return number - self.source_start + self.destination_start

def get_point_total(filename: str) -> int:
    point_total = 0
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file if line.strip()]
        seeds = [int(value) for value in re.findall(r'\d+', lines[0])]
        maps = {}
        current_map = ''
        for line in lines[1:]:
            if ':' in line:
                maps[line[:-5]] = []
                current_map = line[:-5]
            else:
                values = [int(value) for value in re.findall(r'\d+', line)]
                maps.get(current_map).append(Range(values[0], values[1], values[2]))

        locations = []
        for seed in seeds:
            for map in maps:
                for range in maps.get(map):
                    if range.in_range(seed):
                        seed = range.get_destination_value(seed)
                        break
            locations.append(seed)
    return min(locations)

if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_point_total('example.txt')))
    print('Example value part 1: {}'.format(get_point_total('input.txt')))