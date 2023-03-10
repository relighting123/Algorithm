from collections import deque

class Solution(object):
    def buddyStrings(self, s, goal):
        cnt=0
        ans=False
        que = []
        
        if(len(s)!=len(goal)) :
            return False
        
        distinct_yn = len(set(s)) == len(s)
        if(s==goal and distinct_yn is False):
            return True
        
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                que.append((s[i],goal[i]))
                if len(que)>2:
                    return False
        if len(que) == 2:
            a,b = que.pop()
            c,d = que.pop()
            if (b,a) == (c,d):
                return True
            else :
                return False
        return False
                           
                