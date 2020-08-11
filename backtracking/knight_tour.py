import time as t 
def is_safe(mat,r,c):
    if r>=0 and c>=0 and r<N and c<N:
        if mat[r][c]==0:
            return True
    return False
def different_initial_points(mat):
    for i in range(N):
        for j in range(N):
            mat[i][j]=c
            from_source(mat, i, j)
            mat[i][j]=0
    print('Enter New Input:')
def print_mat(mat):
    print('New Pos')
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print()
    print()
def from_source(mat, i, j):
    global c
    if c==N*N:
        print_mat(mat)
        return
    all_possible_positions=[
        (i+1, j+2), (i+1, j-2), (i+2, j+1), (i+2, j-1),
        (i-1, j+2), (i-1, j-2), (i-2, j-1), (i-2, j+1)
        ]
    for row, col in all_possible_positions:
        if is_safe(mat, row, col):
            c+=1
            mat[row][col]=c
            from_source(mat, row, col)
            mat[row][col]=0
            c-=1
c=1
while(input()!='N'):
    N=int(input())
    print(N)
    mat=[[0 for i in range(N)] for i in range(N)]
    different_initial_points(mat)
