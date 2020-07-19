def student_grade(name, grade):
    res="{} received {}% on the exam".format(name, grade)
    return res

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""


'''In these two expressions we're using the greater than operator to align text to the right so that the output is neatly aligned. In the first expression we're saying we want the numbers to be aligned to the right for a total of three spaces. In the second expression we're saying we want the number to always have exactly two decimal places and we want to align it to the right at six spaces.'''