file = open("weapon.txt","r")
i = 1 
for line in file.readlines():
    # print(line.strip())
    if i % 2 == 1 :
        print(line.strip())
    i+=1
    # print(line.strip(),end=" ")