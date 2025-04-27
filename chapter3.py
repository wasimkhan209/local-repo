#  LIST :- A built-in data type that stores set of value

marks = [92.5, 96.3, 94.4, 99.99, 65, "W"]
print(marks)
print(type(marks))

print(len(marks))

print(marks[4])

marks.append("O")

print (marks)

marks.insert(2,98.5)

print(marks)

print(len(marks))

# sorting the list
str = ["w", "o", "A", "k" ,"r"]
str.sort()
print(str)

# Reverse of the List

str.sort(reverse=True)
print(str)
print(len(str))

# write a prog to input 3 movies name and print then as a list and also check their type

movies = [
    input("enter the 1st movies : "),
    input("enter the 2nd movies : "),
    input("enter the 3rd movies : "),
    input("enter the 4th movies : "),
    input("enter the 5th movies : ")
]
print(movies)
print(type(movies))

# write a prog of tuple to count the number of Grade A

list = ("D", "A", "C", "A", "E", "A", "F","A")
print(list.count("A"))


# write a prog to store the above vlaues in list and print the and return as type list

list = ["D", "A", "C", "A", "E", "A", "F","A"]
print(list)

# Type of List

print(type(list))

# Sorting the Above List

list.sort()
print(list)