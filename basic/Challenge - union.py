from typing import Union
def foo(x:Union[str, int]):
    pass




### End ###
foo("foo")
foo(1)

foo([])  # expect-type-error