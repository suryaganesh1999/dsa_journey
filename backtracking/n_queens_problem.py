#Checking if a position is safe or not
def is_safe(mat, r, c):
    #Checking Q in same column
    for row in range(r-1,-1,-1):
        if mat[row][c]=='Q':
            return False
    #Checking Q in right diagonal
    row, col=r,c
    while(row>=0 and col<N):
        if mat[row][col]=='Q':
            return False
        row-=1
        col+=1
    row, col=r,c
    while(row>=0 and col>=0):
        if mat[row][col]=='Q':
            return False
        row-=1
        col-=1
    return True
def print_mat(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print()
        print()
def n_queens(mat, r):
    if r==N:
        print('Possible Arrangement of Queens: ')
        print_mat(mat)
        return 
    for c in range(0,N):
        if is_safe(mat, r, c):
            mat[r][c]='Q'
            n_queens(mat, r+1)
            mat[r][c]='-'
while(input()!='stop'):
    N=int(input())
    mat=[['-' for i in range(N)] for i in range(N)]
    n_queens(mat,0)
