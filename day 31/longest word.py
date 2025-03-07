# Day 31
# Longest Word

def longest_word(arr : list):
    long_word = []
    for i in range(len(arr)):
        if not long_word:
            long_word.append(len(arr[i]))
            long_word.append(arr[i])
        else:
            if long_word[0] < len(arr[i]):
                long_word[0],long_word[1] = len(arr[i]),arr[i]

    return long_word

if __name__ == '__main__':
    print(longest_word(['Java','JavaScript','Python']))
