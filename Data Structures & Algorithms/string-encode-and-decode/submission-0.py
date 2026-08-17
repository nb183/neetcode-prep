class Solution:

    def __init__(self):
        self.indexes = []

    def encode(self, strs: List[str]) -> str:

        combined_str = ""
        start = 0
        for string in strs:
            combined_str += string
            end = start + len(string)
            self.indexes.append((start, end))
            start = end
        return combined_str


    def decode(self, s: str) -> List[str]:
        ans = []
        for i, j in self.indexes:
            ans.append(s[i:j])
        return ans
