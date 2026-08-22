#never repeat yourself
#agr koi vhiz doo baar ho rhi hai toh uska function bna do
#functions are reusable code of block.
#function- random, elif, type, int, float, str, print, input, len, lower, upper, startswith, endswith
#it is set of statements

#have function declaration and function call and define the function

def hello():
    print("Hello, universe")
    print("how are you?")

hello() #calling or invoking function
hello() #reusability of function
hello() #reusability of function

def num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
num()  


def nums():
    a=3
    b=1
    c=a+b
    print(c)
nums()    


#passing parameters
def hello(name):
    print(f"hi how are you (name)")
    print("hi" + name)

    hello("ram")


def greet(a,b):
    return a+b
functionOutput = greet(2,3)