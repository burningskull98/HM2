from typing import Tuple
def foo(x:tuple[()]):
    pass



### End ###
foo(())
foo((1,))  # expect-type-error