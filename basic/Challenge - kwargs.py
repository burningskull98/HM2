def foo(**kwargs: int | str):
    ...



### End ###
foo(a=1, b="2")
foo(a=[1])  # expect-type-error