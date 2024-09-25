chars = input("Enter two space-separated characters: ").split()

if len(chars) != 2:
    print("Please enter exactly two characters.")
else:
    char1, char2 = chars

    greater_char = max(char1, char2)

    print("---------------------------------------------------------")
    print(f"The character with greater value is: {greater_char}")
    print("---------------------------------------------------------")

    ascii_val1 = ord(char1)
    ascii_val2 = ord(char2)

    print("Showing ASCII Values: ")
    print(f"{char1} : {ascii_val1}")
    print(f"{char2} : {ascii_val2}")
