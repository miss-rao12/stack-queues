#6.Suppose you have three nonempty stacks R, S and T. Describe a sequence of operations that results in S storing all elements originally in T below of S’s original elements, with both sets of those elements in their original configuration. For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].
import stack_basic
def stck6(R,S,T):
    r_count=R.stacklength()
    while not S.isstackempty():
        R.stackpush(S.stackpop())
    while not T.isstackempty():
        R.stackpush(T.stackpop())
    while R.stacklength()>r_count:
            S.stackpush(R.stackpop())
    return (S.data,R.data)

def sub1():
    R=stack_basic.LimitedStack()
    S=stack_basic.LimitedStack()
    T=stack_basic.LimitedStack()
    for i in range(1,4):
        R.stackpush(i)
    print (R.data)
    for i in range(4,6):
        S.stackpush(i)
    for i in range(6,10):
        T.stackpush(i)  
    print(stck6(R,S,T))
sub1()