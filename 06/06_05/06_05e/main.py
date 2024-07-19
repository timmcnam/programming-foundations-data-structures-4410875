from collections import deque

def check_matching_parentheses(s):
    stack = deque() #create a stack deque
    for char in s:
        if char == "(":
            stack.append(char) #add the opening bracket to the stack
        elif char == ")":
            if not stack: # if we begin with an ending bracket, we need to return false
                return False
            stack.pop() # pop the top of the stack to signify the match being found
    return len(stack) == 0 #return whether the stack is equal to zero or not

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))
