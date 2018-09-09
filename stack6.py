#5.HTML generally allows optional attributes to be expressed as part of an opening tag. The general form used is <name attribute1 = “value1” attribute2 = “value2”>. Write function that checks whether tags or matched properly, even when an opening tag may include one or more attributes.
import stack_basic
def evaluatehtmltag(str):
    stk=stack_basic.LimitedStack()
    start=str.index('<')
    while  start!=-1:
        end=str.find('>',start+1)
        if end==-1:
            return False
        tok=str[start+1:end]
        if not tok.startswith('/'):
            stk.stackpush(tok)
        else:
            if stk.isstackempty():
                return False
            if tok[1:]!=stk.stackpop():
                return False
        start=str.find('<',end+1)
    return stk.isstackempty()
print (evaluatehtmltag('<html> </html>'))
assert(evaluatehtmltag('<html>')==False)