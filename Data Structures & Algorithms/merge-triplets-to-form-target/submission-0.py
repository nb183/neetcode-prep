class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if x == target[0]:
                    current[0] = x
                if y == target[1]:
                    current[1] = y
                if z == target[2]:
                    current[2] = z

            if current[0] == target[0] and current[1] == target[1] and current[2] == target[2]:
                return True
                
        return False
        
 