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
    changed_lines: Iterator[str] = map(convert_oline, lines_list)
    return "\n".join(list(changed_lines))



def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
-----------------------------





