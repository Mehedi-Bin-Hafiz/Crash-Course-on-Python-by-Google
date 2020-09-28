filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
check=[]
for i in filenames:
    check.append(i.split('.'))
second = []
for j in check:
    if j[1] == 'hpp':
        j[1] = 'h'
    second.append('.'.join(j))

print(second)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
    say = ""
    # Separate the text into words

    words = [x for x in ''.split(text)]
    # for word in words:
    #     # Create the pig latin word and add it to the list
    #
    #     # Turn the list back into a phrase
    return words


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"