
class Solution:
    def median_of_two_lists(self, list_1: [int], list_2: [int]) -> float:

        collateral_list = sorted(list_1 + list_2)

        if len(collateral_list) == 0:
            return 0.0
        else:
            mid = len(collateral_list) // 2
            return (collateral_list[mid] + collateral_list[~mid]) / 2


if __name__ == '__main__':

    input_pairs_1 = [
        list(range(1, 10)),
        [1, 2],
        [1, 3],
        [],
        []
    ]
    input_pairs_2 = [
        list(range(11, 20)),
        [3, 4],
        [2],
        [1],
        []
    ]

    for pairs in zip(input_pairs_1, input_pairs_2):
        print(Solution().median_of_two_lists(*pairs))
