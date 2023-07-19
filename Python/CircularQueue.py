##leetcode number 622
class MyCircularQueue:

    def __init__(self, k: int):

        self.queue = []
        self.size = k
        

    def enQueue(self, value: int) -> bool:


        if len(self.queue) == self.size:

            return False
        self.queue = self.queue + [value]
        
        
        
        return True

        

    def deQueue(self) -> bool:

        if self.isEmpty() == False:
            self.queue.remove(self.Front())
            return True
        return False
    
    def Front(self) -> int:

        if self.isEmpty():
            return -1

        return self.queue[0]
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1

        return self.queue[-1]
        

    def isEmpty(self) -> bool:

        if self.queue:
            return False
        
        return True
        

    def isFull(self) -> bool:

        if len(self.queue) == self.size:
            return True
        return False



        
