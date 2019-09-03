m = 4
foo = 0
list_2d = [[foo for i in range(4)] for j in range(4)]
counter = 0
for x in range(m):
    for y in range(m):
        counter =counter+1
        list_2d[x][y] = x
        print(list_2d[x][y],end ="; ")
    print("")

print(list_2d)
