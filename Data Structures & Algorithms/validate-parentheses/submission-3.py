class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <2:
            return False

        brackets = {
            "(":")",
            "{":"}",
            "[":"]"
            }

        st = []
        for i in s:
            if i in brackets:
                st.append(i)
            elif i in brackets.values():
                if st and i == brackets[st[-1]]:
                    st.pop()
                else:
                    return False
        
        if not st:
            return True
        return False
        