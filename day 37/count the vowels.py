# Day 37
# Count the Vowels

vowels = "aeiou"

def count_the_vowels(s : str):
    vowels_count  = []
    for i in s:
        if i in vowels:
            if i not in vowels_count:
                vowels_count.append(i)

    return len(vowels_count)

if __name__ == '__main__':
    s = "hello"
    print(count_the_vowels(s))

    s1 = "saas"
    print(count_the_vowels(s1))
