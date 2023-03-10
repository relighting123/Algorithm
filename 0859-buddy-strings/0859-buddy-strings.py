
class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        if len(diff) != 2:
            return False
        
        return diff[0] == diff[1][::-1]