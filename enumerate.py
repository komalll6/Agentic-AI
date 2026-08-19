#automatic counter add krta hai 
#work like loop
#work with => searching, sorting etc.

list = [1,2,3,4,5,6,7]
for index, item in enumerate (list, start = 0):
    print(item)


list = [1,2,3,4,5,6,7]
for index, item in enumerate (list):
    print(item)


#break and continue statement
#BREAK- exit the loop
#CONTINUE- skips the current iteration and moves to the next one

a = 1
while a <= 100:
    if a == 50:
        break  #BREAK- exit the loop
    print(a)
    a += 1


a = 1
while a <= 100:
    if a == 50:
        continue
    print(a)
    a += 1