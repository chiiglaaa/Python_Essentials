#Lets see use of for loop
#Example 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
    #This for loop will print all number in numbers variable.

#Example 2

for x in range(10):
    print(x)
    #This for loop will print numbers from 0 to 10.

#Example 3

for i in range(1, 11):
    print(i)
    #This for loop will print numbers from 1 to 10.

#Example 4

for i in range(0, 20, 2):
    print(i)
    #This for loop prints even numbers from 0 to 18(inclusive) in increments of 2.


#Lets see use of while loop
#Example 1

number = 0
while True:
    print(number)
    number += 1
    if number == 10:
        break

"""
This while loop creates an infinite loop that prints the value of the
variable "number" and increments it by 1 each iteration until the value
of "number" becomes 10, at which point the loop is terminated using the
"break" statement.
"""

#Example 2

num = 5
count = 1
while count <= 10:
    result = num * count
    print(num, "x", count, "=", result)
    count += 1

"""
This while loop prints multiplication table from 1 to 10 using a while loop.
It calculates the product of the number and the current count in each 
iteration and prints it in the format "number * count = result". It will
continue to run as long as the value of "count" is less than or equal to 10.
"""

#Try to mess with the code.
