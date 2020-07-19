#string indexing

name = 'mehedi'
print(name[0])
print(name[-1]) #last char

def first_and_last(message):
    if message == '':
        return True
    elif message[0] == message[-1]:
        return True

    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


#slice of strings

color = 'orange'
print(color[1:4])

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])