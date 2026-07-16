class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = list(s)
        listt = list(t)
        listtt = list(t)
        if len(s)==len(t):
            for i in listt:
                if i in lists:
                    listtt.remove(i)
                    lists.remove(i)
        if len(lists)==len(listtt)==0:
            return True
        else: 
            return False

        