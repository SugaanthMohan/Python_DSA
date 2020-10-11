# Licontainer_indexe Quiccontainer_indexSort, Merge Sort is a Divide and Conquer algorithm.
# It divides input array in two halves, calls itself for the two halves
# and then merges the two sorted halves.
# The merge() function is used for merging two halves.
# The merge(arr, l, m, r) is container_indexey process that
# assumes that arr[l..m] and arr[m+1..r] are sorted and
# merges the two sorted sub-arrays into one.
# See following C implementation for details.

# <<<<<<<<<<<< EXAMPLE >>>>>>>>>>>>
# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)


# <<<<<<<<<<<<<<< EXECUTION PATTERN >>>>>>>>>>>>>>>>
# [10, 100, 2, 69, 71]
# MERGESORT :
#
#   ITERATION 1:
#       mid = 2, left = [10, 100], right = [2, 69, 71]
#   ITERATION 2: ( left )
#       mid = 1 , left = [10], right = [100]
#   ITERATION 3: ( right )
#       mid = 1 , left = [2] , right = [69, 71]
#   ITERATION 4: (right, right) [left is already at 1]
#       mid = 1, left = [69], right = [71]

# MERGE:
#   1st Priority => Iteration 2 : left = [10] , right = [100], array = [10, 100, 2, 69, 71]
#       counter_left = 0, counter_right = 0, counter_array = 0
#       Repeat till counter_left < len(left array) and counter_right < len(right array) => 0 < 1 and 0 < 1
#           if left[counter_left] < right[counter_right]: => 10 < 100 True
#               array[counter_array] = left[counter_left] => array = [10, 100, 2, 69, 71]
#               increment counter_left by 1 => counter_left = 1
#               increment counter_array by 1 => counter_array = 1
#           else: False
#               array[counter_array] = right[counter_right]
#               increment counter_right by 1
#               increment counter_array by 1
#
#       Repeat till counter_left < len(left array) => 1 < 1 False
#           array[counter_array] = left_array[counter_left]
#           increment counter_array by 1
#           increment left_array by 1
#
#       Repeat till counter_right < len(right array) => 0 < 1 True
#           array[counter_array] = left_array[counter_left] => array = [10, 100, 2, 69, 71]
#           increment counter_array by 1    => counter_array = 2
#           increment left_array by 1       => left_array = 1
#
#
#   2nd Priority => Iteration 3 :  left = [2] , right = [69, 71] , array = [10, 100, 2, 69, 71]
#       counter_left = 0, counter_right = 0, counter_array = 0
#       Repeat till counter_left < len(left array) and counter_right < len(right array) => 0 < 1 and 0 < 1
#           if left[counter_left] < right[counter_right]: => 10 < 100 True
#               array[counter_array] = left[counter_left] => array = [10, 100, 2, 69, 71]
#               increment counter_left by 1 => counter_left = 1
#               increment counter_array by 1 => counter_array = 1
#           else: False
#               array[counter_array] = right[counter_right]
#               increment counter_right by 1
#               increment counter_array by 1
#
#       Repeat till counter_left < len(left array) => 1 < 1 False
#           array[counter_array] = left_array[counter_left]
#           increment counter_array by 1
#           increment left_array by 1
#
#       Repeat till counter_right < len(right array) => 0 < 1 True
#           array[counter_array] = left_array[counter_left] => array = [10, 100, 2, 69, 71]
#           increment counter_array by 1    => counter_array = 2
#           increment left_array by 1       => left_array = 1
#
#
#
#
#
#
#
#


# FUNCTION FOR MERGING AND SORTING ARRAYS
def merge(left, right, container_):
    """
    Used for performing the merge and sorting
    :param left: left half of the container
    :param right: right half of the container
    :param container_: the actual container
    :return:
    """

    # LEFT HALF INDEX HOLDER
    l_idx = 0

    # RIGHT HALF INDEX HOLDER
    r_idx = 0

    # CONTAINER INDEX HOLDER
    c_idx = 0

    while l_idx < (len(left)) and r_idx < (len(right)):

        if left[l_idx] > right[r_idx]:
            container_[c_idx] = right[r_idx]
            r_idx += 1
        else:
            container_[c_idx] = left[l_idx]
            l_idx += 1

        c_idx += 1

    while l_idx < len(left):
        container_[c_idx] = left[l_idx]
        l_idx += 1
        c_idx += 1

    while r_idx < len(right):
        container_[c_idx] = right[r_idx]
        r_idx += 1
        c_idx += 1


# DIVIDE AND CONQUER FUNCTION
def mergesort(container_):
    """
    Used for performing divide and conquer
    :param container_: the list of elements in container
    :return:
    """
    # GET SIZE OF ARRAY
    n = len(container_)

    # CHECK FOR VALUES OF ATLEAST 2
    if n < 2:
        return

    # GET THE MIDDLE VALUE
    mid = n // 2

    # SLICE CONTAINER INTO TWO HALVES BASED ON INT MIDDLE VALUE
    left = container_[:mid]
    right = container_[mid:]

    # RECURSIVELY PERFORM MERGESORT ON TWO HALVES
    mergesort(left)
    mergesort(right)

    # CALL THE * MERGE FUNCTION
    merge(left, right, container_)


if __name__ == '__main__':
    my_list = list(range(100, 0, -1))
    print(my_list)
    mergesort(my_list)
    print(my_list)
