import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra, bellman_ford,floyd_warshall,depth_first_order,breadth_first_order

from scipy.sparse import csr_matrix

arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(connected_components(arr1))    #op- (1, array([0, 0, 0]))

# Djkstra method- used to find the shortest path from 1 element to another element

arr = np.array([[0,1,2],[1,0,0],[2,1,0]])
arr2=csr_matrix(arr)
print(dijkstra(arr2,return_predecessors=True,indices=0))

# belman ford handles Negative elements as well
arr3 = np.array([[0,-1,-2],[1,0,0],[2,1,0]])
arr4=csr_matrix(arr3)
print(bellman_ford(arr4,return_predecessors=True,indices=0))


# floyd-warshall-> used to give shrtest path between pair of element

print(floyd_warshall(arr4,return_predecessors=True))

# depth first order-> used to give depth first traversal. it takes 2 arguments graph, starting point

arr5=np.array([[1,0,1,1],[1,1,1,1],[1,0,1,0],[1,1,1,1]])
near=csr_matrix(arr5)
print(depth_first_order(near,1))


# breadth first - > used to give breadth first traversal, it takes 2 arge- graph and starting point

print(breadth_first_order(near,1))