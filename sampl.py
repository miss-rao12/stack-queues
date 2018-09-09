import stack_basic
import random
S=stack_basic.LimitedStack()
T=stack_basic.LimitedStack()
def signtransfer(S,T):
    yy=S.stackpush(random.randint(1,20))
    print (yy)
    y=S.stackpop()
    #a=S.stackpop()
    print(y)
    m=T.stackpush(y)
   # m=T.stackpush(a)
    print (m)
   
   
signtransfer(S,T)