class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Initialize the DP table
        dp = [[False for _ in range(n)] for _ in range(n)]
        longest_palindrome = ""
        # Fill the DP table for substrings of length 1
        for i in range(n):
            dp[i][i] = True
            longest_palindrome = s[i]
        # Fill the DP table for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest_palindrome = s[i:i+2]
        # Fill the DP table for substrings of length greater than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > len(longest_palindrome):
                        longest_palindrome = s[i:j+1]
        return longest_palindrome