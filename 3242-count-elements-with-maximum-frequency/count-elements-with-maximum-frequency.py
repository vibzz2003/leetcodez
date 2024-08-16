class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter = list(counter.values())
        maxcount = max(counter)
        return counter.count(maxcount) * maxcount
