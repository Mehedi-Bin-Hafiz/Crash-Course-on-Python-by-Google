print(len('mehedi'*3))

def double_word(word):
    res = word *2

    return res+str(len(res))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0