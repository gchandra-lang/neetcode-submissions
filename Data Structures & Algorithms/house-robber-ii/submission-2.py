class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear(houses: List[int]) -> int:
            prevprev1 = houses[0]
            prev1 = max(houses[1], houses[0])

            for i in range(2, len(houses)):
                current = max(prev1, prevprev1 + houses[i])
                prevprev1 = prev1
                prev1 = current
            
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

        
        

