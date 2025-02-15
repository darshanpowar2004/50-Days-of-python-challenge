# Day 14

class Approach_1:
    def flat_list(arr : list):
        new_list = []
        for i in arr[0]:
            new_list.append(i)
        return new_list

class Approach_2:
    def flat_list(arr : list):
        them = arr[0]
        arr.pop()
        for i in range(len(them)):
            arr.append(them[i])


if __name__=='__main__':
    arr = [[2,4,5,6]]
    print(Approach_1.flat_list(arr))
    
    Approach_2.flat_list(arr)
    print(f"Modifing original list",arr)

