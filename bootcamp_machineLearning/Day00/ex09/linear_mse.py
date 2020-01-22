# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_mse.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/22 11:04:59 by jdussert          #+#    #+#              #
#    Updated: 2020/01/22 13:58:39 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def dot(x, y):
	m = len(x)
	n = len(y)
	if m != n or m == 0 or n == 0:
	   return None
	dot_xy = 0
	for nb_x, nb_y in zip(x, y):
		dot_xy += float(nb_x * nb_y)
	return dot_xy

def linear_mse(x, y, theta):
	"""Computes the mean squared error of three non-empty numpy.ndarray,
using a for-loop. The three arrays must have compatible dimensions.
    Args:
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     x: has to be an numpy.ndarray, a matrix of dimesion m * n.
     theta: has to be an numpy.ndarray, a vector of dimension n * 1.
    Returns:
     The mean squared error as a float.
     None if y, x, or theta are empty numpy.ndarray.
     None if y, x or theta does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	len_x = np.shape(x)
	len_y = np.shape(y)
	m = np.shape(x)[0]
	n = np.shape(x)[1]
	if m == 0 or n == 0 or m != np.shape(y)[0] or n != np.shape(theta)[0]:
		return None
	res = 0
	for i in range(m):
		res += (dot(theta, x[i]) - y[i])**2
	res /= float(m)
	return res

# Examples :
X = np.array([
	    [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print("My linear_mse :\n", linear_mse(X, Y, Z))
