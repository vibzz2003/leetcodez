class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        oc1 = sorted(s)
        og1 = ''.join(oc1)

        og2 = ''.join(sorted(t, key=lambda x: x.lower()))

        if og1!=og2:
            return False
        return True