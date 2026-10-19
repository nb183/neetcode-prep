class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}

        for i, c in enumerate(s):
            last_pos[c] = i

        ans = []
        length, end = 0, 0
        i = 0

        while i < len(s):
            length += 1
            end = max(end, last_pos[s[i]])
            if end <= i:
                ans.append(length)
                length = 0
            i += 1

        return ans