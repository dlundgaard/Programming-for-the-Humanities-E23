# Exercises for Functions Lesson #

## Pair programming ##

<details>
<summary>
Create a function that takes a list as input, ex. <code>[1, 1, 2, 3, 5, 8]</code> and returns the list in reverse order, ex, <code>[8, 5, 3, 2, 1, 1]</code>.

</summary>

_ANSWER_

```py
def reverser(lst):
    return lst[::-1]

# or

def reverser(lst):
    res = list()
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res
```
</details>

## Check your understanding ##

<details>

<summary>1. Combining Strings: 'Adding' two strings produces their concatenation: <code>a + b</code> is <code>ab</code>. Write a function called <code>fence()</code> that takes two parameters called <code>original</code> and <code>wrapper</code> and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

```py
>>> print(fence('name', '*'))
```

and the output should be

```py
*name*
```

</summary>

_ANSWER_

```py
def fence(original, wrapper):
    return wrapper + original + wrapper
```
</details>


<details>
<summary>2. Return versus print: Note that <code>return</code> and <code>print()</code> are not interchangeable. <code>print()</code> is a function that prints data to the screen. It enables us, users, see the data. The <code>return</code> statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:

```py
def add(a, b):
    print(a + b)
```

What will we see if we execute the following commands?

```py
A = add(7, 3)
print(A)
```
</summary>

_ANSWER_

Python will first execute the function `add()` with `a = 7` and `b = 3`, and, therefore, print 10. However, because function `add()` does not have a line that starts with `return` (no return 'statement'), it will, by default, return nothing which is called `None`. Therefore, A will be assigned to `None` and the last line (`print(A)`) will print `None`. As a result, we will see:

```py
10
None
```
</details>

<details>
<summary>3. Selecting Characters From Strings: If the variable <code>s</code> refers to a string, then <code>s[0]</code> is the string's first character and <code>s[-1]</code> is its last. Write a function called <code>outer()</code> that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

```py
>>> print(outer('helium'))
```

and output 

```py
hm
```

</summary>

_ANSWER_

```py
def outer(input_string):
    return input_string[0] + input_string[-1]
```

</details>


## Practice questions ##

In your answers to practice questions, try to use code to illustrate your answer.

<details>
<summary>1: Why are the advantageous of functions, and more generally, modular programming?

</summary>

_ANSWER_

modular/manageble & reusable code

</details>

<details>
<summary>2: When does the code in a function execute: during function definition or function call?

</summary>

_ANSWER_

function call

</details>

<details>
<summary>3: What statement creates a function?

</summary>

_ANSWER_

the `def` statement works as follows. `def` is the keyword for defining a function. The function name is followed by parameter(s) in (). The colon : signals the start of the function body, which is marked by indentation. Inside the function body, the return statement determines the value to be returned. 

</details>

<details>
<summary>4: What is the difference between a function and a function call?

</summary>

_ANSWER_

A function call means invoking or calling that function. Unless a function is called there is no use of that function. The difference between the function and function call is, _a function is procedure to achieve a particular result while function call is using this function to achive that task_.

</details>

<details>
<summary>5: How many scopes are there in Python?

</summary>

_ANSWER_

two or four depending on how you count

</details>

<details>
<summary>6: What happens to a variable in local scope, when the function call returns?

</summary>

_ANSWER_

deleted

</details>

<details>
<summary>7: What is a return value? Can a return value be part of an expression?

</summary>

_ANSWER_

The `return` statement is a special statement that you can use inside a function or method to send the function's result back to the caller. A return statement consists of the return keyword followed by an optional return value. The return value of a Python function can be any Python object.

Yes, because an expression is just a representation of a value. Expressions are composed of values and operators. A function call can be used in an expression because the call evaluates to its return value.

```py
def hello(name):
    return name

print(hello('Spock'))
```

</details>

<details>
<summary>8: If a function lacks a return statement, what is the return value of the function call?

</summary>

_ANSWER_

`None`

</details>

<details>
<summary>9: What keyword allow you to update a global variable in a function?

</summary>

_ANSWER_

`global`

</details>

<details>
<summary>10: What does `None` mean?

</summary>

_ANSWER_

null value

</details>

<details>
<summary>11: What does the `import numpy` statement do?


</summary>

_ANSWER_

import the objects in the numpy namespace

</details>

<details>
<summary>12: If you have a function named <code>randint()</code> and a module named <code>random</code>, how would you import and call <code>randint</code>?

</summary>

_ANSWER_

`random.randint()`

</details>

<details>
<summary>13: How do you prevent a program from crashing, when it gets an error?

</summary>

_ANSWER_

`try - except`, `assert`

</details>

<details>
<summary>14: What constitutes the <code>try</code> clause? What constitutes the <code>except</code> clause?

</summary>

_ANSWER_

In the try clause, all statements are executed until an exception is encountered. except is used to catch and handle the exception(s) that are encountered in the try clause. else lets you code sections that should run only when no exceptions are encountered in the try clause.

* `try` keyword, `:`, indentation and code to be executed
* `except` keyword, `:`, indentation and code to be executed when exeption occurs

</details>