.. code:: ipython3

    introduction to tuple datatype :

.. code:: ipython3

    Defintaion: An immutable list is called a tuple.
    
    classification: It is classified as an immutable datatype
    
    how to define the tuple datatype ====> ()

.. code:: ipython3

    students = ('ramesh','vishal', 'keerthi', 'pranavi', 'joseph', 'abdul')

.. code:: ipython3

    print(students)


.. parsed-literal::

    ('ramesh', 'vishal', 'keerthi', 'pranavi', 'joseph', 'abdul')


.. code:: ipython3

    type(students)




.. parsed-literal::

    tuple



.. code:: ipython3

    # note: we will not be able to edit or modify the tuple datatype

.. code:: ipython3

    print(students[0])


.. parsed-literal::

    ramesh


.. code:: ipython3

    #req: modifying ramesh name to suresh

.. code:: ipython3

    students[0] = 'suresh'


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[13], line 1
    ----> 1 students[0] = 'suresh'


    TypeError: 'tuple' object does not support item assignment


.. code:: ipython3

    dimesion = (200,50)

.. code:: ipython3

    for a in students:
        print(a)


.. parsed-literal::

    ramesh
    vishal
    keerthi
    pranavi
    joseph
    abdul


.. code:: ipython3

    # for loop formula:
    for tempvar in mainvar:
        print tempvar

.. code:: ipython3

    # note: gap before print is called indentation, without gap if you execute it will show error like below

.. code:: ipython3

    for a in students:
    print(a)


::


      Cell In[19], line 2
        print(a)
        ^
    IndentationError: expected an indented block after 'for' statement on line 1






.. code:: ipython3

    ###################Introduction to Dictionaries:#############################


.. code:: ipython3

    Defination: A Dictionary is a combination of key value pairs
    
    classification: it is classified as a mutable datatype.
    
    how to define a dictionary ==? {}

.. code:: ipython3

    # req: i want to create a alien game

.. code:: ipython3

    alien = {'color':'green','points':5} #here color is a key and green is a value, so its called key value pairs

.. code:: ipython3

    # how to access the elements in the dictionaries?

.. code:: ipython3

    print(alien['color'])


.. parsed-literal::

    green


.. code:: ipython3

    #note: give the key and get the value, you can't do it vice versa

.. code:: ipython3

    print(alien[5])


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[35], line 1
    ----> 1 print(alien[5])


    KeyError: 5


