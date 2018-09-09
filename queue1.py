#7 Design a stack using a single queue as an instance variable, and only constant additional local memory within the method bodies. 
import queue_basic

class stck_using_Queue():
    def __init__(self):
        self.data=queue_basic.flexQueue()

    def isempty(self):
        return self.data.isEmpty()
    
    def length(self):
        return self.data.qLength()
    
    def  qpush(self,element):
        self.data.enqueue(element)
        return element
        

    def qpop(self):
        i=1
        while i<self.data.qLength():
            self.data.enqueue(self.data.dequeue())
            i+=1
        return(self.data.dequeue())

q1=stck_using_Queue()
for i in range(1,7):
    print(q1.qpush(i))
while  not q1.isempty():   
    print(q1.qpop())
print (q1.data.data)
        
