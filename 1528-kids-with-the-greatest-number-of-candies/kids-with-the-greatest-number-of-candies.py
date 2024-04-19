class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        list1 = []
        for i in candies:
            if i + extraCandies >= max_candy:
                list1.append(True)
            else:
                list1.append(False)
        return list1