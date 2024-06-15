class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4] -> pointer 1 pe ayega -> 1 chodh ke baaki sabko multiply karna hoga-> 1 ko ans se replace karna hoga
        # hum jabh koi element par aaye -> uss element ko 1 karde -> sabka mul le -> element ki jagah daal de
        size = len(nums)
        ans = [1]*size
        left = 1
        right = 1
        for i in range(size):
            ans[i] *= left
            left *= nums[i]

        for i in range(size-1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
