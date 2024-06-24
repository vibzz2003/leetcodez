class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use hash set for o(n) logic
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            #we will have to check if it is the start of the sequence or not
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num+1 in num_set:
                    current_num+=1
                    current_streak+=1

                #updating the streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak