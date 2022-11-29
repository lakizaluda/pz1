import numpy as np

a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])

#  [ 1  6]
#  [ 2  8]
#  [ 3 11]
#  [ 3 10]
#  [ 1  7]
print(a.shape)

mean_a = a.mean(axis=0)
print(mean_a)

a_centered = a - mean_a
print(a_centered, a_centered.shape)

N = a.shape[0] - 1
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1]) / N
print(a_centered_sp)

print(np.cov(a.T))
