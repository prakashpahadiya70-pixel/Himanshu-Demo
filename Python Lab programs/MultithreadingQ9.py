import threading
import re

def copy_file(src, dest):
    try:
        with open(src, "r") as f1, open(dest, "w") as f2:
            data = f1.read()
            f2.write(data)
        print(f"File copied from {src} to {dest}")
    except FileNotFoundError:
        print("Source file not found")

def count_file_details(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            lines = data.splitlines()
            line_count = len(lines)
            char_count = len(data.replace("\n",""))
            special_count = len(re.findall(r'[^a-zA-Z0-9\s]', data))

        print(f"\nResults for {filename}:")
        print("Lines          :", line_count)
        print("Characters     :", char_count)
        print("Special Symbols:", special_count)

    except FileNotFoundError:
        print("File not found to count")

# Taking filenames from user
file1 = input("Enter source filename: ")
file2 = input("Enter destination filename: ")

# Threads created
t1 = threading.Thread(target=copy_file, args=(file1, file2))
t2 = threading.Thread(target=count_file_details, args=(file1,))

# Starting threads
t1.start()
t2.start()

# Waiting for threads completion
t1.join()
t2.join()

print("\nAll Tasks Completed!")