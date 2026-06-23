agent = {'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
#sec 2
print(agent['name'])
# sec 3
level=agent.get("level")
print(level)
print(agent.get(0))
#sec 4
agent["score"]=95
print(agent)
#sec 5
agent['level']=5
print(agent)
#sec 6
del agent['active']
print(agent)
print(agent.keys())
print(agent.values())
print(agent.items())