import json
from collections import OrderedDict

# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
#firms = OrderedDict(json.loads(input()))

# your code here
square_list = []
for i in range(1, 10):
    if i % 2 == 0:
        square_list.append(i ** 2)
print(square_list)
print([i ** 2 for i in range(1,10) if i % 2 == 0])