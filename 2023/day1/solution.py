def get_calibration_sum_part_1(filename: str) -> int:
    calibration_sum = 0
    with open(filename, 'r+') as file:
        lines = ["".join(filter(str.isdigit, line)) for line in file]
        for line in lines:
            calibration_sum += int(line[0] + line[-1])
    return calibration_sum

def get_calibration_sum_part_2(filename: str) -> int:
    calibration_sum = 0
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(filename, 'r+') as file:
        for line in file:
            min_index = len(line) + 1
            min_value = '0'
            max_index = -1
            max_value = '0'
            for digit in digits:
                min = int(line.find(digit))
                if min > -1 and min < min_index:
                    min_index = min
                    min_value = get_value(digit)
                
                max = int(line.rfind(digit))
                if max > max_index:
                    max_index = max
                    max_value = get_value(digit)
            calibration_sum += int(min_value + max_value)
    return calibration_sum

def get_value(value: str) -> str:
    map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    result = value
    if str.isalpha(value):
        result = map.get(value)
    return result

if __name__ == "__main__":
    print('Example value: {}'.format(get_calibration_sum_part_1('example_1.txt')))
    print('Part 1 value: {}'.format(get_calibration_sum_part_1('input_1.txt')))
    print('Example value: {}'.format(get_calibration_sum_part_2('example_2.txt')))
    print('Part 2 value: {}'.format(get_calibration_sum_part_2('input_2.txt')))