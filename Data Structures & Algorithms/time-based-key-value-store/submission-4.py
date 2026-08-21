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

        if key not in self.mp or timestamp < self.mp[key][0][1]:
            return ""
        l, r = 0, len(self.mp[key]) - 1
        mid = -1
        temp = ""

        while l <= r:
            mid = (l + r) // 2
            curr = self.mp[key][mid][1]

            if curr > timestamp:
                r = mid - 1
            elif curr < timestamp:
                l = mid + 1
                temp = self.mp[key][mid][0]
            else:
                return self.mp[key][mid][0]
        return temp



        

        
        

        
