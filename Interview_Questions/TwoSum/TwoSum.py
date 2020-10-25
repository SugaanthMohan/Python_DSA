import itertools


class Solution:

    def twoSum(self, nums: [int], target: int) -> [int]:

        combinations = 2

        matches = list(
            filter(
                lambda x: x[0][1] + x[1][1] == target,
                itertools.combinations(enumerate(nums), combinations)
            )
        )

        return [matches[0][0][0], matches[0][1][0]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    results = Solution().twoSum(nums, target)
    print(results)

    nums = [3, 2, 4]
    target = 6
    results = Solution().twoSum(nums, target)
    print(results)

    nums = [3, 3]
    target = 6
    results = Solution().twoSum(nums, target)
    print(results)




