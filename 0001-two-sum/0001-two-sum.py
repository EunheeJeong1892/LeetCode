class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3,2,4], 6
        
        head = 0
        cur = 1

        while head <= len(nums) -1:
            while cur < len(nums):
                if nums[head] + nums[cur] == target:
                    return [head, cur]
                cur += 1

            head += 1
            cur = head + 1
        