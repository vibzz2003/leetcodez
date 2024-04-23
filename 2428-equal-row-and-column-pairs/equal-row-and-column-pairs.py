class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = Counter(tuple(x) for x in grid)
        return sum(rows[tuple(x)] for x in zip(*grid)) # zip(*grid) transposes the gris making rows into columns and columns into rows and then checks if the sum of count of rows as hashable objects is equal to the suym of count of columsnas hashable objects