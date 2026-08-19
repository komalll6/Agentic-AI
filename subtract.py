import random 
num1 = random.randint(1,10)
num2 = random.randint(1,10)

if num2>num1:
    num1, num2 = num2, num1

answer = int(input("What is " + str (num1) + " - " + str(num2) + " ? " ))

while num1 - num2 != answer:
    print("Incorrect answer. Please try again.")
    answer = int(input("What is " + str (num1) + " - " + str(num2) + " ? " ))
    print("Correct answer. Well done!")