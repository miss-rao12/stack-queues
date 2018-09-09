class LimitedStack:
    capacity=10
    def __init__(self):
        self.data=[]
        self.count=0

    def isstackempty(self):
        return self.count==0

    def isstackfull(self):
	    return self.count==LimitedStack.capacity
			
    def stacklength(self):
	    return self.count
			
    def stackpeek(self):
        if not self.isstackempty():
        	return self.data[-1]
			
    def stackpush(self,element):
	    if not self.isstackfull():
		    self.data.append(element)
		    self.count+=1
	    return self.data
			
    def stackpop(self):
        if not self.isstackempty():
            self.count-=1
            return self.data.pop()




'''
stk=LimitedStack()
assert(stk.isstackempty()==True)
stk.stackpush(20)
stk.stackpush(30)

assert(stk.isstackempty()==False)
assert(stk.isstackfull()==False)
assert(stk.stacklength()==2)
assert(stk.stackpeek()==30)
#assert(stk.stackpush(30)==[20,30,30])
stk.stackpop()
#assert(stk.stacklength()==2'''