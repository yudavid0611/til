# List comprehension

>**references**
>- https://www.geeksforgeeks.org/python-list-comprehension/
>- https://dojang.io/mod/page/view.php?id=2285
>- https://www.w3schools.com/python/python_lists_comprehension.asp

<br/>

- **What is a list comprehension?**
    - Making a new list from an already created list with using *for* loop.
    - It is charming from efficiency point of view.

<br/>

- **Syntax**
    - *new_list = [expression(element) for element in created_list]*

<br/>

- **examples**
``` python
## example 1
temp_list = [1, 2, 3, 4]

# square each element in temp_list and put it in the new_list
new_list = [i ** 2 for i in temp_list] 

print(new_list)

# output
'''
[1, 4, 9, 16]
'''

########################################
## example 2: with if statement
temp_list = [1, 2, 3, 4]

# add elements to the new_list only if they are multiple of 2.
new_list = [i ** 2 for i in temp_list if i % 2 == 0]

print(new_list)

# output
'''
[4, 16]
'''

########################################
## example 3: two for loop
new_list = [(i, j) for i in range(1,5) for j in range(5, 10)]
print(new_list)

# output
'''
[(1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9)]
'''
```