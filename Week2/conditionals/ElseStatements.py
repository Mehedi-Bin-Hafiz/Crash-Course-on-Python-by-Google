def hint_username(username):
    if len(username)<3:
        print("invalid")
    else:
        print("valid")


"""The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?"""

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

# def is_positive(number):
#   if number > 0:
#     return True
#   return False

print(is_positive(5))



if __name__ == '__main__':
    print("I am current file")