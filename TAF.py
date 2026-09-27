import numpy as np

#Matrice rayée
M = np.indices((10,10))
M1 = M[1]%2
print(M1)

#Damier
M = np.indices((10,10))
M2 = (M[0] + M[1])%2
print(M2)

#Escalier 2 par 2
M = np.indices((10,10))
M3 = (M[0] + M[1])//2
print(M3)

#Matrice par bloc
M = np.indices((10,10))

print(M)