from SolveMethods import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt

c = 3
d = 4
N = 900 + 10*c + d
#print(matrix.GetDiagonal())

# A
e = 8
f=4
a1 = 5 + e
a2 = -1
a3 = a2
b = Matrix(N,1)
b.SetSinValues(f)
matrix = Matrix(N,N)
matrix.SetDiagonal(a1, a2, a3)


# B
print("B")
start = timer()
solution,iterations=Gauss(matrix,b)
end = timer()
print("Gauss:",iterations,"Time:",end - start)

start = timer()
solution,iterations=Jacoby(matrix,b)
end = timer()
print("Jacoby:",iterations,"Time:",end - start)



# C
print("C")
a1=3
a2=-1
a3=-1
N = 900 + 10*c + d
matrix = Matrix(N,N)
matrix.SetDiagonal(a1, a2, a3)

#limit iteracji 400
solution,iterations=Gauss(matrix,b)
print("Gauss:",iterations)
solution,iterations=Jacoby(matrix,b)
print("Jacoby:",iterations)
#wniosek nie zbiegają się!



#d
print("D")
matrix = Matrix(N,N)
matrix.SetDiagonal(a1, a2, a3)
solution=LU(matrix,b)
print("norm=",(matrix*solution-b).GetNorm())

#E


e = 8
f=4
a1 = 5 + e
a2 = -1
a3 = a2
N=[100,500,1000,2000,3000]

GaussTime=[]
JacobyTime=[]
LUTime=[]
for n in N:
    print("n:",n)
    #setup
    matrix = Matrix(n,n)
    matrix.SetDiagonal(a1, a2, a3)
    b = Matrix(n, 1)
    b.SetSinValues(f)

    #pomiary

    start = timer()
    Gauss(matrix,b)
    end = timer()

    GaussTime.append(end-start)

    start = timer()
    Jacoby(matrix, b)
    end = timer()

    JacobyTime.append(end - start)

    start = timer()
    LU(matrix, b)
    end = timer()

    LUTime.append(end - start)


#wyrysowanie:

plt.semilogy(N,GaussTime,label = "Gauss")
plt.semilogy(N,JacobyTime,label = "Jacoby")
plt.semilogy(N,LUTime,label = "LU")
plt.xlabel("matrix size")
plt.ylabel("time [s]")
plt.title("Methods solving time")

plt.legend()
plt.show()


