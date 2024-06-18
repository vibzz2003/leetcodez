class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #srts.sort() se o(nlogn) main chala jaata hai, kar toh voh bhi sakte hai
        min_length = min(len(s) for s in strs)
        if not strs:
            return ""
        #iterating for the smallest length
        for i in range(min_length):
            #now iterating through all elemnts from 1st index
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i] #if does not match up then return the prefix found so far
        return strs[0][:min_length]

        