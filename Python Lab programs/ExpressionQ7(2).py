import re
text = input("Enter string: ")
pattern = r"\b\d{3}\b"
result = re.findall(pattern, text)
print("3-Digit Numbers:", result)