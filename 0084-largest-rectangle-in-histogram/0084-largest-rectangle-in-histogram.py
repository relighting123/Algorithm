class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        area = 0
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area,  h*w)
            stack.append(i)
        return area