#3 Modify ArrayStack implementation so that the stack’s capacity is limited to maxlen elements. If push is called when the stack is at full capacity, throw a Full exception.
import stack_basic as sb 
class ArrayStack(sb.LimitedStack):#inheritance of the class
    def __init__(self,mlen):
        super().__init__()
        sb.LimitedStack.capacity=mlen 
    def stackpush(self,dat):
        if self.isstackfull():
            stackfull=Exception()
            raise stackfull
        else:
            self.data.append(dat)
            self.count+=1

stk=ArrayStack(5)#creating of the object
for i in range(1,7):
    stk.stackpush(i)