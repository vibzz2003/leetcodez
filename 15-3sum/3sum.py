class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        ordered_set = set()
        output = []

        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j<k:
                current = nums[i] + nums[j] + nums[k]
                if current == target:
                    ordered_set.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif current < target:
                    j+=1
                else:
                    k-=1
        
        for triplet in ordered_set:
            output.append(list(triplet))

        return output