def foo(x: int | None = 0):
    pass



### End ###
foo(10)
foo(None)
foo()

foo("10")  # expect-type-error