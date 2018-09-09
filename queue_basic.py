class flexQueue():
    cap = 4
    def __init__(self):
        self.data = [None] * flexQueue.cap
        self.front = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def qLength(self):
        return self.size
    
    def qCapacity(self):
        return len(self.data)
    
    def qFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
    
    def dequeue(self):
        if not self.isEmpty():
            element = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % len(self.data)
            self.size -= 1
            """ if 0 < self.size < len(self.data) // 4:
                self.resize(len(self.data)//2) """
            return element
        else:
            return None
    
    def enqueue(self, element):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        new_pos = (self.front + self.size) % len(self.data)
        self.data[new_pos] = element
        self.size += 1
        
    
    def resize(self, cap):
        old = self.data
        walk = self.front
        self.data = [None] * cap
        for k in range(len(old)):
            #print(walk,k,len(self.data),len(old))
            self.data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0

"""q=flexQueue()
q.enqueue(10)
q.enqueue(20)
print(q.qLength())
print(q.qFirst())
print(q.dequeue())"""