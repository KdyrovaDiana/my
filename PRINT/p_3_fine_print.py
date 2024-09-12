from pprint import pprint as pp

# 42
print(42)
# 43
pp(43)
# 'Hello'
pp('Hello')
# Hello
print('Hello')

# {'power': [0,
#            1,
#            1024,
#            59049,
#            1048576,
#            9765625,
#            60466176,
#            282475249,
#            1073741824,
#            3486784401]}
data = {'power': [x**10 for x in range(10)]}
pp(data)

# {'USA': {'Texas': {'Dalas': [...]}}}
cities = {'USA': {'Texas': {'Dalas': ['Irving']}}}
pp(cities, depth=3)

items = [1, 2, 3]
items.append(items)
print(items)
# [1, 2, 3, [...]]
pp(items)
# [1, 2, 3, <Recursion on list with id=128366948787712>]
print(id(items))
# 134666099924992


import reprlib
reprlib.repr([x**10 for x in range(10)])


