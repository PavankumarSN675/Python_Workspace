
list = [1,2,2,3,4,5,6,5,1]

output = []

counter = 1
for i in range(0, len(list)):
    ele = list[i]
    for j in range(i+1, len(list)):
        if ele == list[j]:
            counter = counter + 1
    print(counter)
    if counter == 1:
        output.append(list[i])
    counter = 1
print(output)