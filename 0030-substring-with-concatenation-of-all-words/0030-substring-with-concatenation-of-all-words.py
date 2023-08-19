from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def search(l, p, r, dic_memo, dic_idx, cnt):
            word_freq = Counter(words)

            while True:
                if r > len(s):
                    break
                target_s = s[p:r]
                if target_s not in words:
                    cnt = 0
                    dic_memo = word_freq
                    dic_idx = {}
                    search(p + len_word, p + len_word, p + 2 * len_word, dic_memo, dic_idx, cnt)
                    break

                if dic_memo[target_s] == 0:
                    min_target_s_idx = dic_idx[target_s][0]

                    for i in range(l, min_target_s_idx + 1, len_word):
                        dic_memo[s[i:i+len_word]] += 1
                        dic_idx[s[i:i+len_word]].pop(0)
                        cnt -= 1

                    search(min_target_s_idx + len_word, p, p + len_word, dic_memo, dic_idx, cnt)
                    break

                if target_s in words:
                    if target_s in dic_idx: 
                        dic_idx[target_s].append(p)
                    else:
                        dic_idx[target_s] = [p]
                    dic_memo[target_s] -= 1
                    cnt += 1

                    if cnt == len_ans:
                        ans.append(l)
                        dic_memo[s[l:l+len_word]] += 1
                        dic_idx[s[l:l+len_word]].pop(0)
                        cnt -= 1
                        search(l + len_word, p + len_word, p + len_word * 2, dic_memo, dic_idx, cnt)
                        break

                l = l
                p = p + len_word
                r = r + len_word

        len_ans, len_word = len(words), len(words[0])        
        ans = []
        
        for i in range(len_word):
            l, p, r = 0, 0, len_word  
            dic_memo = Counter(words)
            dic_idx = {}            
            cnt = 0
            search(l + i, p + i, r + i, dic_memo, dic_idx, cnt)
        return ans
