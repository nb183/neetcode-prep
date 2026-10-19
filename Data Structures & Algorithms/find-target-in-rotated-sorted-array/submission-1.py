class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            
        pivot = r

        def binary_search(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
            
        right = binary_search(pivot, len(nums) - 1)
        if right != -1:
            return right
        
        left = binary_search(0, pivot - 1)

        return left if left != -1 else -1