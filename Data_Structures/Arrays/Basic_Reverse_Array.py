# SET YOUR DEFAULT ARRAY TYPE
from Data_Structures.Arrays.Array import HArray


def basic_reverse_array(array_):

    start = 0
    end = len(array_) - 1
    while start < end:

        array_[end], array_[start] = array_[start], array_[end]
        start += 1
        end -= 1


if __name__ == '__main__':
    array = HArray(20, 0)
    print("BEFORE REVERSE :", array)
    basic_reverse_array(array)
    print("AFTER REVERSE :", array)
