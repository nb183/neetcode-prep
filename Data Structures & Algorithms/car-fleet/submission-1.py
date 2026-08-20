class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Bruteforce: O(N^2) time, O(N) space
        # We can sort the cars by their starting position from closest to furthest from the target. 
        # Then, for every car, we look at the car directly in front of it and calculate exactly when they would collide. 
        # If they collide before or at the target, we merge them into a single fleet, update the trailing car's speed to
        # match the leader, and repeat this check for all remaining cars behind them.

        # Optimal: O(NlogN) time, O(N) space
        # We can sort both the cars' positions and speeds based on their starting positions in descending order 
        # Then, we can use a stack to track the time required to reach the destination using the formula (target - position) / speed. 
        # As we iterate, we push each car's time onto the stack. If a trailing car takes less than or equal time to reach the destination
        # it will inevitably catch up so we pop it.The final length of the stack will give number of fleets
        
        sorted_pair = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, s in sorted_pair:
            req_time = (target - pos) / s
            stack.append(req_time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        

        




