class Dequeue:
    def __init__(self):
        self.dq = []
    def append(self,data):self.dq.append(data)
    def appendLeft(self,data):self.dq.insert(0,data)
    def pop(self):self.dq.pop()
    def popLeft(self):self.dq.pop(0)

