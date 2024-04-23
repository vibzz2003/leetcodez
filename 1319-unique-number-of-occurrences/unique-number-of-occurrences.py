class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for num in arr:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num] = 1


        occurences = set()

        for count in hash_map.values():
            if count in occurences:
                return False
            occurences.add(count)

        return True        

