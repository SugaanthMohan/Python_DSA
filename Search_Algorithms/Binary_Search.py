# function binary_search(A, n, T) is
#     L := 0
#     R := n − 1
#     while L ≤ R do
#         m := floor((L + R) / 2)
#         if A[m] < T then
#             L := m + 1
#         else if A[m] > T then
#             R := m − 1
#         else:
#             return m
#     return unsuccessful
# In computer science, binary search, also known as half-interval search,
# [1] logarithmic search,
# [2] or binary chop,
# [3] is a search algorithm that finds the position of a target value within a sorted array.
# [4][5] Binary search compares the target value to the middle element of the array.
# If they are not equal, the half in which the
# target cannot lie is eliminated and the search continues on the remaining half,
# again taking the middle element to compare to the target value,
# and repeating this until the target value is found.
# If the search ends with the remaining half being empty,
# the target is not in the array.
# Binary search runs in logarithmic time in the worst case,
# making  O(log n) (log n) comparisons,
# where n is the number of elements in the array.
# [a][6] Binary search is faster than linear search except for small arrays.
# However, the array must be sorted first to be able to apply binary search.
# There are specialized data structures designed for fast searching, such as hash tables,
# that can be searched more efficiently than binary search. However,
# binary search can be used to solve a wider range of problems,
# such as finding the next-smallest or next-largest element in the array relative to the target
# even if it is absent from the array.


def process(container_, search_element_) -> int:
    """
    Search the container for the element.
    :param container_: The list of elements
    :param search_element_: The element to search
    :return: return position of the element.
    """
    container_ = sorted(container_)
    left = 0
    right = len(container_) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2

        if search_element_ == container_[mid]:
            return mid
        elif container_[mid] < search_element_:
            left = mid + 1
        else:
            right = mid - 1
        iterations += 1
    return -1


if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = process(container_=List, search_element_=10)
    if pos != -1:
        print("NOT FOUND")
    else:
        print(List[pos])

    # 