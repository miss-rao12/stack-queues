#4.Implement a transfer function and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reverse order
import stack_basic
def transfer(S):
    T1=stack_basic.LimitedStack()
    T2=stack_basic.LimitedStack()
    while not S.isstackempty():
        T1.stackpush(S.stackpop())
    while not T1.isstackempty():
        T2.stackpush(T1.stackpop())
    while not T2.isstackempty():
        S.stackpush(T2.stackpop())
    return (S.data)

stk=stack_basic.LimitedStack()
for i in range(1,5):
    stk.stackpush(i)  
print(transfer(stk))
