def is_perfect_number(num):
    if num <= 0:
        return False
    
    divisors = [i for i in range(1, num) if num % i == 0]
    
    return sum(divisors) == num

def main():
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'exit':
            print("Exiting program.")
            break
        
        try:
            num = int(user_input)
            if is_perfect_number(num):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
