# Day 41
# Only Words with Vowels
vowels = "aeiou"
def words_with_vowels(a):
    words = a.split(" ")
    output = []
    for i in words:
        if i not in output:
            for x in vowels:
                if x in i:
                    output.append(i)
                    break


    return output

if __name__ == '__main__':
    result = words_with_vowels("You have no rhythm")
    print(result)