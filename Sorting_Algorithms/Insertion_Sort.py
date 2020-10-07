# Insertion sort is a simple sorting algorithm that works
# similar to the way you sort playing cards in your hands.
# The array is virtually split into a sorted and an unsorted part.
# Values from the unsorted part are picked and
# placed at the correct position in the sorted part.

# Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

# i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
# 11, 12, 13, 5, 6

# i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
# 11, 12, 13, 5, 6

# i = 3. 5 will move to the beginning and all other elements from 11 to 13
# will move one position ahead of their current position.
# 5, 11, 12, 13, 6

# i = 4. 6 will move to position after 5, and elements from 11 to 13
# will move one position ahead of their current position.
# 5, 6, 11, 12, 13

def process(container_: any):
    """
    Used for performing Insertion sort on a list of items
    :param container_: List of items
    :return: sorted array
    """

    for index_1 in range(1, len(container_), 1):

        correct_index_pos = None

        for index_2 in range(0, index_1):
            if container_[index_2] > container_[index_1]:
                correct_index_pos = index_2
                break

        if correct_index_pos is not None:
            container_.insert(
                correct_index_pos,
                container_.pop(
                    index_1
                )
            )

    return container_


if __name__ == '__main__':
    my_list = [3, 5, 7, 9, 1, 2, 4, 6, 8]
    print(process(container_=my_list))
