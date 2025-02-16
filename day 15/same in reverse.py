# Day 15
# Same In Reverse

def same_in_reverse(word : str):
    if word[::-1] == word:
        return "True, because it reads the same in reverse."
    else:
        return "False, because it reads the not same in reverse."


if __name__=='__main__':
    word = "cid"
    print(same_in_reverse(word))