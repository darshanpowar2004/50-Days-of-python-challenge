# Day 28
# Return Index

def index_position(s : str):
    lower_index = []
    for i in range(len(s)):
        if s[i].islower():
            lower_index.append(i)
    return lower_index

if __name__ == '__main__':
    s = 'LovE'
    print(index_position(s))