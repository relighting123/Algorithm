class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0

        num_set = set(nums)  # 숫자를 집합으로 변환
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
