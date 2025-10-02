from typing import Tuple
def foo(x:tuple[str, int]):
    pass


### End ###
foo(("foo", 1))

foo((1,2))  # expect-type-error
foo(("foo", "bar"))  # expect-type-error
foo((1, "foo"))  # expect-type-error