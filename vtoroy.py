'''
program
'''
try:
    FIRST_INDEX = 1
    SECOND_INDEX = 3
    array = [[1,2,3],[4,5,6]]
    print(array[FIRST_INDEX][SECOND_INDEX])
except IndexError:
    print(array[FIRST_INDEX][SECOND_INDEX-1])
