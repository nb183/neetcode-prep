class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Bruteforce -> For all the substrings, we can for each substring, take the count of the most repeated character. We then subtract this from the length of the substring. We then check if the resulting value is less than or equal to K. If it is, it means we can make valid replacements. Get the max of all such valid replacements. To make sure we dont compute the counts for each substring, we incrementally update the counts in a map when we move "j" for each value of i, from i to j.
        # TC -> O(26. N^2), SC -> O(1)

        # Optimal -> Instead of doing it for every substring, we can use sliding window to check in linear time. The frequency check logic will still hold.So, We start the window with i, j at first character, increase the window and update the max until the condition holds. If the condtion doesnt hold then we now shrink the window decreasing the frequency. We dont need to reevalute the max here as these will be smaller. We run the loop until r < lenth of string
         # TC O(26.N), SC -> O(1)

        max_len = 0
        max_freq = 0
        l = r = 0

        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1

            max_freq = max(max_freq, freq[s[r]])
            length = r - l + 1

            if length - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

            r += 1
        return max_len
