# Day 26
# Sort Words

def sort_words(a : str):
    a = a.replace(" ","")
    sort_list = []
    for txt in a:
        if txt not in sort_list:
            sort_list.append(txt)

    sort_list.sort()

    return [",".join(sort_list)]

if __name__ == '__main__':
    str1 = 'love life'
    print(sort_words(str1))