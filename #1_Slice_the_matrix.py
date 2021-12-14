import numpy as np


matrix2 = [
        list(r"     /"),
        list(r" \  / "),
        list(r"  \/  ")
    ]

matrix1 = [
        list(r"     /"),
        list(r" \  / "),
        list(r"  \   ")
    ]

matrix3 = [
        list(r"\    /"),
        list(r" \  / "),
        list(r"  \/  ")
    ]


def calc(i:int, j:int, n:int, m:int, visited, matrix) -> None:
	if (i>=n or i<0 or j>=m or j<0):
		return
	if(visited[i][j]):
		return

	if (matrix[i][j] !=" "):
		return

	visited[i][j]=1
	calc(i,j-1,n,m,visited,matrix)
	calc(i-1,j,n,m,visited,matrix)
	calc(i,j+1,n,m,visited,matrix)
	calc(i+1,j,n,m,visited,matrix)


def getRegion(matrix)->int:
	r =0
	nrows, ncols = len(matrix), len(matrix[0])
	visited = [[0 for i in range(ncols)] for j in range(nrows)]
	
	for i in range(nrows):
		for j in range(ncols):
			if (  not visited[i][j] and matrix[i][j]==" "):
				calc(i,j,nrows, ncols, visited, matrix)
				r+=1
			else:
				visited[i][j]=1;

	return r







print(getRegion(matrix1))
print(getRegion(matrix2))
print(getRegion(matrix3))
