# Learn Functional Programming in Python

## CH1: Functional Programming

Functional programming is a style or paradigm of programming where we compose functions instead of mutating state (updating the value of variables).
    - Functional programming is more about declaring _what_ you want to happen rather than _how_ you want it to happen.
    - Imperative (or procedural) programming declares both the _what_ and the _how_.
##### Example of imperative code

```Python
car = create_car()
car.add_gas(10)
car.clearn_windows()
```

##### Example of functional code

```Python
return clean_windows(add_gas(create_car()))
```

The important distinction is that in the functional example, we never change the value of the car cariable, we just compose functions that return new values, with the outermost function, `clean_window` in this case, returning the final results. 

In this course, we're working on Doc2Doc, a command line tool for converting documents from one format to another. If you are familiar with Pandoc, the idea is similar. 

### Assignment
Complete th `stylize_title` function. It should take a single string as input, and return a single string as output. The returned string should have both the title centered and a border added. 

- Use the provided functions `center_title` and `add_border`.
- Center the title *before* adding the border.
- Do not create any variables.
- Use only one line of code in the function body.

```Python
def stylize_title(document: str) -> str:
    return add_border(center_title(document))

# Don't touch below this line

def center_title(document: str) -> str:
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)

def add_border(document: str) -> str:
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)
```

Python is _not_ the best language for functional programming. Reasons include:
1. No enforced *static typing* (though *type hints* are supported).
2. (Almost) everything is *mutable*
3. No *tail call optimization*.
4. *Side effects* are common.
5. Imperative and OOP styles abound in popular libraries.
6. *Purity* is not enforced.
7. *Sum types* are hard to define.
8. *Pattern matching* is weak at best.

### Immutability

In FP, we strive to make data *immutable*. Once a value is created, it cannot be changed. Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you are debugging a problem with that variable, you have to consider the possibility that any of those functions could have change the value. 
When a variable is immutable, you can be sure that it hasn't changed since it was created. 
*Generally speaking, immutability means fewer bugs and more maintainable code.*

#### Tuples vs. Lists

You can append to a list, but you cannot append to a tuple. Lists are mutable, tuples are not.

```Python
ages: list[int] = [16, 21, 13]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 13, 80]
```

```Python
ages: tuple[int, ...] = (16, 21, 30)
# note the comma after 80! It's required for a single-element tuple.
more_ages: tuple[int, ...] = (80,)
# all_ages is a brand new tuple
all_ages: tuple[int, ...] = ages + more_ages
# [16, 21, 30, 80]

# or we can even reassign the same variable to point to a new tuple
ages = ages + more_ages
# [16, 21, 30, 80]
```

The `...` in `tuple[int, ...]` means the tuple *can contain any number of* `int` values.

```Python
def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents
```

### Declarative vs imperative programming

avg = Σx/N

Imperative Python code. The `total` variable here is "stateful". 
```Python
def get_average(nums: list[int]) -> float:
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

With functional programming, we sould write code that's a bit more declarative. 
Here we're not keeping track of state. We're simply composing functions to get the results we want. 
```Python
def get_average(nums: list[int]) -> float:
    return sum(nums) / leng(nums)
```

#### Assignment
In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the `get_median_font_size` function. Given a list of numbers representing font sizes, return the median of the list.

For example:

[1, 2, 3] => 2
[10, 8, 7, 5] => 7

- Notice the second list is out of order. Sort the list so that it's in ascending order, then find the middle index, and return the middle number.
- If there's an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but it's good for our purposes).
- If the list is empty, just return None.

Here are some helpful docs:
- sorted
- len
- // (floor division)

To be a good little functional programmer, your code for this lesson should not:
- Use loops
- Mutate any variables (it's okay to create new ones)


My version (Not very functional):
```Python
def get_median_font_size(font_sizes: list[int]) -> None:
    if len(font_sizes) != 0:
        font_sizes = softed(font_sizes)
        median = (len(font_sizes) - 1 // 2
        return font_sizes[median]
    return None
```

The more functional:
```Python
def get_median_font_size(font_sizes: list[int]) -> None:
    If len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes)) - 1) // 2]
```

### Classes vs. Functions

Use classes when you need something long-lived and stateful that would be easier to model if you could share behavior and data structure via inheritance. This is often the case for: video games, simulations, GUIs. The difference is:

**Classes** encourage you to think about the world as a hierarchical collection of objects. Objects bundle behavior, data, and state together in a way that draw boundaries between instances of things, like chess pieces on a board. 

**Functions** encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output. For example, a function might take the entire state of a chess board and a move as input, and return the new state of the board as output. 


### Functional vs OOP
FP and OOP are not are not always at odds with one another. They aren't opposites. Of the four pillars of OOP, inheritance is the only one that doesn't fit with functional programming, due to the mutable classes that come along with it. Encapsulation, polymorphism and abstractions are still used all the time in functional programming. Try using the best ideas from both paradigms effectively and appropriately when you are working with programming languages like Python, JavaScript, or Go that support ideas from both FP and OOP.

### Statements vs Expressions
Statements are actions to be carried out.  
```Python
n: int = 7

def greet(name: str) -> str:
    return f"Hello, {name}!"

if x > 10:
    print(greet("Alice")

for i in range(n):
    print(i)
```

Expressions are subsets of statements that produce values.
```Python
result: int = 2 + 2

length: int = len("Hello")

total_cost: float = len(items) * cost   # Multiple expressions combined into one

print(sum([1, 2, 3, 4]) * 2)    # It's simple to combine expressions


# But this doesn't work!
print((
total = 0
for n in [1, 2, 3, 4]:
    total += n
) * 4)
```

Because expressions always produce values, they're reusable and declarative. You can compose expressions and nest them within each other. Functional programming encourages the use of expressens over statements where possible, because expressions tend to minimize side effects, and make the code easier to reason about. Expressions tend to be concise and logically pure. 

### Ternary Expressions
Ternaries are a great way to reduce a series of statements, like an if/else block, to a single expression.

```Python
result: float = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1
```

A ternary lets us do all that in one expression:
```Python
result: float = number / 2 if number % 2 == 0 else (number *3) + 1

# The syntax for a ternary in Python is:
value_a if condition else value_b
```

#### Assignment

```Python
def choose_parse(file_extention: str) -> str:
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
```

#### Assignment
Debug the `hex_to_rgb` function. `hex_to_rgb` should take a hex triplet color code and return three integers for the RGB values using int().

1. Some of the arguments passed to int() on lines 4, 5, and 6 are incorrect. Review the linked documentation to see how to convert hexadecimal (base 16) values.
2. Use the provided `is_hexadecimal` function inside of `hex_to_rgb` to check if `hex_color` is a valid hexadecimal string.
3. If the input is not six characters long or is not a valid hex string, raise the exception "not a hex color string".

Example:
```Python
red_val: int
green_val: int
blue_val: int
red_val, green_val, blue_val = hex_to_rgb("A020F0")

print(red_val)
# prints 160

print(green_val)
# prints 32

print(blue_val)
# prints 240
```

```Python
def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    if not isinstance(hex_color, str) or len(hex_color) != 6 or not is_hexadecimal(hex_color):
        raise Exception("not a hex color string")

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b

# Don't edit below this line

def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
```



## CH2: First-Class Functions 

### Functions As Values
In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:

```Python
from collections.abc import Callable

def add(x: int, y: int) -> int
    return x + y

# assign the function to a new variable
# called `addition`. It behaves the same as
# the original `add` function

addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7
```

`Callable` is the type hint for a function. Callable[[int, int], int] means a function that takes two `int`s as arguments and returns an int.

```Python
from collections.abc import Callable


def file_to_prompt(file: dict[str, str], to_string: Callable[[dict[str, str]], str]) -> str:


    new_string: str = f"```\n{to_string(file)}\n```"
    return new_string
```


### Anonymous Functions

Anonymous functions have *no name*, and in Python, they're called lambda functions after lambda calculus. Here's a lambda function that takes a single argument `x` and returns the result of `x + 1`:

```Python
lambda x: x + 1
```

Notice that the expression `x + 1` is returnd *automaticalla*, no need for a `return` statement. Compare that to how you'd normally write a function:

```Python
def add_one(x: int) -> int:
    return x + 1
```

Because functions are just values, we cann assign the function to a variable named `add_one`:

```Python
from collections.abc import Callable


    add_one: Callable[[int], int] = lambda x: x + 1
    print(add_one(2)
    # 3
```

Lambda functions might *look* scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations.
Here's an example that uses a lambda to get a value from a dictionary:

```Python
get_age: Callable[[str], int | str] = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane")
# 29
```


#### Assignment

```Python
# list of tuples
file_extension_tuples: list[tuple[str, list[str]]] = [
    ("document", [".doc", ".docx"]),
    ("image", [".jpg", ".png"])
]

# resulting dictionary
file_extensions_dict: dict[str, str] = {
    ".doc": "document",
    ".docx": "document",
    ".jpg": "image",
    ".png": "image"
}

```


```Python
from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]]
) -> Callable[[str], str]:

    file_extension_dict: dict[str, str] = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extension_dict[ext] = tup[0]
    return lambda ext: file_extension_dict.get(ext, "Unknown")
```

## First-Class and Higher-Order Functions

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables. 

- **First-class function:** A function that is treated like any other value
- **Higher-order function:** A function that accepts another function as an argument or returns a function

Python *does* support first-class and higher-order functions.

#### First-Class Example

```Python
from collections.abc import Callable

def square(x: int) -> int:
    return x * x

# Assign function to a variable
f: Callable[[int], int] = square

print(f(5))
# 25
```

#### Higher-Order Example

```Python
def square(x: int) -> int:
    return x * x

def my_map(func: Callable[[int], int], arg_list: list[int]) -> list[int]:
    result: list[int] = []
    for i in arg_list:
        result.append(func(i))
    return result

squares: list[int] = my_map[square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```

### Map
"Map", "filter", and "reduce" are three commonly used higher-order functions in functional programming.

In Python, the built-in map function takes a function and an iterable (often a list) as inputs. It returns an iterator that applies the function to every item, yielding the results. 
With `map`, we can operate on lists without using loops and nasty stateful variables. For example, given this code:

```Python
def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: list[int] = []
for num in nums:
    num_squared: int = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]
```

We could use `map` instead, like this:

```Python
from collections.abc import Iterator

def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: Iterator[int] = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

´map()` returns a "map object", so the list() type constructor is needed to voncvert it back into a standard list.

```Python
from collections.abc import Iterator

def change_bullet_style(document: str) -> str:
    lines_list = document.split("\n")
    changed_lines: Iterator[str] = map(convert_line, lines_list)
    return "\n".join(list(changed_lines))

# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
```

## Filter
The built-in `filter` function takes a function and an iterable (often a list) and returns an iterator that keeps elements from the original iterable only where the result of the function on that item returned `True`.

```Python
def is_even(x: int) -> bool:
    return x % 2 == 0

numbers: list[int] = [1, 2, 3, 4, 5, 6]
evens: list[int] = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

#### Assignment
Complete the remove_invalid_lines function. It accepts a document string as input. It should:

1. Use the built-in filter function with a lambda to make a filtered copy of the input document.
    1. Remove any lines that start with a - character.
    2. Keep all other lines and preserve any trailing newlines (\n).
2. Return the result, all on one expression.


```Python
def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter(lambda line: not line.startwith("-"), document.split("\n")))
```


### Reduce
The built-in `functools.reduce()` function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes.

```Python 
# import functools from the standard library
import functools

def add(sum_so_far: int, x: int) -> int:
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

number: list[int] = [1, 2, 3, 4]
sum: int = functools.reduce(add, numbers)
    # sum_so_far: 1, x: 2
    # sum_so_far: 3, x: 3
    # sum_so_far: 6, x: 4
    # 10 doesn't print, it's just the final result
print(sum)
# 10
```

Notice that we are passing the function `add` without the ()! It means that `reduce` will take care of the execution and pass the parameters for you. Think of passing `add` like handing someone a recipe (the instructions), instead of the finished dich (the result of the execution).

#### Assignment
Complete the join and the join_first_sentences functions.

1. Complete the join function. It's a helper function we'll use in join_first_sentences.
    1. It takes two inputs:
        1. A doc_so_far accumulator string – similar to the sum_so_far variable in the example above.
        2. A sentence string – this is the next string we want to add to the accumulator.
    2. Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

```Python
doc: str = "This is the first sentence"
sentence: str = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence
```

2. Complete the join_first_sentences function.
    1. It accepts two arguments:
        1. A list of sentence strings
        2. An integer n
    2. Only use the first n sentences from the list. If n is zero, just return an empty string.
    3. Use functools.reduce() with your join function to combine the sliced sentences into a single string.
    4. Add a final period without a trailing space and return this string.

`Use list slicing to get the first n sentences.`

Here's an example of the expected behavior:

```Python
joined: str = join_first_sentences(["This is the first sentence", "This is the second sentence", "This is the third sentence"], 2)

print(joined)
# This is the first sentence. This is the second sentence.
```

-----

```Python
import functools


def join(doc_so_far: str, sentence: str) -> str:
    return f"{doc_so_far}. {sentence}"



def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0:
        return ""
    sliced_sentences = sentences[:n]
    combined_string = functools.reduce(join, sliced_sentences)
    return f"{combined_string}."

```


## Map, Filter, and Reduce Review

Higher-order functions like `map`, `filter`, and `reduce` allow us to avoid stateful iteration and mutation of variables.

Take a look at this imperative code that calculates the factorial of a number:

```Python
def factorial(n: int) -> int:
    # a procedure that continuously multiplies
    # the current result by the next number
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

Here's the same factorial function using `reduce`:

```Python
import functools

def factorial(n: int) -> int:
    return functool.reduce(lambda x, y: x * y, range(1, n + 1))
```

In the functional example, we're just combining functions to get the result we want. There's no need to reassign variables or keep track of the program's state in a loop. 

A loop is inherently stateful! Depending on which iteration you're on, the `i` variable has a different value.


### Zip
The zip function takes two iterables (often lists), and return a new iterable where each element is a tuple containing one element from each of the original iterables. 

```Python
a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[tuple[int, int]] = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```

#### Assignment

```Python
valid_formats: list[str] = ["docx", "pdf", "txt", "pptx", "ppt", "md"]

# Don't edit above this line


def pair_document_with_format(doc_names: list[str], doc_formats: list[str] -> list[tuple[str, str]]:
    return list(filter(lambda x: x[1] in valid_formats, zip(doc_names, doc_formats)))

```

#### Assignment
Complete the restore_documents function in one line – if you can. It takes two tuples of document strings, originals and backups, as input. It should return a single clean set of all valid documents from both tuples.

1. Combine the originals and backups tuples.
2. Convert all the combined documents to uppercase with .upper().
3. Filter out documents that are corrupted (where the string is just random numbers, checking with .isdigit()).
4. Return a set to deduplicate the combined valid documents.

**Tip**
I used map, filter, and lambda functions to complete the function on one "line", but it's formatted in multiple lines for readability.

```Python
def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    return set(
        filter(
            lambda doc: not doc.isdigit(), 
            map(lambda doc: doc.upper(), originals + backups)

```


## CH3: Pure Functions


