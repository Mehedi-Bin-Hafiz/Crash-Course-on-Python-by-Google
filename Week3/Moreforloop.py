def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

"""To quickly recap the range() function when passing one, two, or three parameters:

One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter."""