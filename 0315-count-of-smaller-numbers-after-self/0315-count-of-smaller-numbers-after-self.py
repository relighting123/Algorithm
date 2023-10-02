class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.bit[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= index & -index
        return result

class Solution(object):
    def countSmaller(self, nums):
        sorted_nums = sorted(nums)
        result = [0] * len(nums)
        bit = BinaryIndexedTree(len(nums))

        for i in range(len(nums) - 1, -1, -1):
            index = bisect.bisect_left(sorted_nums, nums[i]) + 1
            count = bit.query(index - 1)
            result[i] = count
            bit.update(index, 1)

        return result