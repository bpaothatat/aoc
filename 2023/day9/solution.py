import re

class Sensor:
    def __init__(self, input: list) -> None:
        self.next_values = self.get_next_values(input)
        self.prior_values = self.get_prior_values(input)

    def get_next_values(self, input: list) -> list:
        result = []
        current = input
        while not all(i == current[0] for i in current):
            result.append(current)
            next = []
            for i in range(len(current) - 1):
                next.append(current[i + 1] - current[i])
            current = next
        result.append(current)
        return result
    
    def get_next(self) -> int:
        for i, row in reversed(list(enumerate(self.next_values))):
            if i < len(self.next_values):
                self.next_values[i - 1].append(self.next_values[i - 1][-1] + row[-1])
        return self.next_values[0][len(self.next_values[0]) - 1]
    
    def get_prior_values(self, input: list) -> list:
        result = []
        current = input
        while not all(i == 0 for i in current):
            result.append(current)
            next = []
            for i in range(len(current) - 1, 0, -1):
                next.insert(0, current[i] - current[i - 1])
            current = next
        result.append(current)
        return result
    
    def get_prior(self) -> int:
        for i, row in reversed(list(enumerate(self.prior_values))):
            if i == len(self.prior_values) - 1:
                self.prior_values[i].insert(0, 0)
            else:
                self.prior_values[i].insert(0, row[0] - self.prior_values[i + 1][0])
        return self.prior_values[0][0]

    def __str__(self) -> str:
        return str(self.prior_values)


def get_solution(filename: str) -> int:
    with open(filename, 'r+') as file:
        sensors = [Sensor([int(num) for num in re.findall(r'-?\d+',line)]) for line in file]
        return sum([sensor.get_next() for sensor in sensors]), sum([sensor.get_prior() for sensor in sensors])

if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_solution('example.txt')[0]))
    print('Part 1 value: {}'.format(get_solution('input.txt')[0]))
    print('Example value part 2: {}'.format(get_solution('example.txt')[1]))
    print('Part 2 value: {}'.format(get_solution('input.txt')[1]))
  

