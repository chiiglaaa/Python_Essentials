        Variables

------------------------------------

What is variable?

    A variable in programming is a named container that holds a value or a reference to a value.
    It allows programmers to store and manipulate data in their programs.
    Variables can hold various types of data, such as numbers,text,Boolean values and more complex data structures.

Whats the use of variables?

    For example if you are writing a program that needs to calculate the area of a rectangle, you can create variables
    to store the length and width of the rectangle. Then, you can use those variables in a formula to calculate the area.
    
    Variables also make code easier to read and understand. By giving names to the data being stored, variables can
    make it clear what the purpose of the data is and how it's being used.This can make it easier for other programmers
    to understand and modify the code in the future.

What type of data i can store in variables?

    In variables we can store: String, Integer, Float, Boolean, Array, Object etc.
    
    String example:
    
        this is string --> "Hello", "Have a great day.", "I have 100 dollars.".
    
    Remember!!
    
    If variable is in quotation marks or double quotation marks it does not matter if it contains
    number or boolean or anything it will be still a String.
    
    Integer example:
    
        this is integer --> 1, 99, 592, 10557 etc.
    
    Remember!!
    
    If variable does not have quotation marks or double quotation marks and it contains only numbers it is Integer.
    
    Float example:
    
        this is float --> 1.0, 5.5, 99.99, 1152.79 etc.

    Boolean example:
    
        this is boolean --> True, False.
    
    Boolean can be only two things. True or False.
    
    Remember!!
    
    If you want to store boolean you have to start writing with capital letter.
    For example:
    
        this is not a boolean --> false, FALSE, FAlse, true, TRUE, trUe etc.
        so you have to write like this --> True, False.

------------------------------------

How to make new variable?

For example i want to make a new variable and call it "x" and the value will be 5.
so we have to write like this:

    x=5
or
     x = 5

If we print x. output will be 5.

    print(x)

Output:

    5

------------------------------------

how to know the type of variable?

So if we have a variable and we dont know its type, we can use type() function:

    x = 9.9
    
    print(type(x))

Output:

    float

------------------------------------

We can use variables in math.
for example i have two really big numbers and i need sum of that two numbers:

    x = 9954223617
    y = 66321114755
    print(x + y) #We are using '+' operator which will return the sum of this numbers.

Output:

    76275338372

We have other operators too: '+', '-', '*', '/', '**', '%'.

    + operator performs addition between given values.
    - operator performs substraction between given values.
    * operator performs multiplication between given values.
    / operator performes division between given values.
    ** operator performs exponentation, raising a number to a power.
    % operator performs modulus division, returning the remainder of a division operator.

