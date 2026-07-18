class MinStack:

    def __init__(self):
        self.input_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.input_stack.append(val)

    def pop(self) -> None:
        if self.input_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.input_stack.pop()
                    
    def top(self) -> int:
        return self.input_stack[-1]
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

        
