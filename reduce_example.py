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
def lambda_test(my_list):
    sum_numbers = lambda x, y : x + y 
    return reduce(sum_numbers, my_list)

if __name__ == "__main__":
    list_number = [47, 11, 42, 13]
    result = lambda_test(list_number)
    print(result)