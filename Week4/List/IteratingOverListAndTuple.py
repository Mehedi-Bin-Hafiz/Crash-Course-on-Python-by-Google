animal = ['cat','mat','sat']
chars = 0
for animal in animal:
    chars += len(animal)

print('Total characters', chars)

print("total characters : {} , average length : {} ".format(chars,chars/len(animal)))

whinners = ['mehedi', 'mahim', 'hasan']

# enumerate function returns tuple of each element of list . each tuple contains index and corresponding element
for index, person in enumerate(whinners):
    print("{} - {} ".format(index+1,person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([('mehedi@gmail.com','mehedi'),('mahim@gmail.com','mahim')]))


def skip_elements(elements):
    # code goes here
    ele=[]
    for index , element in enumerate(elements):
        if index %  2 == 0:
            ele.append(element)
    return ele


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

