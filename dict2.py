config = {}
config.setdefault("timeout",30)
print(config)
config.setdefault("timeout",31)
print(config)
#sec 2
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = (d1 | d2)
print(d3)
#sec 3
