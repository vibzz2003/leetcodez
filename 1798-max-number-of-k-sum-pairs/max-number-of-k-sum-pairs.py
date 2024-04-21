class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #isme hume kya karna hai
        #step 1 - pointer initialise karne hai 2
        #total main se minus karte jaana hai jaise pointer aage badhe 
        #limit 2 ki, agar zero nahi toh vapas sum ke equal 
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0
        while left<right:
            if nums[left] + nums[right] == k:
                count+=1
                left+=1
                right-=1
            elif nums[left] + nums[right] < k:
                left+=1
            else:
                right-=1
        return count