import numpy as np

def Diagonalbanda(A,B):
    log1 = True
    log2 = True
    for i in range(len(A)):
        if A[i][0] == 0 and A[0][i] == 0 and log1 and log2:
            p = i
            q = i
            break
        else:
            if A[i][0] == 0 and log1:
                p = i
                log1 = False
            elif A[0][i] == 0 and log2:
                q = i
                log2 = False
    new = np.zeros((len(A), p+q-1))
    for row in range(len(new)):
        for col in range(len(new[0])):
            index = col- p + row + 1
            if index >= len(new) or index < 0:
                new[row][col] = 0
            else:
                new[row][col] = A[row][index]
    print(new)
    print("")

    for k in range(len(new)-1):
        for i in range(k + 1,p + k):
            if i < len(new):
                new[i][p+k-i-1] = new[i][p+k-i-1]/new[k][p-1]
                for j in range(p,len(new[0])):
                    new[i][j-i+k] = new[i][j-i+k] - new[i][p+k-i-1] * new[k][j]
                B[i] = B[i] - new[i][p+k-i-1] * B[k]

    for i in range(len(new)-1,-1,-1):
        for j in range(p,len(new[0])):
            if i+j-p+1 <= len(new)-1:
                B[i] = B[i] - new[i][j] * B[j+i-p+1]
        B[i] = B[i] / new[i][p-1]

    print("Solution:")
    print(B)
    print("")

def main():
    A={0:[],1:[],2:[],3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
    B={0:[],1:[],2:[],3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
    A[0] = np.array([[1., -2., 1., 1., 0., 0.,0.,0.],[1., -1., 3., 2., 1., 0.,0.,0.],[0., 5., 3., 4., 1., 1.,0.,0.],[0.,0.,7.,8.,2.,1.,1.,0.],[0., 0., 0., 1., 4., 2.,2.,1.],[0., 0., 0., 0., 3., 1.,3.,3.],[0., 0., 0., 0., 0., 1.,2.,2.],[0.,0.,0.,0.,0.,0.,1.,1]])
    B[0] = np.array([[31.], [32.], [15.], [13.], [23.], [13.], [41.], [21.]])
    A[1] = np.array([[5., 3., 4., 0., 0., 0.],[2., 4., 1., 6., 0., 0.],[3., 3., 11., 5., 3., 0.],[0., 2., 2., 8., 4., 1.],[0., 0., 5., 1., 5., 2.],[0., 0., 0., 2., 7., 9.]])
    B[1] = np.array([[31.], [32.], [15.], [13.], [23.], [13.]])
    A[2] = np.array([[5., 3., 4., 4., 3., 0.],[2., 4., 1., 6., 2., 1.], [3., 3., 11., 5., 3., 4.], [1., 2., 2., 8., 4., 1.],[1., 2., 5., 1., 5., 2.], [0., 4., 3., 2., 7., 9.]])
    B[2] = np.array([[31.], [32.], [15.], [13.], [23.], [13.]])
    A[3] = np.array([[5., 0., 0., 0., 0., 0.],[0., 4., 0., 0., 0., 0.], [0., 0., 11., 0., 0., 0.], [0., 0., 0., 4., 0., 0.],[0., 0., 0., 0., 2., 0.], [0., 0., 0., 0., 0., 9.]])
    B[3] = np.array([[31.], [32.], [15.], [13.], [23.], [13.]])
    A[4] = np.array([[1., -2., 1., 0., 0., 0.,0.,0.],[1., -1., 3., 2., 0., 0.,0.,0.],[0., 5., 3., 4., 1., 0.,0.,0.],[0.,0.,7.,8.,2.,1.,0.,0.],[0., 0., 0., 1., 4., 2.,2.,0.],[0., 0., 0., 0., 3., 1.,3.,3.],[0., 0., 0., 0., 0., 1.,2.,2.],[0.,0.,0.,0.,0.,0.,1.,1]])
    B[4] = np.array([[31.], [32.], [15.], [13.], [23.], [13.], [41.], [21.]])
    A[5] = np.array([[1., -2., 0., 0., 0., 0.,0.],[1., -1., 3., 0., 0.,0.,0.],[2., 5., 0., 0., 0.,0.,0.],[0.,-4.,-2.,1.,4.,0.,0.],[0., 2., 2., 1., 3.,1.,0.],[0., 0., -1., 2., -3., 0.,3.],[0., 0., 0., 3., 3., -1.,1.]])
    B[5] = np.array([[31.], [32.], [15.], [13.], [23.], [13.], [41.]])
    A[6] = np.array([[7.,1.,0.],[0.,5.,2.],[0.,0.,-6]])
    B[6] = np.array([[31.], [32.], [15.]])
    A[7] = np.array([[7.,0.,0.],[1.,5.,0.],[0.,1.,-6]])
    B[7] = np.array([[31.], [32.], [15.]])
    A[8] = np.array([[2.,-1.,0.,0.],[-1.,2.,-1,0.],[0.,-1.,2.,-1],[0.,0.,-1.,2]])
    B[8] = np.array([[31.], [32.], [15.],[34.]])

    for i in range(8):
        print('\n%s) Matrix:\n%s\n' % (i, A[i]))
        print("->Banded Matrix:")
        Diagonalbanda(A[i],B[i])

if __name__ == "__main__":
    main()
