```python
introduction to tuple datatype :
```


```python
Defintaion: An immutable list is called a tuple.

classification: It is classified as an immutable datatype

how to define the tuple datatype ====> ()
```


```python
students = ('ramesh','vishal', 'keerthi', 'pranavi', 'joseph', 'abdul')
```


```python
print(students)
```

    ('ramesh', 'vishal', 'keerthi', 'pranavi', 'joseph', 'abdul')



```python
type(students)
```




    tuple




```python
# note: we will not be able to edit or modify the tuple datatype
```


```python
print(students[0])
```

    ramesh



```python
#req: modifying ramesh name to suresh
```


```python
students[0] = 'suresh'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[13], line 1
    ----> 1 students[0] = 'suresh'


    TypeError: 'tuple' object does not support item assignment



```python
dimesion = (200,50)
```


```python
for a in students:
    print(a)
```

    ramesh
    vishal
    keerthi
    pranavi
    joseph
    abdul



```python
# for loop formula:
for tempvar in mainvar:
    print tempvar
```


```python
# note: gap before print is called indentation, without gap if you execute it will show error like below
```


```python
for a in students:
print(a)
```


      Cell In[19], line 2
        print(a)
        ^
    IndentationError: expected an indented block after 'for' statement on line 1




```python

```


```python

```


```python

```


```python
###################Introduction to Dictionaries:#############################
```


```python

```


```python
Defination: A Dictionary is a combination of key value pairs

classification: it is classified as a mutable datatype.

how to define a dictionary ==? {}
```


```python
# req: i want to create a alien game
```


```python
alien = {'color':'green','points':5} #here color is a key and green is a value, so its called key value pairs
```


```python
# how to access the elements in the dictionaries?
```


```python
print(alien['color'])
```

    green



```python
#note: give the key and get the value, you can't do it vice versa
```


```python
print(alien[5])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[35], line 1
    ----> 1 print(alien[5])


    KeyError: 5



```python

```
