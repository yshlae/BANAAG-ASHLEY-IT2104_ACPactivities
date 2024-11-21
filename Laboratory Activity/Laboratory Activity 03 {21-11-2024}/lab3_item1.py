def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    roman = roman.upper()
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        if char not in roman_values:
            return f"Invalid Roman numeral: {roman}"
        
        current_value = roman_values[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total
    
def main():
    while True:
        roman = input("Enter a Roman numeral: ")
        if roman.lower() == 'exit':
            print("Exiting program.")
            break
        
        result = roman_to_integer(roman)
        print(f"The integer value of '{roman}' is: {result}")

if __name__ == "__main__":
    main()