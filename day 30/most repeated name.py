# Day 30
# Most Repeated Name

from collections import Counter

def repeated_name(names):
    if not names:
        return None

    counter = Counter(names)
    most_repeated_name = counter.most_common(1)[0]
    return f"The most repeated name is '{most_repeated_name[0]}' is repeated {most_repeated_name[1]} times."

if __name__ == '__main__':
    name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    print(repeated_name(name))