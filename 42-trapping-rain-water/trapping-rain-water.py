class Solution:
    def trap(self, height: List[int]) -> int:
        # n non negative integer
        # width 1
        # 0102
        # answer = 1
        if not height:
            return 0
        
        n = len(height)

        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        water = 0

        while left<=right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right-=1
        
        return water