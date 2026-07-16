class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = ""
        for i in s:
            while i in sub:
                sub = sub[1:]
            sub = sub + i
            max_len = max(max_len, len(sub))
        return max_len