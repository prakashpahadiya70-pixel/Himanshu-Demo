import re
text = input("Enter string: ")
pattern = r"\b[aeiouAEIOU]\w*\b"
result = re.findall(pattern, text)
print("Words starting with vowel:", result)