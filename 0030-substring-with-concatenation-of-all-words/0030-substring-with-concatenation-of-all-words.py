from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count = Counter(words)
        word_len, num_words = len(words[0]), len(words)
        total_len = word_len * num_words
        ans = []

        for i in range(word_len):
            left, right = i, i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                current_count[word] += 1
                right += word_len

                while current_count[word] > word_count[word]:
                    current_count[s[left:left + word_len]] -= 1
                    left += word_len

                if right - left == total_len:
                    ans.append(left)

        return ans
