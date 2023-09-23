def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

def main():
    input_string = input("Enter a string: ")
    reversed_str = reverse_string(input_string)
    print("Reversed string:", reversed_str)

main()

