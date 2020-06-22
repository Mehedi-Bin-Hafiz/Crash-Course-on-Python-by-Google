print("Yellow" > " Cyan" and "Brown" > "Magenta")

"""Here we're comparing strings, and the bigger and smaller operators refer to alphabetical order. Yellow comes after cyan, but brown doesn't come after magenta. So this means that the first statement is true, but the second one isn't, which makes the result of the whole expression false."""

print("Yellow" > " Cyan" or "Brown" > "Magenta")

print(not "Yellow" > " Cyan" or "Brown" > "Magenta") # not can invert the boolean


"""In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False. 

To check if two values are the same, we can use the equality operator: == 
To check if two values are not the same, we can use the not equals operator: != 
We can also check if values are greater than or lesser than each other using > and <. If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError. """