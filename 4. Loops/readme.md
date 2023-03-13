        Loops

------------------------------------

Loops are a fundamental concept in programming that allows you to repeat
a block of code until a certain condition is met. There are different
types of loops, but they all follow a similat pattern. a condition is 
checked and if it is true, the instructions inside the loop are executed.
Then the condition is checked again and if it is still true the instructions
are executed again. This continues until the condition is false, at which
point the loop stops.

Loops are especially useful when you need to perform a task multiple times,
such as processing large amounts of data or iterating over a list of items.

In Python, there are two main types of loops: For loops and While loops.

------------------------------------

For Loops: For loops allow you to iterate over a sequence of items, 
        such as a list, tuple or string and perform a block of code for
        each item in the sequence. For loops in Python are often used to
        iterate over a collection of data and perform some operations on
        each item. 

The general syntax for a for loop in Python is:
        
    for item in sequence:
        # code to be executed for each item.
    
Here's an example that uses a for loop to iterate over a list of numbers
and print each one:
        
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)

Output:

    1
    2
    3
    4
    5

------------------------------------

While Loops: While loops allow you to execute a block of code repeatedly as
long as a certain condition is ture. While loops are often used when you 
dont know exactly how many times you need to repeat a block of code.

The general syntax for a while loop in Python is:

    while condition:
        # code to be executed as long as condition is true

Heres an example that uses a while loop to print the numbers 1 to 5:

    num = 1
    while num <= 5:
        print(num)
        num += 1  # This is same as 'num = num + 1'

In this example, the while loop will continue to execute as long as the variable
'num' is less than or equal to 5. Inside the loop, we print the value of 'num'
and then increment it by 1 using '+=' operator. The loop will exit when 'num' is
incremented to 6 and the condition 'num <= 5' is no longer true.

