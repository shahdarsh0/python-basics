costs=[.25,.27,.25,.25,.25,.25,.33,.31,.25,.29,.27,.22,.31,.25,.25,.33,.21,.25,.25,.25,.28,.25,.24,.22,.20,.25,.30,.25,.24,.25,.25,.25,.27,.25,.26,.29]
scores=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]
i=0
highscore=0
length=len(scores)
length_cost=len(costs)

bestsolution=[]


for i in range(length):
    if highscore<scores[i]:
        highscore=scores[i]
print("Highscore is:", highscore)


for i in range(length):
    if highscore==scores[i]:
        bestsolution.append(i)

print("Best solution:",bestsolution)

cost=100.0
most_effective=0

"""for i in range(length_cost):
    if scores[i]==highscore and costs[i] < cost:
        most_effective=i
        cost=costs[i]
        
print("Solution",most_effective,"is",costs[most_effective]) 
"""

for i in range(len(bestsolution)):
    index = bestsolution[i]
    if cost>costs[index]:
        most_effective=index
        cost=costs[index]
        
print("Solution",most_effective,"is",costs[most_effective]) 



