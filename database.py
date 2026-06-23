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
#sec 7
print(agent.keys())
print(agent.values())
print(agent.items())
#sec 8
if "score" in agent:
    print("yes")
#sec 9
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
print(max(scores.values()))
#sec 10
agent2=agent.copy()
agent2["level"]=4
print(agent2,agent)

