#2.Implement a function that reverses a list of elements by pushing them onto a stack in one order, and write them back to the list in reversed order.
import stack_basic
def reverse_1(list1):
    s1=stack_basic.LimitedStack()
    for ele in list1:
        s1.stackpush(ele)
    list1=[]
    while  not s1.isstackempty():
        list1.append(s1.stackpop())
    return(list1)

print ( reverse_1([1,2,3,4]))