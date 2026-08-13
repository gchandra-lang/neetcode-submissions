class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        if not nums:
            return None

        prevprev = nums[0]
        prev = max(nums[0], nums[1])
            
        for i in range(2, len(nums)):
            current = max(prev, prevprev + nums[i])
            prevprev = prev
            prev = current

            
        return prev
