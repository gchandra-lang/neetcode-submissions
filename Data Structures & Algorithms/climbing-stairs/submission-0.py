class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prevprev = 1
        prev = 2
        current = 0
        for _ in range(3, n+1):
            current = prevprev + prev
            prevprev = prev
            prev = current
        return prev
