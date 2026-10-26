maze=[
    [0,1,0,0],
      [0,0,0,1],
      [1,0,1,0],
      [0,0,0,0]
]

row=len(maze)
col=len(maze[0])

visited=set()
path=[]

def dfs(x,y):
    if x<0 or x>=row or y<0 or y>=col:
        return False
    if maze[x][y]==1:
        return False
    if (x,y) in visited:
        return False

    visited.add((x,y))
    path.append((x,y))

    if x==row-1 and y==col-1:
        return True

    if dfs(x+1,y):
        return True
    
    if dfs(x-1,y):
        return True
    
    if dfs(x,y+1):
        return True
    
    if dfs(x,y-1):
        return True
    
    path.pop()
    return False

if dfs(0,0):
    print("Path Found!")
    print("Path:",path)
else:
    print("NO path Found!")