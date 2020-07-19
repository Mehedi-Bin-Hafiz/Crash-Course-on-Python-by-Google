m = list('mehedi')

print(type(m))

print('m' in m)


def get_word(sentence, n):
    # Only proceed if n is positive
    m=n
    if n > 0:
        words = sentence.split()
        print(words)
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[m-1])
    return ("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

