message = 'I am mehedi'
# message[4]='h' #TypeError: 'str' object does not support item assignment
print(message.index('I'))
print(message.index('mehedi')) #index of substring.

#Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious"
word = "supercalifragilisticexpialidocious"
print(word.index('x'))

# print(message.index('cat')) #ValueError: substring not found it produce error.
# so how can we check substring in message

print('cat' in message) # if it produce false then there is no substring

'''If we aren't sure what the index of our typo is, we can use the string method index to locate it and return the index. Let's imagine we have the string "lions tigers and bears" in the variable animals. We can locate the index that contains the letter g using animals.index("g"), which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins. animals.index("bears") would return 17, since that’s the start of the substring. If there’s more than one match for a substring, the index method will return the first match. If we try to locate a substring that doesn't exist in the string, we’ll receive a ValueError explaining that the substring was not found.'''