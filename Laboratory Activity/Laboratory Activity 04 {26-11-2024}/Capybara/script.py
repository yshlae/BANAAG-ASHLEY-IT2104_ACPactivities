from Capybara import Capybara

capybara_1 = Capybara("Biscoff", "M", 5)

capybaras = [capybara_1]

test_case_number = int(input("Enter the test case number: "))

selected_capybara = capybaras[test_case_number - 1]

print(f"Test Case {test_case_number}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
