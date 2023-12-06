import re

def get_point_total(filename: str) -> int:
    point_total = 0
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file]
        for line in lines:
            matching_numbers = 0
            winning_numbers, numbers = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', winning_numbers)
            numbers = re.findall(r'\d+', numbers)
            for number in numbers:
                if number in winning_numbers:
                    matching_numbers += 1
            if matching_numbers > 0:
                point_total += 2 ** (matching_numbers - 1)
    return point_total

def get_total_scratchcards(filename: str) -> int:
    scratchcards_count = []
    lines = []
    with open(filename, 'r+') as file:
        lines = [line.strip() for line in file]
        scratchcards_count = [1] * len(lines)
        for index,line in enumerate(lines):
            matching_numbers = 0
            winning_numbers, numbers = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', winning_numbers)
            numbers = re.findall(r'\d+', numbers)
            for number in numbers:
                if number in winning_numbers:
                    matching_numbers += 1
            for i in range(matching_numbers):
                scratchcards_count[index + i + 1] = scratchcards_count[index + i + 1] + scratchcards_count[index] * 1
    return sum(scratchcards_count)

if __name__ == "__main__":
    print('Example value part 1: {}'.format(get_point_total('example.txt')))
    print('Part 1 value: {}'.format(get_point_total('input.txt')))
    print('Example value part 2: {}'.format(get_total_scratchcards('example.txt')))
    print('Part 1 value: {}'.format(get_total_scratchcards('input.txt')))