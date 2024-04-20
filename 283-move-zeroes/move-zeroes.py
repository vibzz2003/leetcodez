class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # zeros_count = nums.count(0)
        # nums[:] = [num for num in nums if num!=0]
        # nums.extend([0] * zeros_count)

        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left+=1

        