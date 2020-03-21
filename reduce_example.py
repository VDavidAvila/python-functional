from functools import reduce 
"""
list of numbers 
|-------------------|          
| 47 | 11 | 42 | 13 |
|-------------------|

47 + 11 = 58
|--------------|
| 58 | 42 | 13 |
|--------------|

58 + 42 = 100
|----------|
| 100 | 13 |
|----------|

100 + 13 = 113 result final 
"""
def lambda_test(functions,my_list):
    return reduce(functions, my_list)


""" Determining the maximum of a list of numerical values """
def maximum_number(numbers):
    f = lambda x, y: x if (x > y) else y
    return reduce(f, numbers)

if __name__ == "__main__":
    sum_numbers = lambda x, y : x + y 
    list_number = [47, 11, 42, 13]
    result = lambda_test(sum_numbers,list_number)
    print(result)
    
    print(maximum_number(list_number))