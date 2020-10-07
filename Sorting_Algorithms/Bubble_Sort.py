# Bubble Sort is the simplest sorting algorithm that works by repeatedly
# swapping the adjacent elements if they are in wrong order.
# Example:
# First Pass:
# ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
# ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5),
# algorithm does not swap them.
#
# Second Pass:
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
# Now, the array is already sorted, but our algorithm does not know if it is completed.
# The algorithm needs one whole pass without any swap to know it is sorted.
#
# Third Pass:
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

# COMPLEXITY : Best O(n^2); Average O(n^2); Worst O(n^2)


def process(container_: any):
    """
    Used for performing bubble sort on a list of items
    :param container_: List of items
    :return: sorted array
    """

    while True:
        total_swaps = 0
        for idx in range(0, len(container_)-1, 1):
            if container_[idx] > container_[idx+1]:
                container_[idx + 1], container_[idx] = container_[idx], container_[idx + 1]
                total_swaps += 1
        if total_swaps == 0:
            break
    return container_


if __name__ == '__main__':
    my_list = [3, 5, 7, 9, 1, 2, 4, 6, 8]
    print(process(container_=my_list))
