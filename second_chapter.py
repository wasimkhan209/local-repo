# Methods of creating Strings
# name = "wasim"
# name = 'wasim'
# name = '''wasim'''
# print(name)

# Indexing
# print(name[0:3])
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# OR
# print(name[-5:len(name)])

str = "i am wasim khan and im studying BS computer science"
# print(str.capitalize())
str = str.capitalize()
print(str)
print(str.endswith("nce")) # True
print(str.endswith("eg")) #False

#  write a Prog that input four vlaues and find the Gretest one

a = float (input("Enter the First Number : "))
b = float (input("Enter the Second Number : "))
c = float (input("Enter the Third Number : "))
d = float (input("Enter the Fourth Number : "))
if(a >=b and a>= b and a >= c and a >= d):
    print("the first vlaue you have entered is the Greatest")
elif(b >=c and b >=d):
    print("The Second Value you have entered is Greatest")
elif(c >= d):
    print("Third Vlaue is Greatest ")
else:
    print("fourth Vlaue you have Entered is greatest")
