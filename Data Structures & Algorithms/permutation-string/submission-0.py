import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mp = defaultdict(int)
        for c in s1:
            mp[c] += 1

        mp_cp = copy.deepcopy(mp)

        count = 0
        start = 0
        current = start + count
        while current < len(s2):
            c = s2[current]
            if c not in mp_cp:
                mp_cp = copy.deepcopy(mp)
                count = 0
                start = current + 1
            elif mp_cp[c] == 0:
                start += 1 
                mp_cp = copy.deepcopy(mp)
                count = 0
            else:
                count += 1
                mp_cp[c] -= 1
                if count == len(s1):
                    return True
            current = start + count
        return False