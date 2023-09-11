# Execercises 01: Basic Python #

## Pair programming ##

<details>
  <summary> Write a program, <code>hello.py</code>  that that says hello and asks for name </summary>

```py
print('Hello, world!')
print('What is your name?')
name = input()
print(f'Good to meet you {name}')

print(f'The length of your name is {len(name)}')

print('What is your age?')
age = input()
print(f'You will be {int(age) + 1} in a year')
```

</details>

## Check your understanding ##

<details>
  <summary> 1: What values do the variables <code>mass</code>  and <code>age</code> have after each of the following statements? Test your answer by executing the lines. 

```py
>>> mass = 47.5
>>> age = 122
>>> mass = mass * 2.0
>>> age = age - 20
```
</summary>

1. `mass` holds a value of 47.5, `age` does not exist
2. `mass` still holds a value of 47.5, `age` holds a value of 122
3. `mass` now has a value of 95.0, `age`'s value is still 122
4. `mass` still has a value of 95.0, `age` now holds 102

</details>

<details>
  <summary> 2: Sorting Out References. Python allows you to assign multiple values to multiple variables in one line by separating the variables and values with commas. What does the following program print out?

```py
>>> first, second = 'James', 'Kirk'
>>> third, fourth = second, first
>>> print(third, fourth)
```

</summary>

- `Kirk James`

</details>

<details>
  <summary> 3: Seeing Data Types. What are the data types of the following variables?

```py
planet = 'Earth'
apples = 5
distance = 10.5
```
</summary>

* `str`
* `int`
* `float`

</details>

## Practice questions ##

<details>
  <summary> 1: Which of the following are operators, and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

</summary>

- operator
- value
- value
- operator
- operator
- operator
- value

</details>

<details>
  <summary> 2: Which of the following is a variable, and which is a string?

```py
spam
'spam'
```
</summary>

- `spam` is a variable and `'spam'` is a string

</details>

<details>
  <summary> 3: Name three data types </summary>

* sting
* integer
* float

</details>

<details>
  <summary> 4: What is an expressions made up of? What fo all expressions do? </summary>

* An expression is an instruction that combines values and operators and always evaluates down to a single value.

</details>

<details>
  <summary> 5: What is a statement, e.g., assignment statement <code>var = 10</code> </summary>

- A statement is an instruction that the Python interpreter can execute. We have seen two kinds of statements: print and assignment. When you type a statement on the command line, Python executes it and displays the result, if there is one. The result of a print statement is a value.
- Statements represent an action or command e.g print statements, assignment statements. Expression is a combination of variables, operations and values that yields a result value. An expression is something that can be reduced to a value, for example `1+3` is an expression, but `foo = 1+3` is not.

</details>

<details>
  <summary> 6: what does the variable `spock` contain in the following code </summary>

```py
spock = 20
spock + 1
```

</details>

<details>
  <summary> 7: What should the following two expressions evaluate to </summary>

```py
'spam' + 'spamspam'
'spam' * 3
```

</details>

<details>
  <summary> 8: Why is <code>spock</code>  a valid variable name and 100 invalid </summary>

- one word with no spaces
- only use letters, numbers and underscore
- cannot begin with number

| Valid | Invalid |
| --- | --- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |

</details>

<details>
  <summary> 9: What three functions can be used to get the integer, floating-point numner, string version of a value? </summary>

- `int()`
- `float()`
- `str()`

</details>