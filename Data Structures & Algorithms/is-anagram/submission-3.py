class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        start = 0
        if len(s) != len(t):
            return False
        for char in s:
            if char in dict:
                dict[char] = dict[char]+1
            else:
                dict[char] = start + 1

        for char in t:
            if char in dict:
                dict[char] = dict[char]-1

        for val in dict.values():
            if val != 0:
                return False
        return True
        
        