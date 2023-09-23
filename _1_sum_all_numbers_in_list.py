def summation(numbers):
    totalsum = sum(numbers)
    return " + ".join(map(str, numbers)) + " = " + str(totalsum)

def main():
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        user_numbers = [int(num) for num in input_str.split()]
        result = summation(user_numbers)
        print("User list is",user_numbers)
        print("Summation:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")


main()
