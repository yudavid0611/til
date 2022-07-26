# List
## Methods
- **list.remove(*x*)**: removes an element that matches x.
  ``` python
  temp_list = [1, 2, 3]
  temp_list.remove(2)
  print(temp_list) # [1, 3]

  temp_list = [1, 1, 2, 3]
  temp_list.remove(1)
  print(temp_list) # [1, 2, 3]

  temp_list = [1, 1, 2, 3]
  temp_list.remove(4) # list.remove(x): x not in list
  ```
- **list.pop(*i*)**: returns an element and removes it from the list.
  ``` python
  temp_list = [1, 2, 3]
  popped = temp_list.pop()
  print(f'temp_list: {temp_list}  popped: {popped}') # temp_list: [1, 2]  popped: 3

  temp_list = [1, 2, 3]
  popped = temp_list.pop(0)
  print(f'temp_list: {temp_list}  popped: {popped}') # temp_list: [2, 3]  popped: 1
  ```
- **list.index(*x, start, end*)**: returns the index of x when x is in the list. *start* and *end* parameters are used when you want to set a specific searching area.
  ``` python
  temp_list = ['a', 'b', 'c']
  target = temp_list.index('b')
  print(target) # 1

  temp_list = ['a', 'b', 'c']
  target = temp_list.index('c', 1, 2)
  print(target) # 'c' is not in list

  temp_list = ['a', 'b', 'c']
  target = temp_list.index('c', 1, 3)
  print(target) # 2
  ```
- **list.reverse()**: reverses the elements of the list.
  ``` python
  temp_list = ['a', 'b', 'c']
  temp_list.reverse()
  print(temp_list) # ['c', 'b', 'a']
  ```
- **list.sort()**: sorts the elements of the list.
  ``` python
  temp_list = ['z', 'w', 'a']
  temp_list.sort() # default: reverse=False
  print(temp_list) # ['a', 'w', 'z']

  temp_list = ['z', 'w', 'a']
  temp_list.sort(reverse=True)
  print(temp_list) # ['z', 'w', 'a']
  ```
- **list.insert(*i, x*)**: inserts an element to the list. You can set the location where x is inserted.
  ``` python
  temp_list = ['a', 'b', 'c']
  temp_list.insert(1, 'z')
  print(temp_list) # ['a', 'z', 'b', 'c']
  ```