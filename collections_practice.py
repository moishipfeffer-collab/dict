# #sec 1
# tags = {'python', 'bash', 'git', 'python'}
# print(tags)
# #sec 2
# tags.add("linux")
# print(tags)
# #sec 3
# tags.discard("bash")
# print(tags)
# tags.discard("moishi")
# print(tags)
# #sec 4
# a = {1, 2, 3} 
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# #sec 5
# if "git" in tags:
#     print(True)
# else:
#     print(False)    
# #sec 6
# point = (10, 20)
# print(point)
# print(point[0:2])
# #sec 7
# # point[0]=99
# # print(point)
# #'tuple' object does not support item assignment
# #sec 8
# rgb = (255, 128, 0)
# r=rgb[0]
# g=rgb[1]
# b=rgb[2]
# print(r,g,b)
# #sec 9
# coords = (1, 2, 3, 2, 1)
# print(coords.count(2))
# print(coords.index(1))
# print(coords.index(2))
# print(coords.index(3))
# #sec 10
# list=[1,2,3]
# set={1,2,3}
# tuple=(1,2,3)
# print(list,set,tuple)
#list=index,mutable.tuple=immutable,index.set=no index,no mult.
#part 2 sec 1
a = {1, 2, 3} 
b = {3, 4, 5}
print(a.issubset(b))
print(a.issuperset(b))
#sec 2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(pairs[1][1])
#sec 3
names=["moishi","rachel","moishi"]
print(set(names))
print(list(names))
#sec 4
number={1,2,3}
addr={1,2,3,4}
print(addr.symmetric_difference(number))
# sec 5
#just primitive values can be added to set
me={"moishi","rachel"}
you=["moishi","rachel"]
he=("moishi","rachel")
me.add(he)
print(me)
