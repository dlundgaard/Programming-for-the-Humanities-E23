# Assignment 1: Pattern Generation, Authorization Test, and Sequence Generation

**Programming for the Humanities E23.**

>Daniel Lundgaard (202004134@post.au.dk)
>Individual submission.

## 1. Pattern generation

__Task__: Write a script that uses flow control statements to generate the following pattern. Ensure that your script can continue the pattern

```sh
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
```

**[Proposed solution](./task_01.py)**

Tracks current state using `current_width` and the upcoming state-change using binary flag `rising`, which denotes whether `current_width` should increment or decrement at next loop iteration and is flipped when reaching peak width or 0.

The alternating sequence of values `current_width` takes on runs from 0 to `peak_width`, but output to terminal is only made when `current_width > 0`. Starting from `0` is to accomodate the "dead-zone" between waves where no increase/decrease in width occurs. 

Able to continue indefinitely if not interrupted by keyboard termination signal since all variables are bounded to avoid overflow. Parameterised to allow for arbitrary amplitude/width and period between waves, given in Hz.

## 2. Authorization test

__Task__: Write a script that uses at least one function to accept user input of `name` and `password`, prints a polite welcome to the user, and tests if the password is correct (you decide the correct password).

**[Proposed solution](./task_02.py)**

The script prompts the user to enter first a name, then a password. If the password enterede matches the string `"erisology`, the user is issued a welcome-message; otherwise they are informed that the password was invalid and reprompted to try again. 

User can abort/interrupt at any stage using keyboard termination signal.

## 3. Sequence generation

__Task__: Write a script that uses at least one function that when it takes `15` as an argument, it generates this sequence '0010102030508013021034055089014402330377'. The solution must be _scalable_ to the set of all positive integers.

**[Proposed solution](./task_03.py)**

Produces a joined string of 0-padded subsequent Fibonacci sequence terms up to $n$.

Calculates each term of the Fibonacci-sequence as the sum of the two preceding terms, with terms 0, 1 predefined to have Fibonacci-values 0 and 1 respectively.

Initially, the Fibonacci value of each term up to $n$ is computed and retrieved as list. Then values are cast to `str` and prefixed by `'0'` before concatenating all values for all terms to a single string.

Achieved with memoization to cache during process of computing values to avoid recomputing "known" terms of the sequence. 