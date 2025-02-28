# Create a Nested List
import numpy as np

def nested_list(*args):
    return np.array(args)

if __name__ == '__main__':
    arr1 = [1, 2, 3, 5]
    arr2 = [1, 2, 3, 4]
    arr3 = [1, 3, 4, 5]
    output = nested_list(arr1,arr2,arr3)
    print(output)