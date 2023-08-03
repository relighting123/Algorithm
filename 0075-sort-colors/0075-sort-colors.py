class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, a, b = 0, 0, len(nums) - 1

        while i <= b:
            if nums[i] == 0:
                if i != a:  # Avoid unnecessary swap if already in the correct position
                    nums[a], nums[i] = nums[i], nums[a]
                a += 1
                i += 1
            elif nums[i] == 2:
                if i != b:  # Avoid unnecessary swap if already in the correct position
                    nums[b], nums[i] = nums[i], nums[b]
                b -= 1
            else:
                i += 1
