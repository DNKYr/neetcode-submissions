class MinStack:

    def __init__(self):
        self.minS = []
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minS) == 0:
            self.minS.append(val)
        else:
            self.minS.append(min(self.minS[-1], val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]
        
