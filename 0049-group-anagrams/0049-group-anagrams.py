from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert(string):
            base = [0] * 26
            for char in string:
                idx = ord(char) - ord('a')
                base[idx] += 1
            return tuple(base)
        
        dict_a = defaultdict(list)
        
        for string in strs:
            key = convert(string)
            dict_a[key].append(string)
        
        return list(dict_a.values())