class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for i, c in enumerate(s):
            if c == ")":
                if not star and not left:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
            elif c == "(":
                left.append(i)
            else:
                star.append(i)

        print(left, star)
        if not left and not star:
            return True
        
        if len(left) > len(star):
            return False

        left_p, star_p = 0, 0
        while left_p < len(left) and star_p < len(star):
            if left[left_p] <= star[star_p]:
                left_p += 1
            star_p += 1

        if left_p == len(left):
            return True

        return False

        

        