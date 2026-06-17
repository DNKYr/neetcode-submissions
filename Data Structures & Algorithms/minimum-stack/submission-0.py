class MinStack:

    def __init__(self):
        self.minS = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if len(self.minS) == 0:
            self.minS.append(val)
        else:
            self.minS.insert(0, min(self.minS[0], val))
        

    def pop(self) -> None:
        self.stack.pop(0)
        self.minS.pop(0)
        

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.minS[0]
        
