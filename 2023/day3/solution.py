import re

def is_part(row: int, column: int, lines: list) -> bool:
    if row > -1 and row < len(lines) and column > -1 and column < len(lines[0]):
        value = lines[row][column]
        return value != '.' and not value.isnumeric()
    return False

def is_next_to_part(row: int, column: int, lines: list) -> bool:
    return (is_part(row - 1, column, lines) or is_part(row + 1, column, lines) or is_part(row, column - 1, lines) 
            or is_part(row, column + 1, lines) or is_part(row - 1, column - 1, lines) or is_part(row - 1, column + 1, lines)
            or is_part(row + 1, column - 1, lines) or is_part(row + 1, column + 1, lines))
    

def is_part_number(number: str, current_index: int, row: int, lines: list) -> bool:
    result = False
    column = lines[row].index(number, current_index)
    for index in range(len(number)):
        if is_next_to_part(row, column + index, lines):
            result = True
            break
    return result


def get_sum_of_parts(filename: str) -> int:
    parts_sum = 0
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file]
        for row_index, line in enumerate(lines):
            numbers = re.findall(r'\d+', line)
            current_index = 0
            for number in numbers:
                if is_part_number(number, current_index, row_index, lines):
                    parts_sum += int(number)
                current_index = line.index(number) + len(number)
    return parts_sum

if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_sum_of_parts('example.txt')))
    print('Part 1 value: {}'.format(get_sum_of_parts('input.txt')))