class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHashmap = [0]*26
        tHashmap = [0]*26

        for char in s:
            letter = ord(char) - ord('a')
            sHashmap[letter] += 1

        for char in t:
            letter = ord(char) - ord('a')
            tHashmap[letter] += 1

        for i in range(26):
            if sHashmap[i] != tHashmap[i]:
                return False
            
        return True