from typing import Final

my_list: Final = []


### End ###
my_list.append(1)
my_list = []  # expect-type-error
my_list = "something else"  # expect-type-error