#1.Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T, so that that elements that starts at the top of S is the first to be inserted into T, and element at the bottom of S ends up at the top of T.
import stack_basic
import random
S=stack_basic.LimitedStack()
T=stack_basic.LimitedStack()
def signtransfer(S,T):
    yy=S.stackpush(20)
    z=S.stackpush(30)
    print (z)
    y=S.stackpop()
    a=S.stackpop()
    print(y)
    m=T.stackpush(y)
    m=T.stackpush(a)
    print (m)
   
   
signtransfer(S,T)