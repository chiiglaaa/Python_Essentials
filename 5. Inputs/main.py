#Lets see how to get information with input about a user.

name = input("Please enter you name: ")
print(name)

"""
For example we wrote "Jack" as name.
it will be same as if we wrote
    name = "Jack"
Output will be whatever we wrote in
"""


#Now lets see how to get integer as input
"""
To make sure that if user enter integer in age input
We can use while loop to check that user really wrote number.
"""

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter valid age.")

"""
We can make it little bit more complicated.
for example to check if the number is positive
an not negative or zero.
and many other stuff.
"""



"""
We can ask user to input number and save it as string
but we can transform it as integer like that.
"""

age = input("Enter age: ")
age = int(age)
#If we wrote something other than number it will give us ValueError.

#Try to mess with the code and explore new stuff.
