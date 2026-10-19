class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0

        if sum(gas) < sum(cost):
            return -1

        start = 0

        for i in range(len(gas)):
            current_gas += gas[i]
            if current_gas < cost[i]:
                start = i + 1
                current_gas = 0
            else:
                current_gas -= cost[i]
        
        return start