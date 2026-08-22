class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)

        max_len = 0
        for num in S:
            if num - 1 in S:
                continue
            
            length = 1
            start = num + 1

            while start in S:
                length += 1
                start += 1

            max_len = max(max_len, length)
        
        return max_len

        