def is_palindrome(input_string):
        input_string=input_string.lower().split()
        new_string = ""
        reverse_string=''
        for word in input_string:
               new_string += word
        reverse_string=list(new_string)
        reverse_string = "".join(reverse_string[::-1])
        if reverse_string == new_string:
            return True
        else:
            return False



print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


weather = 'Rainfall'
print(weather[:4])


def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."