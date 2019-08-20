#creating opening list 
openList = ["[","{","("]
#creating closeing list
closeList = ["]","}",")"]
def balance(myStr):
#create a Empty Stack 
    stack= []
    for i in myStr:
        if i in openList:     
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)   
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
            #if Both Parentheses are matched than POP element for List
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
 #driver code
print (balance("{[()](){}}")) 
print (balance("]{[()](){}}")) 
