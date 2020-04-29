## This is for part 2 on lists

# count()
# sort() method
# sorted() function
# reverse()
# clear()
# copy()

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
fruits.sort()
print(fruits)

numbers = [1,5,8,5,1,2,3,5]
numbers.sort()
print(numbers)
numbers1 = numbers.copy()
print

numbers.clear()
print(numbers1)
print(numbers)


print(sorted(fruits))

## use == for checking value in two different lista
## use is for checking memory allocation in two lists
#split() method, this will convert strin gto list
user_info = "Anoop 37".split()
print(user_info)


user_info = "Anoop,37".split(",")
print(user_info)

name, age = input("enter your name and age ").split(",")
print(name)
print(age)




#join method
#convert list to string

user_info =["Anoop", "Sheoran"]
print(",".join(user_info))
