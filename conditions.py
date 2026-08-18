#if else condition
#if - true
#else- not true
#also known as blocks (set of instructions)
age = 20
if age >= 18: #just simply write colon and enter - indedntaiton. make block with the help of indentation
    print("You are an adult.")
else:
    print("You are not an adult.")

#if under if condition are- nested 
#multiple if else conditions are- elif


#loops- repitatly/ multiple times execute the same block of code
example_variable = 0
while example_variable < 10:
    print(example_variable)
    example_variable += 1

a = 0
while a <= 10: #while loop- jb hume pta ho loop chlna kitni baar
    print(a)
    a = a + 1


#game like guess the number- user will guess the number, if user guess the number correctly then it will print "you guessed it correctly", otherwise it will print "try again"