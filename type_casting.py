#like float to int, int to float, str to int, str to float, int to str, float to str
#have specility to change the type of variable, like float to int, int to float, str to int, str to float, int to str, float to str
#not add in alphabets.

age = (input("enter your age: ")) #input function to take input from user, it will take input in string format
age = int(age) #type casting to convert string to integer
print(age) #output will be 22, it will remove the decimal part
print(age + 1) #output will be 23, it will add 1 to the age
print(type(age)) #output will be <class 'int'>  .

example_float = 3.14
example_int = int(example_float) #type casting to convert float to integer
print(example_int) #output will be 3, it will remove the decimal part

example_int = 10
example_float = float(example_int) #type casting to convert integer to float
print(example_float) #output will be 10.0, it will add the decimal part