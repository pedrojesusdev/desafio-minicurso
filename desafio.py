limit = int(input("Digite o número de linhas: "))
space = ""
position = 0

for x in range(0,limit,1):
    space += " "
    position += 1
    print(space, end="")
    print("#")
    if position == 5:
        while position != 1:
            space = space.replace(" ", "",1)
            position -=1
            print(space, end="")
            print("#")
