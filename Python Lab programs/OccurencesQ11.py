def count_letters(filename):
    try:
        with open(filename, "r") as file:
            data = file.read().lower()
            letter_count = {}
            for ch in data:
                if ch.isalpha():
                    letter_count[ch] = letter_count.get(ch, 0) + 1
            print("\nLetter Occurrences:")
            for letter, count in sorted(letter_count.items()):
                print(f"{letter} : {count}")
    except FileNotFoundError:
        print("File not found!")
filename = input("Enter filename: ")
count_letters(filename)