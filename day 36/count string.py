# Day 36
# Count String

def count(s: str):
    count_dict = {}
    for i in s:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict

if __name__ == '__main__':
    s = 'hello'
    result = count(s)
    print(result)