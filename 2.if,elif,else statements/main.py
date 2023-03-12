x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
print()  # This will print an empty line.

if x > y:
    print("First number is greater than Second.")
elif x == y:
    print("First and Second numbers are equal.")
else:
    print("Second number is greater than First.")

print()  # This will print an empty line.
text = input("Enter text: ")

if text.islower():
    # '.islower()' is a Python built-in function which check if String is all lowercase letters.
    print("String contains only lowercase letters.")
elif text.isupper():
    # '.isupper()' is a same thing, but it checks if String is all uppercase letters.
    print("String contains only uppercase letters.")
else:
    print("String contains both upper and lowercase letters.")

#Try to mess with the code. change stuff to see what will happen.
