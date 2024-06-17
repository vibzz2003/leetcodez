class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 1-1-1-1-1-1-1-1 -> candies
        # each - atleast 1 candy toh jayengi
        # n candies toh gayi
        # higher rating children -> more candies
        # 1-2-1-2
        # 4 candies 
        # 2 - 1 candy extra => 2 more candies -> 6 candy
        n = len(ratings)
        candies = [1]*n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        
        return sum(candies)
