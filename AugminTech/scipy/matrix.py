
import numpy as np
from scipy.sparse import csr_matrix


# Sparse Data  - Holds most of the zero(0) values

# create csr matrix

arr = np.array([0,0,0,0,0,1,0,2])
print(csr_matrix(arr))
'''o/p
(0, 5)	1    -> 0 row 5th index col , val is 1
  (0, 7)	2    -> 0 row 7th index col, val is 2
'''


arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr1).data)   #[1 1 2]  o/p - non zero data

# Non zero values
print(csr_matrix(arr1).count_nonzero())    #o/p - 3

# eliminate zero values
mat=csr_matrix(arr1)
mat.eliminate_zeros()
print(mat)

'''o/p-   non zero values after eliminating zero's with row and col index
  (1, 2)	1
  (2, 0)	1
  (2, 2)	2
'''
# with sum_duplicate() method

mat.sum_duplicates()
print(mat)
'''o/p-   non zero values after eliminating zero's with row and col index
  (1, 2)	1
  (2, 0)	1
  (2, 2)	2
'''


# convert csr matrix to csv using tocsc() method

newarr=csr_matrix(arr1)
newarr.tocsc()
print(newarr)
'''o/p-   non zero values after eliminating zero's with row and col index
  (1, 2)	1
  (2, 0)	1
  (2, 2)	2
'''
