# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_mat_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 18:46:57 by jdussert          #+#    #+#              #
#    Updated: 2020/01/21 19:39:40 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mat_mat_prod(x, y):
	"""Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * p.
    Returns:
     The product of the matrices as a matrix of dimension m * p.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
"""
	m = np.shape(x)[0]
	n = np.shape(x)[1]
	p = np.shape(y)[1]
	i = 0
	tmp = 0
	tab = []
	if m == 0 or n == 0 or p == 0 or n != np.shape(y)[0]:
		return None
	while i < p:
		for k in x:
			tmp = 0
			l = 0
			for t in k:
				tmp += k[l] * y[l][i]
				l += 1
			tab.append(tmp)
		i += 1
	tab = np.asarray(tab).reshape(m, p)
	return np.transpose(tab)

W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
Z = np.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])
print("My mat_mat_prod :\n", mat_mat_prod(W, Z))
