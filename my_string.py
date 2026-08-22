user_input = input("Enter a string: ")

input = user_input.strip()
print(input)
print(input.lower()) # lower() is a method that converts a string to lowercase
print(input.upper()) # upper() is a method that converts a string to uppercase

text  = "py is powerful"
print(text.startswith("py")) # startswith() is a method that checks if a string starts with a specific substring
print(text.endswith("ful")) # endswith() is a method that checks if a string ends with a specific substring