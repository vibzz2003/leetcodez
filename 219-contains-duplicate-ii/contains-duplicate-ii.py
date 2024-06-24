class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash1={}

        for i,num in enumerate(nums):
            if num in hash1 and i - hash1[num] <=k:
                return True
            else:
                hash1[num] = i
        return False