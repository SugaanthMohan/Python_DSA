

def process(container_):
    """
    Testing pythons default sorting operations
    :param container_: container of array (vector) of scalars
    :return: sorted container
    """

    return sorted(container_)


if __name__ == '__main__':
    my_list = [3, 5, 7, 9, 1, 2, 4, 6, 8]
    print(process(container_=my_list))
