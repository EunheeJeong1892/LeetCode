class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = -1 
        last_index = -1
        for i, num in enumerate(nums):
            if num == target:
                if start_index == -1:
                    start_index = i
                else:
                    last_index = i

        return [start_index, last_index]
                