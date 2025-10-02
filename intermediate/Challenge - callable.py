from collections.abc import Callable

SingleStringInput = Callable[[str], None]


### End  ###
def accept_single_string_input(func: SingleStringInput) -> None:
    ...


def string_name(name: str) -> None:
    ...


def string_value(value: str) -> None:
    ...


def int_value(value: int) -> None:
    ...


def new_name(name: str) -> str:
    return name


accept_single_string_input(string_name)
accept_single_string_input(string_value)
accept_single_string_input(int_value)  # expect-type-error
accept_single_string_input(new_name)  # expect-type-error