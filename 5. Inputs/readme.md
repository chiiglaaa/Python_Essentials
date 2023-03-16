        Inputs

------------------------------------

In Programming, inputs are data or information provided to a program
or function in order to perform certain operations or calculations.
Inputs can come from a variety of sources, such as user input via
keyboard or mouse, files, network connections, or other programs.

The use of inputs in programming is to allow userts to provide 
information to a program or function, which then uses that information
to perform specific tasks or operations. Inputs are essential for 
making programs interactive and user-friendly, as they allo users to
provide specific instructions or data to the program.

In Python, you can read input from the user using 'input()' function.
The syntax for this function is:

    input(prompt)

------------------------------------

Here, the 'prompt' parameter is an optional string that is displayed 
to the user before the input is read. If the prompt is not specified,
the function will simply wait for the user to input something and 
press Enter.

------------------------------------

For example, to read a user's name and print it to the screen, you 
could use the following code:

    name = input("Enter you name: ")
    print("Your name is: ", name)

------------------------------------

For example if you want to get only integer value you can do this:

    number = int(input("Enter number: "))
    print("The number is: ")

In here number will be saved as integer and we can use it like a 
number. but if we remove 'int' it will be saved as string and if
we try to do something like this:

    number = int(input("Enter number: "))
    print(number * 3)

Now this will give us error.
You can always try to see what it does.

------------------------------------

When you run this code, it will display the prompt "Enter you name:"
on the screen, and wait for the user to input their name. Once the 
user presses Enter, the input is soted in the 'name' variable, and
then the program prints out the message "Your name is:" followed by
the value of the 'name' variable.

    Always validate user input to ensure that it is
    of the correct type and format before using it
    in your program.
------------------------------------
    Make sure to handle any exceptions that may occur
    when reading input from the user, enters invalid 
    data or the input stream is interrupted.
------------------------------------
    Make it clear what type of input is expected from
    user.





------------------------------------

I used "try:" and "except:" statements. They are used to catch and handle
exceptions. its a code block that allows our program to take alternative 
actions in case an error occurs.

------------------------------------

Example:

    while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter valid age.")

When we run this program it will ask us "Enter you age:" and if we wrote
something other than integer(number) it will give us "ValueError". so if
we want to make sure that user writes integer we used try and except 
statements. while running the program if there is any ValueError the 
program will stop next action in try statement and print whats in the 
except statement.

Output will be:

    Enter your age: hello
    Please enter valid age.
    Enter your age: 123abc
    Please enter valid age.
    Enter your age: 25

After writing integer the while loop will be stopped and the age variable
will be "25".
