class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        size = len(gain)
        list1 = [0]*(size+1)
        alt = 0
        maxalt = float('-inf')

        for i in range(0, len(list1)):
            list1[i] = alt + gain[i-1] if i-1>=0 else 0
            alt += gain[i-1] if i-1>=0 else 0
            maxalt = max(maxalt, list1[i])
        
        return maxalt