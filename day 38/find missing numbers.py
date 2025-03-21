# Day 38
# Find Missing Numbers

def missing_numbers(l : list):
    missing_num = [x for x in range(l[0],l[-1]+1) if x not in l]
    print(missing_num)

if __name__ == "__main__":
    l = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
    missing_numbers(l)