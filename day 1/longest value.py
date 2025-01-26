def longest_value(element : dict):
    long_value = max(element.keys())
    return f'longest value is {element[long_value]}'

if __name__ == '__main__':
    fruits = {'fruit': 'apple',
              'color': 'green'}
    print(longest_value(fruits))