# def format_address(address_string):
#     # Declare variables
#     lis=address_string.split(" ")
#     # Separate the address string into parts
#     number = lis[0]
#     lis.remove(lis[0])
#     lis = " ".join(lis)
#
#     return "house number {} on street named {}".format(number,lis)
#
#
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


print("question 2")
def highlight_word(sentence, word):
    lis = sentence.split(" ")
    lis = lis.insert(lis.index(word),word.upper())
    return lis






print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud !", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


print(" 7")

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    ___
    # Add or increment the value in the dictionary
    ___
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}