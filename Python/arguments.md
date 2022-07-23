# Arguments

>References
>- https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29

<br/>

## Contents
- **What is an argument?**
    - An value(or values) is used when we call a function.
    - Types of arguments
        1. Positional argument: passed through a function by its position.
        2. Keyword argument: passed through a function by being mapped with a parameter.
            - *positional argument should be placed before keyword argument*
        3. Mandatory argument: must be used when calling a function. 
        4. Optional argument: not necessarily needed when calling a function.
        5. Arbitrary positional argument: used when the number of positional arguments is not fixed.
        6. Arbitrary keyword argument: used when the number of keyword arguments is not fixed.

<br/><br/>

- **examples**
    1. Positional argument, Mandatory argument
    ``` python
    def add(x, y):
        return x + y
    add(2, 3)
    # -> x = 2, y =3
    # 2 and 3 are Mandatory arguments.
    ```
    
    2. Keyword argument
    ```python
    def add(x, y):
        return x + y
    add(y=2, x=3)
    # -> x = 3, y =2
    ```
    3. ~~Mandatory argument: refer to the first example.~~
    4. Optional arguments
    ```python
    def add(x, y=0):
        return x + y
    add(2, 3)
    # -> x = 2, y =3
    # 2 is mandatory, and 3 is optional.
    ```
    5. Arbitrary positional argument
    ```python
    def add(*args):
        result = 0
        for i in args:
            result += i
        return result
    add(1, 2, 3, 4, 5)
    # output: 15
    # arguments are wrapped up in a tuple
    ```
    6. Arbitrary keyword argument
    ```python
    def family(**kwargs):
        for k, v in family:
            print(k, v)
    family(father='john', mother='kate', sister='joy')
    # output
    '''
    father john
    mother kate
    sister joy
    '''
    # arguments are wrapped up in a dictionary
    ```