def isValid(string):
    stack = []
    if len(string)%2 != 0: return False
    for letter in string:
        if letter == '[' or letter == '(' or letter == '{':
            stack.append(letter)
        # if letter == ']' and len(stack) != 0 and ('[' in stack):
        #     stack.pop()
        # if letter == '}' and len(stack) != 0 and ('{' in stack):
        #     stack.pop()
        # if letter == ')' and len(stack) != 0 and ('(' in stack):
        #     stack.pop()
        elif letter == ']' and len(stack) != 0 and (stack[-1] == '['):
            stack.pop()
        elif letter == '}' and len(stack) != 0 and (stack[-1] == '{'):
            stack.pop()
        elif letter == ')' and len(stack) != 0 and (stack[-1] == '('):
            stack.pop()
        else:
            return False
    return len(stack) == 0

print(isValid('[](){}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid("({{{{}}}))"))
print(isValid('()'))
print(isValid("([}}])"))