""" The data inside dictionaries take the form of pairs of keys and values"""
x = {}
print(type(x))

file_count = {'jpg':10,'txt':14, 'csv':2, 'py':21}
print(file_count)
print(file_count["txt"])

print('jpg' in file_count)
print('html' in file_count)
file_count['cfg']=12
print(file_count)
file_count['cfg']=145
print(file_count)

#delete element from dictionary

del file_count['cfg']
print(file_count)
