# printing the hello world
print ("hello world")

# variables in python:- variables are name given to a memory location in a program 
# let practice some variable 

name = "wasim ullah khan"
age = 20
old = False
semester = 6
prog = "BS"
subject = "Computer Science"
uni = "Islamia College University Peshawar"

# now printing the above variables
print("name is :" , name)
print("Age is : ", age)
print("Current Semester :" , semester)
print("Program is :" , prog)
print("Subject is :" , subject)
print("University name is :" , uni)

# adding two vlaues in python

a = 16
b = 19
c = a+b
print ("the sum of a and b is :" , c)

# here d is use for just checking the None Type in python
d = None 

# print the types of the variables
print (type(name))
print (type(age))
print (type(semester))
print (type(prog))
print (type(subject))
print (type(uni))
print (type(c))
print (type(old))



# conditional statements
# if-elif-else strings
# example
color = input("light color : ")
if(color == "red"):
    print ("stop")
elif(color == "yellow"):
    print("Ready to Go")
elif(color == "Green"):
    print("Now you can Go")
else:
    print("you are fully not allowed to go becuse you are under 18")

# conditional statements entering the interger data type

ball = int(input("Enter the hiting of ball : "))
if(ball == 6):
    print("you are the 1st position")
elif(ball == 4):
    print("you are second position holder")
elif(ball == 2):
    print(" you aer the 3rd position holder")
else:
    print("oh! you lose the match")