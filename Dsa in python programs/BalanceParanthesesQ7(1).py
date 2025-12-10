def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (ch == ')' and top != '(') or \
               (ch == ']' and top != '[') or \
               (ch == '}' and top != '{'):
                return False
    return len(stack) == 0

expr = "{(a+b) * (c+d)}"
print("Expression:", expr)

if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")