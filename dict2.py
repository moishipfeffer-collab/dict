# sec 1
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
print(d1.pop("a"))
print(d1)
# sec 4
nested = {'server': {'host': 'localhost', 'port': 8080}}
print(nested["server"]["port"])
# sec 5
items = ['a', 'b', 'a', 'c', 'b', 'a']
freq={}
freq["a"]=items.count("a")
freq["b"]=items.count("b")
freq["c"]=items.count("c")
print(freq)
