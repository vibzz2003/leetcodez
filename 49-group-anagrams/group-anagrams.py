class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict ={}
        for word in strs:
            sortedword = "".join(sorted(word)) #why using join?? so that when we sort the string converts tot a list, here by applying join to an empty string it converts into a string again

            if sortedword not in dict:
                dict[sortedword] = [word] #if sorted word is not in the dict, then we add the sorted word as the key and the word as the value, we add trhe word as a list in the dict of sorted word
            else:
                dict[sortedword].append(word) #if found, then append it in the already found list of the sorted word
        
        result = []
        for item in dict.values():
            result.append(item)
        
        return result