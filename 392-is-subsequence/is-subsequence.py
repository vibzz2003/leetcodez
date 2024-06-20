class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        a1 = list(t)
        a2 = list(s)
        for i in range(len(a1)):
            if index < len(a2) and a1[i]==a2[index]:
                index+=1
        return index == len(a2)
        #index maintain rakha
        #0 se initialise kia
        #agar index a2 ki len se chotta hai and a1[i] == a2[index], tabh index ko increase kiya
        #and return kara when index becomes equal to len of a2 agar nahi toh false