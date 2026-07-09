from collections.abc import Callable


def add(x: int, y: int) -> int:
    return x + y

# assign the function to a new variable
# called `addition`. It behaves the same
# as the original `add` function
addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7

-------------------------

# Callable is the type hint for a function. Callable[[int, int], int] means a function that takes two `int`s as arguments and returns an int.

-------------------------
from collections.abc import Callable


def file_to_prompt(
        file: dict[str, str], to_string: Callable[[dic[str, str]], str]) -> str:
    new_string: str = f"```\n{to_string(file)}\n```"
    return new_string
-------------------------

from collections.abc import Callable


def file_to_prompt(
        file: dic[str, str], to_string: Callable[[dict[str, str]], str]
        ) -> str:
    stringified = to_string(file)
    return f"```\n{stringified}\n```"
----------------------------

from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list]]]
) -> Callable[[str], str]:

    file_extension_dict: dic[str, str] = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extension_dict[ext] = tup[0]
    return lambda ext: file_extension_dict.get(ext, "Unknown")

------------------------------

from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]]
    ) -> Callable[[str], str]:

    file_extension_dict: dic[str, str] = {}
    for tup in file_extension_tuples:
        for extension in tup[1]:
            file_extension_dict[extension] = tup[0]
    return lambda extension: file_extension_dict.get(extension, "Unknown")

-----------------------------------------

from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]]
    ) -> Callable[[str], str]:

    file_extension_dict: dict[str, str] = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extension_dict[ext] = tup[0]
    return lambda ext: file_extension_dict.get(ext, "Unknown")
----------------------------

from collections.abc import Iterator

def change_bullet_style(document: str) -> str:
    lines_list = document.split("\n")
    changed_lines: Iterator[str] = map(convert_line, lines_list)
    return "\n".join(list(changed_lines))


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
-----------------------------

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


-----------------------------

from collections.abc import Iterator


def change_bullet_style(document: str) -> str:
    lines_list = document.split("\n")
    changed_lines: Iterator[str] = map(convert_oline, lines_list)
    return "\n".join(list(changed_lines))



def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
-----------------------------

def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))

-----------------------------

def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))

-----------------------------

import functools

def add(sum_so_far: int, x: int) -> int:
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers: list[int] = [1, 2, 3, 4]
sum: int = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10

-----------------------------------

import functools
def add(sum_so_far: int, x: int) -> int:
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers: list[int] = [1, 2, 3, 4]
sum: int = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 2, x: 3
# sum_so_far: 3, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10

----------------------------------

a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[tuple[int, int]] = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]

-----------------------------------

valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pait_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    return list(filter(lambda x: x[1] in valid_formats, zip(doc_names, doc_formats)))

--------------------------------------

def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    return set(
        filter(
            lambda doc: doc not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups)
        )
    )

---------------------------------------

from collections.abc import Iterator

def change_bullet_style(document: str) -> str:
    lines_list = document.split("\n")
    changed_lines: Iterator[str] = map(convert_line, lines_list)
    return "\n".join(list(changed_lines))

# Don't chagne below this line

def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bulle + line[1]
    return line

----------------------------------------
# CH3: Pure Functions
# Reference vs. Value
# Example of Pass-By-Reference

def modify_list(inner_lst: list[int]) -> None:
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst: list[int] = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]

--------------------------------------
# Example of Pass-By-Value

def attempt_to_modify(inner_num: int) -> None:
    inner_num: += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num: int = 1
attempt_to_modify(outer_num)
# outer_num = 1

------------------------------------

def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    default_formats = default_formats.copy()
    default_formats[new_format] = True
    return default_formats


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    default_formats = default_formats.copy()
    default_formats[old_format] = False
    return defautl_formats

----------------------------------------------

def sort_dates(dates: list[str]) -> list[str]:
    return sorted(dates, key=format_date)


def format_date(date: str) -> str:
    month, day, year = date.split("-")
    return year + month + day

------------------------------------------

def format_date(date: str) -> str:
    month, day, year = date.split("-")
    return year + month + day

def sort_dates(dates: list[str]) -> str:
    return sorted(dates, key=format_date)

-------------------------------------
# Recursion
-------------------------------------

def sum_nums(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15

-------------------------------------

def sum_nums(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    return num[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
--------------------------------------

def factorial_r(x: int) -> int:
    if x <= 1:
        return 1
    return x * factorial_r(x - 1)

----------------------------------

def print_chars(word: str, i: int) -> None:
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("Hello", 0)
# H
# e
# l
# l
# o

-----------------------------------------------------

def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    # 1. Base case: If either list is empty, return an empty dictionary
    if not keys or not values:
        return{}

    # 2. Recursive step: Call zipmap on everything except the first elements
    zipped: dict[str, float] = zipmap(keys[1:], values[1:])

    # 3. Add the first key and value to the resulting dictionary
    zipped[keys[0]] = values[0]

    # 4. Return the updated dictionary
    return zipped

---------------------------------------------------------------


