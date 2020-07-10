for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]" , end=' ')
        # if we want to print to write something else instead of the newline character, we use the end parameter.
    print()



def is_valid(user):
    if len(user)>=3:
        return True
    else:
        return False

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")
      break

validate_users(["purplecat"])


"""range() generates a sequence of integer numbers. It can take one, two, or three parameters:

range(n): 0, 1, 2, ... n-1
range(x,y): x, x+1, x+2, ... y-1
range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)"""

def multiples(n):
    if n == 0 :
        return 0
    elif (n % 7) == 0:
        return n
    else:
        return
for i in range(0,101):
    if multiples(i) != None:
        print(multiples(i))