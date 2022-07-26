# Set
## Methods
- **set.copy()**: returns a shallow copy of the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set_copy = temp_set.copy()
  print(temp_set_copy) # {1, 2, 3}
  ```
- **set.add(*x*)**: adds x to the set if x is not in the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set.add(4)
  print(temp_set) # {1, 2, 3, 4}

  temp_set = {1, 2, 3}
  temp_set.add(3)
  print(temp_set) # {1, 2, 3}
  ```
- **set.pop()**: returns an element randomly and removes it.
  ``` python
  temp_set = {1, 2, 3}
  popped = temp_set.pop()
  print(f'temp_set: {temp_set}  popped: {popped}') # temp_set: {2, 3}  popped: 1

  temp_set = set()
  popped = temp_set.pop() # 'pop from an empty set'
  ```
- **set.remove(*x*)**: removes x from the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set.remove(3)
  print(temp_set) # {1, 2}

  temp_set = {1, 2, 3}
  temp_set.remove(4) # KeyError: 4
  ```
- **set.discard(*x*)**: removes x from the set. It does not raise an error though x is not in the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set.discard(3)
  print(temp_set) # {1, 2}

  temp_set = {1, 2, 3}
  temp_set.discard(4) # no error
  print(temp_set) # {1, 2, 3}
  ```
- **set.update(*t*)**: adds elements of the set 't' to the set if they are not in the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set2 = set([3, 4, 5])
  temp_set.update(temp_set2)
  print(temp_set) # {1, 2, 3, 4, 5}
  ```
- **set.clear()**: deletes all the elements in the set.
  ``` python
  temp_set = {1, 2, 3}
  temp_set.clear()
  print(temp_set) # set()
  ```
- **set.isdisjoint(*t*)**: checks whether there is an element that is included in both of sets or not.
  ``` python
  temp_set = {1, 2, 3}
  temp_set2 = {1, 4, 5}
  print(temp_set.isdisjoint(temp_set2)) # False

  temp_set = {1, 2, 3}
  temp_set2 = {4, 5}
  print(temp_set.isdisjoint(temp_set2)) # True
  ```
- **set.issubset(*t*)**: checks whether the set is a subset of set 't' or not.
  ``` python
  temp_set = {1, 2, 3}
  temp_set2 = {1, 2, 3, 4, 5}
  print(temp_set.issubset(temp_set2)) # True
  ```
- **set.issuperset(*t*)**: checks whether the set is a superset of set 't' or not.
  ``` python
  temp_set = {1, 2, 3, 4, 5}
  temp_set2 = {1, 2, 3, 4}
  print(temp_set.issuperset(temp_set2)) # True
  ```