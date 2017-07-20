class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            if self.minstack[-1] >=x:
                self.minstack.append(x)
            
                

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.minstack[-1] == self.stack[-1]:
                self.minstack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
