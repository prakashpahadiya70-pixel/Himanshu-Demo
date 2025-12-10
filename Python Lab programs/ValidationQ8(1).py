import re
ip = input("Enter IP Address: ")
pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.)){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
if re.match(pattern, ip):
    print("Valid IP Address")
else:
    print("Invalid IP Address")