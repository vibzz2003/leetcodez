class Solution:
    def digitCount(self, num: str) -> bool:
        hash_map = {}
        for n in num:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        # print(hash_map)
        for n in range(len(num)):
            if str(n) in hash_map.keys():
                if hash_map[str(n)] != int(num[n]):
                    return False
            elif str(n) not in hash_map.keys():
                if int(num[n]) != 0:
                    return False
        return True
        