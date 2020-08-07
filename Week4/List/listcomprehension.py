multiples = []
for x in range(1, 11):
    multiples.append(x*7)

print(multiples)

multiples = [ x*7 for x in range(1,11)]
print(multiples)

languages =  [ 'python ', 'perl', 'ruby']

lenghts = [len(language) for language in languages]
print(lenghts)

z = [ x for x in range(0,101) if x % 3 == 0]
print(z)
