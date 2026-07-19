class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-","*", "/"]
        st = []
        for i in tokens:
            if i in operations:
                b = st.pop()
                a = st.pop()
                c = int(eval(f"{a}{i}{b}"))
                st.append(c)
            else:
                st.append(int(i))
        return st.pop()