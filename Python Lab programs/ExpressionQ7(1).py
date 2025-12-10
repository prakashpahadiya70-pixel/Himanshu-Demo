import re
date = input("Enter date in YYYY-MM-DD format: ")
pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, date)
if match:
    print("Year :", match.group(1))
    print("Month:", match.group(2))
    print("Date :", match.group(3))
else:
    print("Invalid Date Format")