class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key].append((value, timestamp))
            return

        self.mp[key].append((value, timestamp))
   
        return None


    def get(self, key: str, timestamp: int) -> str:
        # Just do a binary search -> O(logN) tome

        if key not in self.mp or timestamp < self.mp[key][0][1]:
            return ""

        l, r = 0, len(self.mp[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.mp[key][mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return self.mp[key][r][0]


        

        
        

        
