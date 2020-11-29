#Functions

#Taking input in lowercase
name = input("Enter Name?").lower()

#Defining Two Functions
def advaith():
    print("Hello, Advaith");
def rohan():
    print("Hello, rohan");

#Checking the person's data
if name == "advaith":
    advaith()
elif name == "rohan":
    rohan()
else:
    print("Unknown person");