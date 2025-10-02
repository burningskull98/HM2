def foo(x:dict[str, str]):
    pass


### End ###
foo({"foo": "bar"})
foo({"foo": 1})  # expect-type-error