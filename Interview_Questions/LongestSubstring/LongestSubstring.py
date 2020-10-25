import itertools


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        max_possibility = len(s) // 2

        for size in range(max_possibility, 0, -1):
            for combinations in itertools.combinations(s, size):
                search_str = "".join(combinations)
                temp = s.split(search_str, 1)
                for seq in temp:
                    if search_str in seq:
                        return len(search_str)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("bbbbb"))
