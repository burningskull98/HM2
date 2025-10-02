from typing import ClassVar


class Foo:
    bar: ClassVar[int]



### End  ###
Foo.bar = 1
Foo.bar = "1"  # expect-type-error
Foo().bar = 1  # expect-type-error