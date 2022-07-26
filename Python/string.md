# String
## Methods
- **string.find(x)**: returns the first index of x in the string.
  ``` python
  print('apple'.find('p')) # 1
  print('apple'.find('j')) # -1
  ```
- **string.index(x)**: returns the first index of x in the string. If x is not in the string, it rases an exception.
  ``` python
  print('apple'.index('p')) # 1
  print('apple'.index('j')) # ValueError: substring not found
  ```
- **string.isalpha()**: checks whether characters in the string are alphabets or not.
  ``` python
  print('abc'.isalpha()) # True
  
  a = 1
  print(a.isalpha()) # 'int' object has no attribute 'isalpha'
  ```
- **string.isupper()**: checks whether characters in the string are in uppercase or not.
  ``` python
  print('AB'.isupper()) # True
  print('Ab'.isupper()) # False
  ```
- **string.islower()**: checks whether characters in the string are in lowercase or not.
  ``` python
  print('ab'.islower()) # True
  print('aB'.islower()) # False
  ```
- **string.istitle()**: checks whether each word in the string starts with an upper case letter or not. And it also considers other letters except for the first letter of each word are in lowercase.
  ``` python
  print('Title Title'.istitle()) # True
  print('TitlE TitlE'.istitle()) # False
  print('Title title'.istitle()) # False
  ```
- **string.replace(*old, new[,count]*)**: replaces old characters with new characters. The optional parameter 'count' restricts the numbers of replacements. 
  ``` python
  text = 'let the lady leave'
  print(text.replace('l', '!')) # !et the !ady !eave
  print(text.replace('l', '!', 2)) # !et the !ady leave
  ```
- **string.strip(*[chars]*)**: removes specific characters or spaces in the string.
  ``` python
  text = '    abc    '
  print(text)
  print(text.strip())
  print(text.lstrip())
  print(text.rstrip())
  '''
      abc    
  abc
  abc    
      abc
  '''

  text = ',,,,abc,,,,,,'
  print(text)
  print(text.strip(','))
  print(text.lstrip(','))
  print(text.rstrip(','))
    '''
  ,,,,abc,,,,,,
  abc
  abc,,,,,,
  ,,,,abc
  '''
  ```
- **string.split(*sep=None*)**: splits characters by space or a specific character value for the 'sep' parameter.
  ``` python
  text = 'aa.bb.cc.dd'
  print(text)
  print(text.split())
  print(text.split('.'))
  print(text.split(sep = '.'))
  # output
  '''
  aa.bb.cc.dd
  ['aa.bb.cc.dd']
  ['aa', 'bb', 'cc', 'dd']
  ['aa', 'bb', 'cc', 'dd']
  '''

  text = 'aa bb cc dd'
  print(text)
  print(text.split())
  print(text.split(' '))
  print(text.split(sep = ' '))
  # output
  '''
  aa bb cc dd
  ['aa', 'bb', 'cc', 'dd']
  ['aa', 'bb', 'cc', 'dd']
  ['aa', 'bb', 'cc', 'dd']
  '''
  ```
- **'*seperator*'.join(*iterable*)**: joins all elements in the given iterable object with using the separator.
  ``` python
  print('.'.join('I love you')) # 'I. .l.o.v.e. .y.o.u'
  print('.'.join(['I', 'love', 'you'])) # 'I.love.you'
  ```
- **string.title()**: changes every first letter of each word in the string into uppercase letter.
  ``` python
  text = 'let the lady leave'
  print(text.title()) # Let The Lady Leave
  ```
- **string.capitalize()**: changes the first letter in the string into uppercase letter.
  ``` python
  text = 'let the lady leave'
  print(text.capitalize()) # Let the lady leave
  ```
- **string.upper()**: makes all of the characters in the string uppercase letters.
  ``` python
  text = 'let the lady leave'
  print(text.upper()) # LET THE LADY LEAVE
  ```
- **string.lower()**: makes all of the characters in the string lowercase letters.  
  ``` python
  text = 'LET THE LADY LEAVE'
  print(text.lower()) # let the lady leave
  ```
- **string.swapcase()**: changes lowercase letters to uppercase letters, uppercase letters to lowercase letters.
  ``` python
  text = 'LET the LADY leave'
  print(text.swapcase()) # let THE lady LEAVE
  ```