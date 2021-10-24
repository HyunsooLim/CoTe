count = 1

def calcualtion(x,y,d):
    global count, dx, dy
    check = 0
    for i in range(4):
        if matrix[x+dx[i]][y+dy[i]] != 0:
            check += 1

    if check == 4:
        if matrix[x+dx[d-1]][y+dy[d-1]] == 1:#뒷방향이 막혀있으면
            return
        else:
            x += dx[d-1]
            y += dy[d-1]
            calcualtion(x,y,d)
    else:
        if d == 0:
            if matrix[x + dx[d]][y + dy[d]] == 0:
                matrix[x + dx[d]][y + dy[d]] = 2
                x += dx[d]
                y += dy[d]
                d = 3
                count += 1
                calcualtion(x, y, d)
            else:
                d = 3
                calcualtion(x, y, d)
        elif d == 1:
            if matrix[x + dx[d]][y + dy[d]] == 0:
                matrix[x + dx[d]][y + dy[d]] = 2
                x = x + dx[d]
                y = y + dy[d]
                d = 0
                count += 1
                calcualtion(x, y, d)
            else:
                d = 0
                calcualtion(x,y,d)
        elif d == 2:
            if matrix[x + dx[d]][y + dy[d]] == 0:
                matrix[x + dx[d]][y + dy[d]] = 2
                x = x + dx[d]
                y = y + dy[d]
                d = 1
                count += 1
                calcualtion(x, y, d)
            else:
                d = 1
                calcualtion(x,y,d)
        elif d == 3:
            if matrix[x + dx[d]][y + dy[d]] == 0:
                matrix[x + dx[d]][y + dy[d]] = 2
                x = x + dx[d]
                y = y + dy[d]
                d = 2
                count += 1
                calcualtion(x, y, d)
            else:
                d = 2
                calcualtion(x, y, d)

N,M = map(int,input().split())
r,c,direction =map(int,input().split()) # d = 0123 북동남

matrix = [[] for _ in range(N)]
for k in range(N):
    matrix[k] = list(map(int, input().split()))

matrix[r][c] = 2
dx = [0, +1, 0, -1] # 3/0 /1 / 2/
dy = [-1, 0, +1, 0]

a = calcualtion(r,c,direction)
print(count)