limit = int(input("Digite o número de linhas: "))
space = ""
position = 0
times = 0

for x in range(0,limit,1):
    space += " "
    position += 1
    print(space, end="")
    print("#")
    times += 1
    if position == 5:
        for x in range(0,5,1):
            space = space.replace(" ", "",1)
            position -=1
            times += 1
            print(space, end="")
            print("#")
    if times == limit:
        break
