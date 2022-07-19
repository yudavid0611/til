# lambda and etc.

## Introduction
- introduct the lambda function and other functions that are related to the lambda function.
- other functions: map, reduce, filter

<br/>

## Contents
- **lambda**
  - It is a function that executes the expression on the arguments.
  - Syntax: lambda arguments : expression
  - example
  ``` python
  temp_fn = (lambda x : x**2)
  for i in range(5):
    print(temp_fn(i))
  
  # output
  '''
  0
  1
  4
  9
  16
  '''
  ```

<br/>

- **map**
  - It is a function that applies the given function to the iterable object(list, tuple, etc) and makes a map object with the result.
  - Syntax: map(function, iterable object)
  - example
  ``` python
  temp_fn = (lambda x : x**2)
  temp_list = [1, 2, 3, 4]
  print(list(map(temp_fn, temp_list)))

  # output
  '''
  [1, 4, 9, 16]
  '''
  ```

<br/>

- **reduce**
  - It is a function that applies the given function to all of elements of the given iterable object and outputs a cumulative result of this this process.
  - This fucntion is defined in the *functools* module.
  - Syntax: reduce(function, iterable object)
  ``` python
  from functools import reduce
  temp_fn = (lambda x, y : x * y)
  temp_list = [1, 2, 3, 4]
  print(reduce(temp_fn, temp_list))

  # output
  '''
  24
  '''
  ```

<br/>

- **filter**
  - It is a fucntion that filters the elements of the iterable object through the given function and returns a filter object.
  - The given function tests whether the each element is accepted or not.
  - Syntax: filter(function, iterable object)
  - example
  ``` python
  temp_fn = (lambda x : x > 10)
  temp_list = [1, 5, 11, 15]
  print(list(filter(temp_fn, temp_list)))

  # output
  '''
  [11, 15]
  '''
  ```