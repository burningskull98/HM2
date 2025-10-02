from typing import List
def foo(x:list[str]):
    pass



### End ###
foo(["foo", "bar"])
foo(["foo", 1])  # expect-type-error