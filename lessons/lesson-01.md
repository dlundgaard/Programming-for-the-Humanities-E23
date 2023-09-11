## Lesson 1.1 File system ##

In order for Python to use  to use certain files you need to direct it to where they can find them. This means, you need to know how to navigate your file system. Therefore it is important that you understand how your computer is organised.

The part of the operating system responsible for managing files and directories is called the _file system_. It organizes our data into files, which hold information, and directories (also called ‘folders’), which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories. To start exploring them, we’ll go to a Terminal application.

First, let’s find out where we are by running a command called `pwd` (which stands for 'print working directory'). Directories are like places — at any time while we are using the shell, we are in exactly one place called our current working directory. Commands mostly read and write files in the current working directory, i.e. 'here', so knowing where you are before running a command is important. `pwd` shows you where you are:

```bash
$ pwd

/home/nelle
```

You can also get your working directory from via Python, but it requires you to import and use the `os` library (more about that later):

```py
>>> import os
>>> print(os.getcwd())

/home/nelle
```

Irrespective of the method, the computer's response is `/home/nelle`, which is Nelle's home directory

> **_Home Directory Variation:_**  The home directory path will look different on different operating systems. On Linux, it may look like `/home/nelle`, on Mac it will looks like `/Users/nelle`, and on Windows, it will be similar to `C:\Documents and Settings\nelle` or `C:\Users\nelle`. (Note that it may look slightly different for different versions of Windows.) In future examples, we’ve used Linux output as the default - Mac and Windows output may differ slightly but should be generally similar.We will also assume that your pwd command returns your user’s home directory. If `pwd` returns something different, you may need to navigate there using `cd` or some commands in this lesson will not work as written.

To understand what a 'home directory' is, let’s have a look at how the file system as a whole is organized. For the sake of this example, we’ll be illustrating the filesystem on our scientist Nelle's computer. After this illustration, you’ll be learning commands to explore your own filesystem, which will be constructed in a similar way, but not be exactly identical.

On Nelle’s computer, the filesystem looks like this:

```bash
/
├── bin
├── data
├── home
└── tmp
```

At the top is the root directory that holds everything else. We refer to it using a slash character, `/`, on its own; this character is the leading slash in `/home/nelle`.

Inside that directory are several other directories: `bin` (which is where some built-in programs are stored), `data` (for miscellaneous data files), `home` (where users’ personal directories are located), `tmp` (for temporary files that don’t need to be stored long-term), and so on.

We know that our current working directory `/home/nelle` is stored inside `/home` because `/home` is the first part of its name. Similarly, we know that `/home` is stored inside the root directory `/` because its name begins with `/`.

> **_Slaches:_** Notice that there are two meanings for the `/` character. When it appears at the front of a file or directory name, it refers to the root directory. When it appears _inside_ a path, it’s just a separator.

Underneath /home, we find one directory for each user with an account on Nelle’s machine, her colleagues imhotep and larry.

```bash
/
├── bin
├── data
├── home
│   ├── imhotep
│   ├── larry
│   └── nelle
└── tmp
```

The user  _imhotep_'s files are stored in `/home/imhotep`, user larry’s in `/home/larry`, and Nelle’s in `/home/nelle`. Because Nelle is the user in our examples here, therefore we get `/home/nelle` as our home directory. Typically, when you open a new command prompt, you will be in your home directory to start.

Now let's learn the command that will let us see the contents of our own filesystem. We can see what's in our home directory by running `ls`:

```bash
$ ls

Desktop  Documents  Downloads  Music  Pictures  Public  Videos
```

and with Python

```py
>>> import os
>>> print(os.listdir())

['Music', 'Desktop', 'Pictures', 'Downloads', 'Public', 'Videos', 'Documents']
```

(Again, your results may be slightly different depending on your operating system and how you have customized your filesystem.)

`ls` prints the names of the files and directories in the current directory. We can make its output more comprehensible by using the `-F` option which tells `ls` to _classify_ the output by adding a marker to file and directory names to indicate what they are:

a trailing `/` indicates that this is a directory
`@` indicates a link
`*` indicates an executable

Depending on your shell’s default settings, the shell might also use colors to indicate whether each entry is a file or directory.

```bash
$ ls -F

Desktop/  Documents/  Downloads/  Music/  Pictures/  Public/  Videos/
```

and with Python

```py
>>> import os
>>> os.system('ls -F')

Desktop/  Documents/  Downloads/  Music/  Pictures/  Public/  Videos/
```

Here, we can see that our home directory contains only _sub-directories_. Any names in our output that don't have a classification symbol are plain old _files_.

> **_Clearing your terminal:_** If your screen gets too cluttered, you can clear your terminal using the `clear` command. You can still access previous commands using `↑` and `↓` to move line-by-line, or by scrolling in your terminal.

### Exploring Other Directories ###

Not only can we use `ls` on the current working directory, but we can use it to list the contents of a different directory. Let's take a look at our `Desktop` directory by running `ls -F Desktop`, i.e., the command `ls` with the `-F` option and the argument `Desktop`. The argument `Desktop` tells `ls` that we want a listing of something other than our current working directory:

```bash
$ ls -F Desktop/

terminal-lesson-data/
```

Note that if a directory named `Desktop` does not exist in your current working directory, this command will return an error. Typically, a `Desktop` directory exists in your home directory, which we assume is the current working directory of your terminal.

As you may now see, using a terminal is strongly dependent on the idea that your files are organized in a hierarchical file system. Organizing things hierarchically in this way helps us keep track of our work: it's possible to put hundreds of files in our home directory, just as it's possible to pile hundreds of printed papers on our desk, but it’s a self-defeating strategy.

Now that we know the `terminal-lesson-data` directory is located in our `Desktop` directory, we can do two things.

First, we can look at its contents, using the same strategy as before, passing a directory name to `ls`:

```bash
$ ls -F Desktop/terminal-lesson-data/

exercise-data/  north-pacific-gyre/
```

Second, we can actually change our location to a different directory, so we are no longer located in our home directory.

The command to change locations is `cd` followed by a directory name to change our working directory. `cd` stands for 'change directory', which is a bit misleading: the command doesn't change the directory; it changes the shell's idea of what directory we are in. The `cd` command is akin to double-clicking a folder in a graphical interface to get into a folder.

Let's say we want to move to the `data` directory we saw above. We can use the following series of commands to get there:

```bash
$ cd Desktop
$ cd terminal-lesson-data
$ cd exercise-data
```

These commands will move us from our home directory into our Desktop directory, then into the `shell-lesson-data` directory, then into the `exercise-data` directory. You will notice that `cd` doesn't print anything. This is normal. Many terminal commands will not output anything to the screen when successfully executed. But if we run `pwd` after it, we can see that we are now in `/home/nelle/Desktop/terminal-lesson-data/exercise-data`.

If we run `ls -F` without arguments now, it lists the contents of `/home/nelle/Desktop/terminal-lesson-data/exercise-data`, because that's where we now are:

```bash
$ pwd

/home/nelle/Desktop/terminal-lesson-data/exercise-data

$ ls -F

animal-counts/  creatures/  numbers.txt  proteins/  writing/
```

We now know how to go down the directory tree (i.e. how to go into a subdirectory), but how do we go up (i.e. how do we leave a directory and go into its parent directory)? We might try the following:

```bash
$ cd terminal-lesson-data

-bash: cd: terminal-lesson-data: No such file or directory
```

But we get an error! Why is this?

With our methods so far, `cd` can only see sub-directories inside your current directory. There are different ways to see directories above your current location; we’ll start with the simplest.

There is a shortcut in the shell to move up one directory level that looks like this:

```bash
$ cd ..
$ pwd

/home/nelle/Desktop/terminal-lesson-data
```

The special directory `..` doesn't usually show up when we run `ls`. If we want to display it, we can add the `-a` option to `ls -F`:

```bash
$ ls -F -a

./  ../  exercise-data/  north-pacific-gyre/
```

`-a` stands for 'show all'; it forces ls to show us file and directory names that begin with `.`, such as `..` (which, if we're in /home/nelle, refers to the /home directory). As you can see, it also displays another special directory that's just called `.`, which means 'the current working directory'. It may seem redundant to have a name for it, but we’ll see some uses for it soon.

Note that in most command line tools, multiple options can be combined with a single - and no spaces between the options: `ls -F -a` is equivalent to `ls -Fa`.

> **_Other Hidden Files:_** In addition to the hidden directories `..` and `.`, you may also see a file called `.bash_profile`. This file usually contains shell configuration settings. You may also see other files and directories beginning with `..` These are usually files and directories that are used to configure different programs on your computer. The prefix `.` is used to prevent these configuration files from cluttering the terminal when a standard ls command is used.

These three commands are the basic commands for navigating the filesystem on your computer: `pwd`, `ls`, and `cd`. Let’s explore some variations on those commands. What happens if you type cd on its own, without giving a directory?

```bash
$ cd
$ pwd

/home/nelle
```

It turns out that `cd` without an argument will return you to your home directory, which is great if you’ve got lost in your own filesystem.

Let’s try returning to the `exercise-data directory` from before. Last time, we used three commands, but we can actually string together the list of directories to move to exercise-data in one step:

```bash
$ cd Desktop/terminal-lesson-data/exercise-data
```

Check that we’ve moved to the right place by running `pwd` and `ls -F`.

If we want to move up one level from the data directory, we could use `cd ..`. But there is another way to move to any directory, regardless of your current location.

So far, when specifying directory names, or even a directory path (as above), we have been using __relative paths__. When you use a relative path with a command like `ls` or `cd`, it tries to find that location from where we are, rather than from the root of the file system.

However, it is possible to specify the __absolute path__ to a directory by including its entire path from the root directory, which is indicated by a leading slash. The leading `/` tells the computer to follow the path from the root of the file system, so it always refers to exactly one directory, no matter where we are when we run the command.

This allows us to move to our `terminal-lesson-data` directory from anywhere on the filesystem (including from inside `exercise-data`). To find the absolute path we're looking for, we can use `pw`d and then extract the piece we need to move to shell-lesson-data.

```bash
$ pwd

/home/nelle/Desktop/shell-lesson-data/exercise-data

$ cd /home/nelle/Desktop/shell-lesson-data

```

Run `pwd` and `ls -F` to ensure that we're in the directory we expect.

### Two more shortcuts ###

The shell interprets a tilde (`~`) character at the start of a path to mean "the current user's home directory". For example, if Nelle’s home directory is `/home/nelle`, then ~/data is equivalent to `/home/nelle/data`. This only works if it is the first character in the path: `here/there/~/elsewhere` is not `here/there/home/nelle/elsewhere`.

Another shortcut is the dash (`-`) character. `cd` will translate `-` into the previous directory I was in, which is faster than having to remember, then type, the full path. This is a very efficient way of moving back and forth between two directories – i.e. if you execute `cd -` twice, you end up back in the starting directory.

The difference between `cd ..` and `cd -` is that the former brings you up, while the latter brings you back.

## Lesson 1.2: Python as a Calculator ##
 
* entering command in the interacitve shell/Read-Evaluate-Print Loop
* REPL allows line-by-line execution

## Entering an expression

* basic math operations

```py
>>> 2 + 2
4
>>> 2 ** 3
8
>>> 22 % 8
6
>>> 22 // 8 # integer division/floored quotient
2
>>> 22 / 8
2.75
>>> 3 * 5
15
>>> 5 - 2
3
```

### Precedence

* order of operations
* order of operations (**, %, //, /, *, -, +)

```py
>>> 2 + 3 * 6
20
>>> (2 + 3) * 6
30
>>> (5 - 1) * ((7 + 1) / (3 - 1))
16.0
```

## 1.3 Variable assignment ##

* variable: a value assigned a label

```py
>>> spock = 50 # initialize variable
>>> spock
50
>>> janeway = 35
>>> spock + janeway 
85
>>> spock + janeway + janeway
135
>>> spock = spock + 5 # assigne new value to variable (old is  overwritten)
>>> spock
55
```

* overwrite string

```py
>>> captain = 'Kirk'
>>> captain
'Kirk'
>>> captain = 'Piccard'
>>> captain
Piccard
```

### Valid variable names ###

* one word with no spaces
* only use letters, numbers and underscore
* cannot begin with number

| Valid | Invalid |
| --- | --- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |

## Lesson 1.4: Errors    ##

* `SyntaxError` error message
* The most common reason of an error in a Python program is when a certain statement is not in accordance with the prescribed usage. Such an error is called a syntax error. The Python interpreter immediately reports it, usually along with the reason.


```py
>>> print 'hello'
  File "<stdin>", line 1
    print 'hello'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?
```
* In Python 3.x, print is a built-in function and requires parentheses. The example statement violates this usage and hence syntax error is displayed.


```py
>>> 5 +
  File "<stdin>", line 1
    5 +
      ^
SyntaxError: invalid syntax
```


```py
>>> 2 +* 3
  File "<stdin>", line 1
    2 +* 3
       ^
SyntaxError: invalid syntax
>>> 
```

* breaking down the error message
    * The file name where the invalid syntax was encountered
    * The line number and reproduced line of code where the issue was encountered
    * A caret (^) on the line below the reproduced code, which shows you the point in the code that has a problem
    * The error message that comes after the exception type SyntaxError, which can provide information to help you determine the problem

```sh
File "src/tracebackerror.py", line 11
    2 +* 3
       ^
SyntaxError: invalid syntax
```

#### Type of errors

* Important built-in exceptions in Python.

| Exception | Description |
| -- | -- |
| AssertionError | Raised when the assert statement fails. |
| AttributeError | Raised on the attribute assignment or reference fails. |
| EOFError | Raised when the input() function hits the end-of-file condition. |
| FloatingPointError | Raised when a floating point operation fails. |
| GeneratorExit | Raised when a generator's close() method is called. |
| ImportError | Raised when the imported module is not found. |
| IndexError | Raised when the index of a sequence is out of range. |
| KeyError | Raised when a key is not found in a dictionary. |
| KeyboardInterrupt | Raised when the user hits the interrupt key (Ctrl+c or delete) |.
| MemoryError | Raised when an operation runs out of memory. |
| NameError | Raised when a variable is not found in the local or global scope. |
| NotImplementedError | Raised by abstract methods. |
| OSError | Raised when a system operation causes a system-related error. |
| OverflowError | Raised when the result of an arithmetic operation is too large to be represented. |
| ReferenceError | Raised when a weak reference proxy is used to access a garbage collected referent. |
| RuntimeError | Raised when an error does not fall under any other category. |
| StopIteration | Raised by the next() function to indicate that there is no further item to be returned by the iterator. |
| SyntaxError | Raised by the parser when a syntax error is encountered. |
| IndentationError | Raised when there is an incorrect indentation. |
| TabError | Raised when the indentation consists of inconsistent tabs and spaces. |
| SystemError | Raised when the interpreter detects internal error. |
| SystemExit | Raised by the sys.exit() function. |
| TypeError | Raised when a function or operation is applied to an object of an incorrect type. |
| UnboundLocalError | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| UnicodeError | Raised when a Unicode-related encoding or decoding error occurs. |
| UnicodeEncodeError | Raised when a Unicode-related error occurs during encoding. |
| UnicodeDecodeError | Raised when a Unicode-related error occurs during decoding. |
| UnicodeTranslateError | Raised when a Unicode-related error occurs during translation. |
| ValueError | Raised when a function gets an argument of correct type but improper value. |
| ZeroDivisionError | Raised when the second operand of a division or module operation is zero. |

* `IndexError`

```py
>>> l = [1, 1, 2, 3, 5]
>>> l[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

* `ModuleNotFoundError`

```py
>>> import notamodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'notamodule'
```

* `KeyError`

```py
>>> captains = {'Enterprise' : 'Kirk', ' Voyager' : 'Janeway', 'DS9' : 'Sisko'}
>>> captains['BorgCube']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'BorgCube'
```

* `ImportError`

```py
>>> from math import borgcube
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'borgcube' from 'math' (unknown location)
```

* `NameError`

```py
>>> borg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'borg' is not defined
```

* `ValueError`

```py
>>> int('borg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'borg
```


## Advanced topics

* Linting: Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors. For example, linting detects use of an uninitialized or undefined variable, calls to undefined functions, missing parentheses, and even more subtle issues such as attempting to redefine built-in types or functions.  Linting is thus distinct from Formatting because linting analyzes how the code runs and detects errors whereas formatting only restructures how code appears. (see `linting.py`)

---

* content
    - snake case for variables, camel case for classes
    - "Consistency with the style guide is important. But most importantly: know when to be inconsistent—sometimes the style guide just doesn’t apply. When in doubt, use your best judgment."
* advanced content
    - mutable and immutable data types
      * mutable: list, dictionary, set, user-defined classes
      * immutable: int, float, decimal, bool, string, tuple, range
    - deep and shallow copy: see `var_copy.py`   