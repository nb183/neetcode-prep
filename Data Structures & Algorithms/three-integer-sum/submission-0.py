class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Bruteforce:
        # We can try all possible triplets and check if they satisfy the conditions.
        # To handle duplicates, for each valid triplet, first check whether it is a already present in the answer.
        # TC -> O(N^3), SC -> O(N)

        # Minor Refactor:
        # Use a set to help track duplicates and avoid repeatedly adding the same triplet.

        # Optimal:
        # First, sort the array and traverse through each element. Fix the first number (num1),
        # and use two pointers, l and r, for the remaining two numbers. l points to the element
        # immediately after num1, while r points to the last element.
        # If num1 + nums[l] + nums[r] equals the target, add the triplet and move both l and r.
        # If the sum is smaller than the target, increment l; otherwise, decrement r.
        # Be careful to skip duplicate values for num1, nums[l], and nums[r] so that the same
        # triplet is not added multiple times.
        # TC -> O(N^2), SC -> O(1), excluding the output array.

        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1

            target = - nums[i]
            while l < r:
                cur_sum = nums[l] + nums[r]
                
                if cur_sum == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif cur_sum < target:
                    l += 1
                else:
                    r -=1
        return ans