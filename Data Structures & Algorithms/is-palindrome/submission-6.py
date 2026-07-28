class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                ss += i.lower()
        print(ss)

        return list(ss) == list(ss)[::-1]