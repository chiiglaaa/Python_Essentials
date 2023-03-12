        if,elif,else statements

------------------------------------

In programming, a statement is a single instruction that the computer can execute.
It is a unit of code that performs a specific task. In Python, there are several
types of statements, including assigments statements, conditional statements, 
loop statements, and function calls.

The most commonly used conditional statements in Python are 'if', 'elif', 'else'
statements.

Today we will cover conditional statements.

------------------------------------

'if' statements are used to execute a block of code if a certain condition is true.
The syntax for an 'if' statement in Python looks like this:

    if condition:
        statement(s)

Here, 'condition' is a Boolean expression that evaluates to their 'True' or 'False'.
If 'condition' is True, the 'statement(s)' block will be executed. If 'condition'
is False, the 'statement(s)' block will be skipped.

Example:

    x = 5
    if x > 0:
        print('x is positive')

------------------------------------

'elif' statements are used to check for additional conditions if the previous 'if'
or 'elif' statements are false. The syntax for an 'elif' statement in Python looks
like this:

    if condition1:
        statement(s1)
    elif condition2:
        statement(s2) 
    elif condition3:
        statement(s1)
    else:
        statement(s3)

Here, 'condition1' is the first condition to be evaluated. If it is false, then
'condition2' is evaluated. If 'condition2' is true, the 'statement(s2)' block
associated with the 'elif' statements is executed. If its False, then it will do
same on 'condition3'. If its FALSE, then 'else' statement block will be executed.

Example:

    x = 0
    if x > 0:
        print('x is positive')
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")

------------------------------------

'else' statements are used to specify what should happen if none of the previous
'if' or 'elif' statements are true. The syntax for an 'esle' statement in Python
is:

    if condition:
        statement(s1)
    else:
        statement(s2)

Here, if condition is False it execute the 'statement(s2)' block, which is 
associated with the 'else' statement.

------------------------------------

Example:

    x = -5
    if x > 0:
        print("x is positive")
    else:
        print('x is negative')

------------------------------------

In summary, 'if', 'elif' and 'else' statements are conditional statements that
allow you to execute different blocks of code depending on whether a certain 
condition is true or false. They are powerful tools that enable you to create 
more complex and better programs.

------------------------------------

#Try to make a program that will have two or more integer variables. And use
#Conditional statements to print larger number.

#Try to make a program that will tell you if the number is Even or Odd. Also
#Use conditional statements to implement the logic.

------------------------------------
