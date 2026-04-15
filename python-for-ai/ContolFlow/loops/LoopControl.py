#break → stop loop

for i in range(5):
    if i == 3:
        break
    print(i)

print("-"*40)

#continue → skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

#pass → do nothing (placeholder)
for i in range(5):
    pass 

#ELSE WITH LOOPS
for i in range(3):
    print(i)
else:
    print("Loop finished")

#NESTED CONTROL FLOW
for i in range(3):
    for j in range(2):
        print(i, j)

#MATCH-CASE
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")