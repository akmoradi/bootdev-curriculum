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



