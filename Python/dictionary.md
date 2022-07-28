# Dictionary

## Methods
- **dict.copy()**: returns a shallow copy of the dictionary.
  ``` python
  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict2 = temp_dict.copy()
  print(temp_dict == temp_dict2) # True
  print(temp_dict is temp_dict2) # False
  ```
- **dict.items()**: returns an object that displays a list, which contains key-value tuple pairs of the dictionary.
  ``` python
  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  result = temp_dict.items()
  print(result) # dict_items([('a', 1), ('b', 2), ('c', 3)])
  ```
- **dict.get(*x, y*)**: returns a value that matches x(key). If x is not in the dictionary, it returns None or y.
  ``` python
  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  result = temp_dict.get('a')
  print(result) # 1

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  result = temp_dict.get('d')
  print(result) # None

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  result = temp_dict.get('d', -1)
  print(result) # -1
  ```
- **dict.pop(*x, y*)**: deletes a pair of key-value that the key is x. If x is not in the dictionary as a key, it raises an exception or returns y.
  ``` python
  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict.pop('a')
  print(temp_dict) # {'b': 2, 'c': 3}

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict.pop('d') # KeyError: 'd'

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict.pop('d', -1) # -1
  ```
- **dict.update(*[object]*)**: updates the dictionary with a new dictionary or an iterable object that has pairs of key-value.
  ``` python
  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict2 = {'d': 4}
  temp_dict.update(temp_dict2)
  print(temp_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict2 = {'c': 4}
  temp_dict.update(temp_dict2)
  print(temp_dict) # {'a': 1, 'b': 2, 'c': 4}

  temp_dict = {'a': 1, 'b': 2, 'c': 3}
  temp_dict2 = [['d', 4], ['e', 5]]
  temp_dict.update(temp_dict2)
  print(temp_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
  ```