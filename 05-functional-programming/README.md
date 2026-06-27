# Learn Functional Programming in Python

## Functional Programming

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

