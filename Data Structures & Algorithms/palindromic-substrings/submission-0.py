class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    res+=1
        return res
