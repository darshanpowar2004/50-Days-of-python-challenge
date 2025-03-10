# Set or List
import timeit
# Testing the speed of execution in a set
speed_test = '''
a = range(1000000)
b = list(a)
i = 999999
for i in b:
    print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))