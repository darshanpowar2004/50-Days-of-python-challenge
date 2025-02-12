"""
To compare the two strings, first, we need to sort them. We use the
'sorted()' function to sort the two strings. Then we use the (==)
operator to compare the two strings.
"""

def equal_strings(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1== str2:
        return True
    else:
        return False

if __name__=="__main__":
    str1 = 'love'
    str2 = 'evol'
    print(equal_strings(str1,str2))

