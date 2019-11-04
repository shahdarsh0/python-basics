bubble=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]
i=0
highest=0
length=len(bubble)
solutions=[]
length=len(bubble)
while i<length:
    bubble_string="Bubble Solution #"+str(i)
    print(bubble_string,"score:",bubble[i])
    if(highest<=bubble[i]):
        highest=bubble[i]
        
    i=i+1

for i in range(length):
    if(highest==bubble[i]):
        solutions.append(i)


print("Bubble Tests",length)
print("Highest Bubble Score",highest)
print("Solution with highest score",solutions)
