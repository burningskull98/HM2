def add[T: int](a: T) -> T:
    ...


### End ###
from typing import assert_type


class MyInt(int):
    pass


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)  # expect-type-error
add(["1"], ["2"])  # expect-type-error
add("1", 2)  # expect-type-error