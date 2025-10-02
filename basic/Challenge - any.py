from typing import Any

def foo(any)-> None:
    print(foo)


### End ###

foo(1)
foo("10")
foo(1, 2)  # expect-type-error