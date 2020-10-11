
def process(container_, search_element_) -> int:
    """
    Search the container for the element.
    :param container_: The list of elements
    :param search_element_: The element to search
    :return: return position of the element.
    """

    position = 0
    iteration = 0
    while position < len(container_):
        if container_[position] == search_element_:
            return position
        iteration += 1
        position += 1
    return -1


if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = process(container_=List, search_element_=10)
    if pos != -1:
        print("NOT FOUND")
    else:
        print(List[pos])
