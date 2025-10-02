class Foo:
    bar: int


### End ###
foo = Foo()
foo.bar = 1
foo.bar = "1"  # expect-type-error