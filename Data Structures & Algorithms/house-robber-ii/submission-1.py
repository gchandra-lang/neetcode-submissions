class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prevprev1 = nums[0]
        prev1 = max(nums[1], nums[0])

        for i in range(2, len(nums)-1):
            current = max(prev1, prevprev1 + nums[i])
            prevprev1 = prev1
            prev1 = current
        
        prevprev2 = nums[1]
        prev2 = max(nums[2], nums[1])

        for i in range(3, len(nums)):
            current = max(prev2, prevprev2 + nums[i])
            prevprev2 = prev2
            prev2 = current

        return max(prev2, prev1)

        
        

