class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) -1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid +=1
                low +=1
                print(nums)
            elif nums[mid] == 1:
                mid+=1
                print(nums)
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
                print(nums)
