class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        hash_set = {}
        for word in words:
            if word not in hash_set:
                hash_set[word] = 1
            else:
                hash_set[word] += 1
        
        top4 = [key for key, _ in sorted(hash_set.items(), key = lambda item : item[1], reverse = True)[:k]]

        return top4

            