class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:

		res = ''
		for ele in zip(*strs):
			if len(set(ele)) > 1:
				return res
			else:
				res += ele[0]
		return res