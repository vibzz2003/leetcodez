class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #prev, curr, next leke kar dakte hain
        #agar prev khaali hai and curr khaali,and next khaali hai toh curr pe laga do
        #agar prev bahar curr khaali and next bhara toh false
        size = len(flowerbed)
        i = 0
        while i<size and n>0:
            if flowerbed[i]==0:
                prev = flowerbed[i-1] if i-1>=0 else 0
                nextp = flowerbed[i+1] if i+1<size else 0
                if prev == 0 and nextp == 0:
                    flowerbed[i] = 1
                    n-=1
                    i+=1
            i+=1

        return n==0 
                
            