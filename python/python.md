# python notes for my future reference

---

## index 

1. [shebang](#shebang)
2. [strings](#strings)
    - [string formatting](#string-formatting)
3. [list](#lists)
4. [multiple assignment](#multiple-assignment)
5. [operators](#operators)
6. [loop](#for-loop)
7. [range()](#range-function)
8. [break and continue](#break-continue)
9. [pass](#pass)
10. [match](#match)
11. [function](#function)
12. [class](#class)
13. [dictionary](#dictionary)
14. [modules](#modules)

---

### shebang
- make the python file an executable,
- add the line #!/usr/bin/env python to the **first line**, then only
- then chmod +x file-name.py
- then ./file-name.py

### strings

- use \ to escape strings,
- ' and " are treated 
- print(r'c\name') // not \n not treated as newline

- string literal """ """ or ''' ''' to enclose large peices of text

- concatenate with + or simply strings beside one another, " he" "-man" // cant concatnate with variable " string"
- repeat with * operator

``` python
word = "python"
print(word[0]) # prints out p

word[-1] # last character

# slicing

word[2:5] # tho [2,5) # 2 included 5 excluded
word[:2] # beginning to 2
word[-2:] # second last to end
word[2:1228] # IndexError
word[start:end:skip]

# there is no function like strrev, thus we use
word[::-1] # to reverse a string

# functions

str.upper()
str.lower()

# gives either true or false
str.startswith("str-2") 
str.endswith("str-3")

# split
str.split("char")
# splits the string from the string "char" to the next "char"
# default is " " , which splits the words in the sentence

# index
str.index(char)
# returns what index char is at

str.count(char)
# counts the occurences of the word/letter char



```

len(s) returns length of string
- string is immutable i.e. you can't str[2] = 'a'

- [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### string-formatting

- print("%s is %d years and %m months old" % (name, ageYear, ageMonth))
- an object which is not a string can be formatted too, eg print("%s" % [1,2,3])
- formatted string literal or f-string is f"some text"
- procedure to format f"text {var}"
- displays the var
- f"text {var=}" # displays the var name and its value (for debugging useful)

- formatting with str.format()

- stri.format(a,b,c)
- stri = " random string {0} first arg {1} {2} args have a, b, c var vals "


### lists

- squares = [1,4,9,16,25]
- string functions, slice etc can work on lists,
- lists are mutable, i.e. they  lst[2] = 3 // valid

> 7 ** 3 // 7^3
- list.append(element) # to add element to end of list

> note: list.append(element) is more efficient than list = list + [element]



- slice and change also psbl, ls[2:4] = [1,2] 
- clear the list, ls[:] = []
- length of the list, len(listName)

- nest the list a = [1,2,3]
- b = [ 4, 5 ,6]
- c = [a,b]
- c [0][2] // multi-array notation

### multiple-assignment
a,b = 0, 1
- expressions on the right side are evaluated first before assignment takes place 
- non int value true, 0 false in python

### operators

``` python 

and
or
not

in # if this in [list]

is # x=[2,3], y=[2,3] , x is y (false) compares object instances, unlike == operator

```
### if

- sequence can be used

```py

if answer in ('y', 'yes', 'yeah', 'ye'):
    # code

```

### for-loop

``` python
# Create a sample collection

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# if the loop condition becomes false, or break is not executed, then the else part executed
while condition:
    # exec
else:
    # exec if condition false
```

### range-function

- doesn't return a list
- returns an object which gives successive items of the desired sequence
- range(start, after-end, step)

### break-continue
 
- break statement returns out of for or while loop
- inside a loop, if break is there, there can also be and else block, the else block will run if
there is no break.

- continue makes the next iteration of the loop

### pass

- does nothing.
- if statement is required syntactically but the program has no action there
- like :-
    while True:
	pass

- ( similar to just ; in c++ )
- commonly used for creating minimal classes, eg:
    class EmptyClass:
	pass

- Another place pass can be used is as a place-holder for a function or conditional body when 
you are working on new code, allowing you to keep thinking at a more abstract level. 
The pass is silently ignored:

``` python
def initlog(*args):
    pass   # Remember to implement this!
```
### match

- python ka switch

match status:
    case 100:
	return ...
    case 300:
	return ...
    case 200:
	return ...
    case 500:
	return ...


- Only the first pattern that matches gets executed

``` python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

- the thing _ acts as default, it is executed when nothing is,
- the variable in case number 2-4 binds itself to the thing given by *point* tuple.
- the fourth thing is same as doing (x, y) = point

- combine the cases, 
    case 401 | 403 | 404: // this | stands for 'or'
	do stuff

``` python

  match point:
    case Point(x, y) if x == y: // this if clause is known as a guard
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

```


### function

``` python

def function_name(argument):
    """ documentation string """
    # function operation

print(function_name.__doc__)
# prints out the doc string

"""


"""

```

*The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas **variable references first look in the local symbol table**, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.*

*The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.*

*A function definition associates the function name with the function object in the current symbol table. The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same function object and can also be used to access the function*

```py

a = 10
def fib():
    print(a)

f = fib

f()
# prints a


```

- `return` statement alone, returns `None` , None is a built in python entity,
if function doesnt return anything, it returns None.


- default argument values:

```py

def f(a, b=3, c=4):
    # code

f(1)
f(2,9)
f(5,5,5)

# can be called all three ways, if arg not specified, then default arg called

# eg: print

print("hello", end="")
# prints without newline

"""
The default values are evaluated at the point of function definition in the defining scope
"""
# thus then if 
i = 2

def f(ag=i):
    # code

i = 4
f()
# calls out with i = 2
```
- Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable
object such as a list, dictionary, or instances of most classes.

- function can be called with a keyword arg, f(a='', b=other), even if the order is not correct, but keyword specified

``` def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2): ```



### class

- template to create object
- object : encapsulation of variable and functions

``` py

class myClass:
    var = "haha"

    def __init__(self, number):
        self.number = number
    # __init__() is a special function called when the class is being initiated, it is used for assigning
    # values in a class
    # like a constructor

# create object

obj = myClass()


```

### dictionary

- key : value

``` py

a = {}
a["a"] = 1
a["b"] = 2
a["c"] = 3


# or


a {
    "a" : 1
    "b" : 2
    "c" : 3
}

# iteration over dictionary

for letter, num in a.items():
    # code

# to delete an index

del dic["key"]

# or

dic.pop("key")

```

### modules

- make a file named name.py in same directory ./
- then in main.py, 

``` py

import name 
# loads the name script and all its objects into out main

from name import particular_variable
from name import particular_function

#                  ^
# to ease the load |

# to import all objects from the module

from mod import *



```























