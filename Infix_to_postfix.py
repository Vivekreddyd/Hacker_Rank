expr='A*B-(C+D)+E'

operators=['*','-','(','+',')']
postfix_arr=[]
operator_stack=[]
for char in expr:
    if(not postfix_arr):
        postfix_arr.append(char)
    else:
        if(char in operators):
            if(operator_stack):
                if(operator_stack[-1]):
                    print("continue the program")