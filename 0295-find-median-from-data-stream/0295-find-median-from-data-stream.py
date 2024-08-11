import heapq

class MedianFinder:

    def __init__(self):
        self.lowerpart = []  # max-heap (invert sign to simulate)
        self.longerpart = []  # min-heap

    def addNum(self, num: int) -> None:
        if not self.lowerpart or num <= -self.lowerpart[0]:
            heapq.heappush(self.lowerpart, -num)
        else:
            heapq.heappush(self.longerpart, num)

        if len(self.lowerpart) > len(self.longerpart) + 1:
            heapq.heappush(self.longerpart, -heapq.heappop(self.lowerpart))
        elif len(self.longerpart) > len(self.lowerpart):
            heapq.heappush(self.lowerpart, -heapq.heappop(self.longerpart))

    def findMedian(self) -> float:
        if len(self.lowerpart) == len(self.longerpart):
            return (-self.lowerpart[0] + self.longerpart[0]) / 2.0
        else:
            return -self.lowerpart[0]
