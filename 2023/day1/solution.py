def get_calibration_sum(filename: str) -> int:
    calibration_sum = 0
    with open(filename, 'r+') as file:
        lines = ["".join(filter(str.isdigit, line)) for line in file]
        for line in lines:
            calibration_sum += int(line[0] + line[-1])
    return calibration_sum


if __name__ == "__main__":
    print('Example value: {}'.format(get_calibration_sum('example.txt')))
    print('Part 1 value: {}'.format(get_calibration_sum('input.txt')))