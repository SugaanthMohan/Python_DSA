# IMPORTING NECESSARY PACKAGES
import itertools


class HArray:
    """
    Default Set of arrays containing the total
    """
    __slots__ = (
        'size',
        'items',
        'type',
    )

    def __init__(self, size_, default_value_=None, type_=int):
        self.size = size_
        self.items = list(itertools.repeat(default_value_, size_))
        self.type = type_

    def insert(self, index, value):
        self.items[index] = value

    def remove(self, value):
        self.items.remove(value)

    def __repr__(self):
        return ','.join(map(str,self.items))

    def __str__(self):
        return ','.join(map(str, self.items))

    def __len__(self):
        return self.size


if __name__ == '__main__':
    my_array = HArray(10)
    my_array.insert(0, 10)
    my_array.insert(1, 11)
    my_array.insert(2, 12)
    my_array.remove(12)
    print(my_array)
