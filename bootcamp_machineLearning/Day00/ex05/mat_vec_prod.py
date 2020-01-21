# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_vec_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 19:24:23 by jdussert          #+#    #+#              #
#    Updated: 2020/01/21 17:54:28 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mat_vec_prod(x, y):
	"""Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * 1.
    Returns:
     The product of the matrix and the vector as a vector of dimension m *
1.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
    """
	m = np.shape(x)[0]
	n = np.shape(x)[1]
	if m == 0 or n == 0 or n != np.shape(y)[0]:
		return None
	k = 0
	index = 0
	tab = []
	while k < 1:
		for i in x:
			j = 0
			tmp = 0
			for l in i:
				tmp += i[j] * y[j][k]
				j += 1
			tab.append(tmp)
		k += 1
	tab = np.asarray(tab).reshape(m, 1)
	return tab	

# Examples :
W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
print("My mat_vec_prod :\n", mat_vec_prod(W, X))
