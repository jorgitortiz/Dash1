import numpy as np
import math

def Diagonalbanda(A):
    for i in range(len(A)):
        if A[i][0] == 0 or A[0][i] == 0:
            if A[i][0] == 0 and A[0][i] == 0:
                banda = (i*2)-1
                break
            else:
                banda = i*2
                ind = i
                break
    new = np.zeros((len(A), banda))
    if banda % 2 == 0:
        for i in range(len(new)):
            for j in range(len(new[0])):
                index = j-(banda-(math.ceil(banda/2)))+i
                if index >= len(new) or index < 0:
                    new[i][j] = 0
                else:
                    if A[ind][0] == 0:
                        new[i][j] = A[index][i]
                    else:
                        new[i][j] = A[i][index]
    else:
        for i in range(len(new)):
            for j in range(len(new[0])):
                index = j-(banda-(math.ceil(banda/2)))+i
                if index >= len(new) or index < 0:
                    new[i][j] = 0
                else:
                    new[i][j] = A[i][index]

    print(new)

def main():
    #A = np.array([[5., 3., 4., 0., 0., 0.],[2., 4., 1., 6., 0., 0.],[3., 3., 11., 5., 3., 0.],[0., 2., 2., 8., 4., 1.],[0., 0., 5., 1., 5., 2.],[0., 0., 0., 2., 7., 9.]])
    A = np.array([[5., 3., 4., 4., 3., 0.], [2., 4., 1., 6., 2., 1.], [3., 3., 11., 5., 3., 4.], [1., 2., 2., 8., 4., 1.],[1., 2., 5., 1., 5., 2.], [0., 4., 3., 2., 7., 9.]])
    #A = np.array([[5., 0., 0., 0., 0., 0.], [0., 4., 0., 0., 0., 0.], [0., 0., 11., 0., 0., 0.], [0., 0., 0., 4., 0., 0.],[0., 0., 0., 0., 2., 0.], [0., 0., 0., 0., 0., 9.]])
    #A = np.array([[1., -2., 1., 0., 0., 0.,0.,0.],[1., -1., 3., 2., 0., 0.,0.,0.],[0., 5., 3., 4., 1., 0.,0.,0.],[0.,0.,7.,8.,2.,1.,0.,0.],[0., 0., 0., 1., 4., 2.,2.,0.],[0., 0., 0., 0., 3., 1.,3.,3.],[0., 0., 0., 0., 0., 1.,2.,2.],[0.,0.,0.,0.,0.,0.,1.,1]])
    #A = np.array([[7.,1.,0.],[0.,5.,2],[0.,0.,-6]])
    #A = np.array([[7.,0.,0.],[1.,5.,0.],[0.,1.,-6]])
    #A = np.array([[2.,-1.,0.,0.],[-1.,2.,-1,0.],[0.,-1.,2.,-1],[0.,0.,-1.,2]])
    print(A)
    print("")
    Diagonalbanda(A)

if __name__ == "__main__":
    main()
