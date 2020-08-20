def get_possible_positions(mat, visited, r, c):
    pos_list=[]

    #r-1, c
    if r-1>=0:
        if visited[r-1][c]==0 and mat[r-1][c]==1:
            pos_list.append((r-1, c))
    #r+1, c
    if r+1<R:
        if visited[r+1][c]==0 and mat[r+1][c]==1:
            pos_list.append((r+1, c))

    #r, c+1
    if c+1<C:
        if visited[r][c+1]==0 and mat[r][c+1]==1:
            pos_list.append((r, c+1))

    #r, c-1
    if c-1>=0:
        if visited[r][c-1]==0 and mat[r][c-1]==1:
            pos_list.append((r, c-1))

    return pos_list


dists=set()
def from_source(visited, mat, r, c):
    global dists
    global distance
    if r==d_r and c==d_c:
        dists.add(distance)
        return

    go_to=get_possible_positions(mat, visited, r, c)

    for pos in go_to:
        r=pos[0]
        c=pos[1]
        distance+=1
        visited[r][c]=1
        from_source(visited, mat, r, c)
        distance-=1
        visited[r][c]=0
distance=1

#reading source
s_r, s_c=map(int,input().split())
d_r, d_c=map(int,input().split())

mat = [
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]
R=len(mat)
C=len(mat[0])
visited=[[0 for i in range(C)] for j in range(R)]
visited[s_r][s_c]=1
from_source(visited, mat, s_r, s_c)
print(dists)    
