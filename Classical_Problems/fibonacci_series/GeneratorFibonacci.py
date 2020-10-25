

def generator_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def get_fibonacci(count):

    for idx, scalar in enumerate(generator_fibonacci(), start=1):
        if idx > count:
            break
        else:
            print("\t#{idx} => {scalar}".format(idx=idx, scalar=scalar))


if __name__ == '__main__':
    get_fibonacci(count=10)
