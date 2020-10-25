
def calculate_fibonacci(number):

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)


def generate_fibonacci_series(count):

    for pos in range(count):
        print(calculate_fibonacci(pos))


if __name__ == '__main__':
    generate_fibonacci_series(10)
