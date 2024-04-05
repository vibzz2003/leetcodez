class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        s = len(nums)
        i = 0
        j = i+1
        while(i<s and j<s):
            if nums[i]==nums[j]:
                return nums[j]
            i+=1
            j+=1
