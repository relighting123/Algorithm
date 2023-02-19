class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fac(n):
            if n==1:
                return 1
            return n*fac(n-1)
        return fac(2*n)/(fac(n+1)*fac(n))
        