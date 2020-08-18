cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
print(cool_beasts.items())
for keys,values in cool_beasts.items():
    print("{} have {}".format(keys,values))


"""An Interesting program"""

### count letter in a string

def letter_count(letter):
    result={}
    for l in letter:
        if l not in result:
            result[l] = 0
        result[l] += 1
    return result

print(letter_count('aaaaaaaaaaabbbbbbbbbcccccccccc'))

for key,value in letter_count('aaaaabbbbbdddbbbfbeerbbdsfs').items():
    print('number of {} is {}'.format(key,value))
