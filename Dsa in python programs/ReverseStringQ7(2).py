def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)
    rev = ""
    while stack:
        rev += stack.pop()
    return rev

s = "hello"
print("Original:", s)
print("Reversed:", reverse_string(s))