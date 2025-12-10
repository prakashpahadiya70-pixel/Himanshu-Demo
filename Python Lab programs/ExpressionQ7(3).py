import re
text = input("Enter string: ")
pattern = r"\w+"
result = re.findall(pattern, text)
print("Words and Numbers:", result)