a = [1,1,2,2]
result={}
re = 0
answer = 0
for i in a:
    if i in result:
        result[i] += 1 
    else:
        result[i] = 1


for i in result:
    if result[i] > re:
        answer = i
        re = result[i]
    elif result[i] == re:
        answer = -1

print(answer)