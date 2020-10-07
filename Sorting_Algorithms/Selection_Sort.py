# The selection sort algorithm sorts an array by repeatedly finding the minimum element
# (considering ascending order)
# from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
#
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
#
# In every iteration of selection sort,
# the minimum element (considering ascending order)
# from the unsorted subarray is picked and
# moved to the sorted subarray.


# <<<<<<<<< EXAMPLE >>>>>>>>>>>
# Following example explains the above steps:
# arr = 64 25 12 22 11

# Find the minimum element in arr[0...4]
# and place it at beginning
# 11 25 12 22 64

# Find the minimum element in arr[1...4]
# and place it at beginning of arr[1...4]
# 11 12 25 22 64

# Find the minimum element in arr[2...4]
# and place it at beginning of arr[2...4]
# 11 12 22 25 64

# Find the minimum element in arr[3...4]
# and place it at beginning of arr[3...4]
# 11 12 22 25 64

# COMPLEXITY : Best O(n^2); Average O(n^2); Worst O(n^2)


def process(container_: any):
    """
    Used for performing bubble sort on a list of items

    :param container_: List of items
    :return: sorted array
    """

    for index_1 in range(len(container_)):
        min_index = index_1
        for index_2 in range(min_index+1, len(container_)):

            if container_[index_2] < container_[index_1]:
                min_index = index_2

        container_[min_index], container_[index_1] = container_[index_1], container_[min_index]

    return container_


if __name__ == '__main__':
    my_list = [3, 5, 7, 9, 1, 2, 4, 6, 8]
    print(process(container_=my_list))
