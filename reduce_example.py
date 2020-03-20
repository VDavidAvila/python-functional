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
sum_numbers = lambda x, y : x + y 
result = reduce(sum_numbers, [47, 11, 42, 13])
print(result)