import heapq

class MedianFinder:

    def __init__(self):
        self.lowerpart = []  # max-heap (invert sign to simulate)
        self.longerpart = []  # min-heap

    def addNum(self, num: int) -> None:
        if not self.longerpart or num >= self.longerpart[0]:
            heapq.heappush(self.longerpart, num)
        else:
            heapq.heappush(self.lowerpart, -num)

        # Balance the heaps: Ensure longerpart (min-heap) always has the extra element when odd
        if len(self.longerpart) > len(self.lowerpart) + 1:
            heapq.heappush(self.lowerpart, -heapq.heappop(self.longerpart))
        elif len(self.lowerpart) > len(self.longerpart):
            heapq.heappush(self.longerpart, -heapq.heappop(self.lowerpart))

    def findMedian(self) -> float:
        if len(self.lowerpart) == len(self.longerpart):
            return (-self.lowerpart[0] + self.longerpart[0]) / 2.0
        else:
            return self.longerpart[0]
