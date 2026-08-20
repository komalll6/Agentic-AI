#list, tuples, dictionaries, sets


#LIST
#list - ordered collection of item, which are mutable- chnageable, allows duplicate elements
#list are declare with []
list = [1,3,4,5] #ordered or mutable
print(list)
print(list[0]) #accessing first element
list[0] = 10 #changing first element
print(list)
print(type(list)) #checking the type of list, like integer, float, string, boolean, list, tuple, dictionary, set
print(len(list)) #checking the length of list //5


#TUPLES
#tuples- ordered but not mutable
#declare with () round bracles
#both list and tuples are ordered, but list is mutable and tuple is immutable
tuple = (1,2,3,4,5) #ordered or immutable
print(tuple)


#SETS
#sets- unordered, collection of unique elements
#declare with {} curly braces
sets= {1,2,3,4,5} #unordered or unique
print(sets)


#dictionaries
#dictionaries- unordered, collection of key-value pairs, like name , age and tell the value of name and age
dictionary = {
    "name":"John", 
    "age":30,
    "color": "fair"
            } #unordered or key-value pairs
print(dictionary)