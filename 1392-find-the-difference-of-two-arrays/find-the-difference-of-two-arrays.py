class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #set ke andar duplicate values nahi aate 
        answer = [[],[]]
        size1 = len(nums1)
        size2 = len(nums2)

        if size1 == 0:
            answer[1] = nums2
        elif size2 == 0:
            answer[0] = nums1
        else:
            nums1 = set(nums1)
            nums2 = set(nums2)
        
            for num in nums1.copy(): #u cannot iterate over a set and modify it at the same time
                if num in nums2:
                    nums1.remove(num)
                    nums2.remove(num)

            num1 = list(nums1)
            num2 = list(nums2)
            answer[0] = num1
            answer[1] = num2
        
        return answer
