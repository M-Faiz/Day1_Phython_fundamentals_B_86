```python
continutaion with list datatype
```


```python
# Organising the list datatype
```


```python
Slicing the list :
```


```python
# Genral syntax of slicing :
[Start_value: stop_value: Step_count]
```


```python
students = ['Naveen', 'raju', 'khader','joseph', 'keerthi', 'sahana' ]
```


```python
print (students)
```

    ['Naveen', 'raju', 'khader', 'joseph', 'keerthi', 'sahana']



```python
type (students)
```




    list




```python
Note_point: stop value is always exclusive, to include the stop value we have to increment the number by +1
```


```python
# req: i want to include Naveen and Raju in the slice
```


```python
print (students [0:1])
```

    ['Naveen']



```python
print (students [0:2])
```

    ['Naveen', 'raju']



```python
# req: i want to include khader and joseph in the slice
```


```python
print(students [2:4])
```

    ['khader', 'joseph']



```python
print(students [4:6])
```

    ['keerthi', 'sahana']



```python
print (students [0:6:2])
```

    ['Naveen', 'khader', 'keerthi']



```python
print (students)
```

    ['Naveen', 'raju', 'khader', 'joseph', 'keerthi', 'sahana']



```python

```


```python

```


```python
Introducing to for loop:
```


```python
# genral syntax of for Loop :
```


```python
for tempvar in mainvar:
print (tempvar)
```


```python
print(students)
```

    ['Naveen', 'raju', 'khader', 'joseph', 'keerthi', 'sahana']



```python
message = f"keep up the good work, {students[0].title()}"
print(message)
```

    keep up the good work, Naveen



```python
message = f"keep up the good work, {students[1].title()}"
print(message)
```

    keep up the good work, Raju



```python
for x in students:
   print(f"keep up the good work, {x}")
```

    keep up the good work, Naveen
    keep up the good work, raju
    keep up the good work, khader
    keep up the good work, joseph
    keep up the good work, keerthi
    keep up the good work, sahana



```python
for x in students:
   print(f"keep up the good work, {x}")
   print(f"good going {x}")
```

    keep up the good work, Naveen
    good going Naveen
    keep up the good work, raju
    good going raju
    keep up the good work, khader
    good going khader
    keep up the good work, joseph
    good going joseph
    keep up the good work, keerthi
    good going keerthi
    keep up the good work, sahana
    good going sahana



```python
for x in students:
   print(f"keep up the good work, {x}")
   print(f"good going {x}\n")
```

    keep up the good work, Naveen
    good going Naveen
    
    keep up the good work, raju
    good going raju
    
    keep up the good work, khader
    good going khader
    
    keep up the good work, joseph
    good going joseph
    
    keep up the good work, keerthi
    good going keerthi
    
    keep up the good work, sahana
    good going sahana
    



```python

```
