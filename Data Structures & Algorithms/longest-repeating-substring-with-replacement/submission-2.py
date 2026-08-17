class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # Bruteforce -> For every possible substring, find the frequency of the most
    # repeated character. Subtract this frequency from the length of the substring
    # to get the number of replacements required. If the required replacements are
    # less than or equal to k, the substring is valid, so update the maximum length.
    # To avoid recomputing frequencies for every substring, for each i, maintain a
    # frequency map and incrementally update it as j moves from i to the end.
    # TC -> O(26 * N^2) = O(N^2), SC -> O(1)

    # Optimal -> Instead of checking every substring, use a sliding window. Expand
    # the window by moving r and update the character frequencies. For each window,
    # calculate the number of replacements required as:
    #       window_length - frequency_of_most_common_character
    # If this is <= k, the window is valid, so update the maximum length. Otherwise,
    # shrink the window once from the left by moving l and decreasing that       
    # character's frequency. We do not need to keep shrinking until the window #
    # becomes valid, since we are only interested in finding a window larger than    
    # the   best one already seen. Continue expanding r until the end of the string.
    # TC -> O(26 * N) = O(N), SC -> O(1)

        max_len = 0
        max_freq = 0
        l = r = 0

        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1

            max_freq = max(max_freq, freq[s[r]])
            length = r - l + 1

            if length - max_freq <= k:
                max_len = max(max_len, length)
            else:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

            r += 1
        return max_len
