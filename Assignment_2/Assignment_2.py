import numpy as np

def transpose(X): 
    result = np.zeros((np.shape(X)[1], np.shape(X)[0]))
    
    for i in range(np.shape(X)[0]):
        for j in range(np.shape(X)[1]):
            result[j][i] = X[i][j]
    return result

# 1) A = np.array([[5],[1/2],[-1]])      
A = np.array([[5],[1/2],[-1]])  
A_t=transpose(A)

print("Transpose of matrix A is")
for i in range(np.shape(A)[1]):
    for j in range(np.shape(A)[0]):
        print(A_t[i][j], " ", end='')
    print() 

# 2) B = np.array([[1,-1],[2,3]])      
B = np.array([[1,-1],[2,3]])  
B_t=transpose(B)

print("Transpose of matrix B is")
for i in range(np.shape(B)[1]):
    for j in range(np.shape(B)[0]):
        print(B_t[i][j], " ", end='')
    print()   

# 3) C = np.array([[-1,5,6],[pow(3,0.5),5,6],[2,3,-1]])       
C = np.array([[-1,5,6],[pow(3,0.5),5,6],[2,3,-1]])  
C_t=transpose(C)

print("Transpose of matrix C is")
for i in range(np.shape(C)[1]):
    for j in range(np.shape(C)[0]):
        print(C_t[i][j], " ", end='')
    print()   