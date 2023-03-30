class Solution(object):
    def findCircleNum(self, isConnected):
        
        def dfs(e):
            if e in visit :
                return
            visit.append(e)
            for i in range(len(node)):
                if node[i][0] == e and node[i][1] not in visit:
                    dfs(node[i][1])
                
                    
        node,visit = [],[]
        n = len(isConnected)
        ans = 0
        
        #node 전환#
        for c in range(n):
            for r in range(n):
                if isConnected[c][r] == 1 and r != c:
                    
                    node.append((c,r))
        
        #DFS#
        for i in range(len(node)):
            
            if node[i][0] not in visit:                
                ans+=1
                dfs(node[i][0])
        
        return ans + n-len(visit)
                    
                    
    
 
        