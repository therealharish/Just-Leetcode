class MinStack:
    
    def __init__(self):
        self.a = []
        self.min_ = float("inf")

    def push(self, val: int) -> None:
        self.a.append(val)
        if val<self.min_:
            self.min_ = val

    def pop(self) -> None:
        x = self.a.pop()
        if x==self.min_:
            if len(self.a):
                self.min_=min(self.a)
            else:
                self.min_=float("inf")

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.min_
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()