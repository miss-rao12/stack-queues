#8 Design a queue using two stacks as instance variables, such that all queue operations execute in amortized O(1) time.
import stack_basic
S=stack_basic.LimitedStack()
T=stack_basic.LimitedStack()
class Queue_using_stk():
    def __init__(self):
        self.S=stack_basic.LimitedStack()
        self.T=stack_basic.LimitedStack()
    def qempty(self):
        return self.S.isstackempty()
        
    def qlength(self):
        return self.S.stacklength()
    
    def  enq(self,element):
        self.S.stackpush(element)
        return element
    
    def dq(self):
    
        while not self.S.isstackempty():
            self.T.stackpush(self.S.stackpop())
        temp=self.T.stackpop()
        while not self.T.isstackempty():
            self.S.stackpush(self.T.stackpop())
        return temp

s1=Queue_using_stk()
for i in range(1,7):
    print(s1.enq(i))
while  not s1.qempty():   
    print(s1.dq())
        

