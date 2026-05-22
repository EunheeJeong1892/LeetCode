class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        result = [x for pair in zip(nums[:half], nums[half:]) for x in pair]

        return result