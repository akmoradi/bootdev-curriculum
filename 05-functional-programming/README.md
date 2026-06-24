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


