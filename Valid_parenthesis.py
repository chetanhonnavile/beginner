#Validate parenthesis

def is_match(p1,p2):
    if p1 == '{' and p2 == '}':
        return True
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    is_balanced = True
    index = 0
    stack = []
    dict = {"{":"}","[":"]","(":")"}
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '{[(':
            stack.append(paren)
        else:
            if len(stack) == 0:
                is_balanced =False
            else:
                top = stack.pop()
                if  not is_match (top,paren):
                    is_balanced = False
        index += 1
    if len(stack) == 0 and is_balanced:
        return True
    else:
        return False

print is_paren_balanced("{)}")

