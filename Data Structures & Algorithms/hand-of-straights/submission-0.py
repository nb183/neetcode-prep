class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize:
            return False

        hand.sort()

        mp = defaultdict(int)
        for num in hand:
            mp[num] += 1
        
        for num in hand:
            if not mp[num]: continue

            for num2 in range(num, num + groupSize):
                if not mp[num2]: return False
                mp[num2] -= 1
        return True
        