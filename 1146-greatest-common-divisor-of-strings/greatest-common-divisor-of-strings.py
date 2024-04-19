class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        gcd_len = math.gcd(len1, len2) #gcd of the lengths

        gcd_str = str1[:gcd_len]

        if str1 == gcd_str * (len1//gcd_len) and str2 == gcd_str * (len2//gcd_len):
            return gcd_str
        else:
            return ""

