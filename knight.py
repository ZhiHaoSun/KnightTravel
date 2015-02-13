size=int(input("Enter the size of the square board:"))
board=[]
start=(int(input("Enter the start X start from (0,0):")),int(input("Enter start Y:")))
steps=[(start[0],start[1],0)]

print("The steps to get every point on the board is as follows:")

for i in range(size):
    board.append([])
    for j in range(size):
        board[i].append(999)

board[start[0]][start[1]]=0

def judge(x,y,s):
    if board[x][y]>s+1:
        board[x][y]=s+1
        steps.append((x,y,s+1))

while len(steps)>0:
    temp=steps[-1]
    x=temp[0]
    y=temp[1]
    s=temp[2]
    steps=steps[:-1]
    
    if x>1:
        if y>0:
            judge(x-2,y-1,s)
        if y<size-1:
            judge(x-2,y+1,s)
    if x<size-2:
        if y>0:
            judge(x+2,y-1,s)
        if y<size-1:
            judge(x+2,y+1,s)
    if x>0:
        if y>1:
            judge(x-1,y-2,s)
        if y<size-2:
            judge(x-1,y+2,s)
    if x<size-1:
        if y>1:
            judge(x+1,y-2,s)
        if y<size-2:
            judge(x+1,y+2,s)

for i in range(size):
    for j in range(size):
        print("{:4d}".format(board[i][j]),end='')
    print()

print()
target=(int(input("Enter your target positionX:")),int(input("Enter targetY:")))

def routeToTarget(target):
    
    x=target[0]
    y=target[1]

    if board[x][y]==1:
        print(target,"->",start)
        return
    
    neighbours=[(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]

    for point in neighbours:
        if size>point[0]>=0 and size>point[1]>=0 and board[point[0]][point[1]]==board[x][y]-1:
            print(target,end="->")
            routeToTarget(point)
routeToTarget(target)
    
