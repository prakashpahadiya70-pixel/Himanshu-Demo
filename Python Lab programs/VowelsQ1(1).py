string = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = c_count = b_count = 0

for ch in string:
    if ch in vowels:
        v_count += 1
    elif ch == " ":
        b_count += 1
    elif ch.isalpha():
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Blanks:", b_count)

