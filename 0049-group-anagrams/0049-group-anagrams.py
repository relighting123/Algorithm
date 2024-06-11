from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert(string):
            base = [0] * 26
            for char in string:
                base[ord(char) - ord('a')] += 1
            return tuple(base)
        
        dict_a = defaultdict(list)
        for string in strs:
            dict_a[convert(string)].append(string)
        
        return list(dict_a.values())