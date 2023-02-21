# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([])
        queue.append(root)
        if root is None:
            return 0
        answer=1
        while(queue):
            level_size = len(queue)
            for i in range(level_size):
                currTree = queue.popleft()
                nextleftTree = currTree.left
                nextrightTree = currTree.right
                if(nextleftTree is None and nextrightTree is None):
                    return answer
                elif(nextleftTree is None):
                    queue.append(currTree.right)
                elif(nextrightTree is None):
                    queue.append(currTree.left)   
                else:
                    queue.append(currTree.left)
                    queue.append(currTree.right)
                
            answer+=1
        
        return answer
        