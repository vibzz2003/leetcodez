class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        j = 0
        k = len(height)-1
        while j<k:
            area = abs(k-j) * min(height[j], height[k])
            max_area = max(max_area, area)
            if height[j]<height[k]:
                j+=1
            else:
                k-=1
        return max_area