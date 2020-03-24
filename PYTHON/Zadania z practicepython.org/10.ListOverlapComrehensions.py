'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'''
import random
a = random.sample(range(100), 5)
b = random.sample(range(100), 5)
c=[x*y for x in a for y in b]
print(c)
