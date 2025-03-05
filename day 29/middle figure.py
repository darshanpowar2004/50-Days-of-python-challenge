# Day 29
# Middle Figure

def middle_figure(a:str,b:str):
    ab = a.replace(" ","") + b.replace(" ","")
    if len(ab) % 2 != 0:
        mid_index = (len(ab) // 2)
        return ab[mid_index]
    else:
        return 'No Middle Figure'

if __name__ == '__main__':
    # a,b = "make love","not wars"
    a = "hello"
    b = "world"

    print(middle_figure(a,b))
