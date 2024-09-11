def find_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_list = [char for char in input_string if char in vowels]
    return vowel_list
input_string = input("Enter a string: ")
vowels_in_string = find_vowels(input_string)
print(vowels_in_string)