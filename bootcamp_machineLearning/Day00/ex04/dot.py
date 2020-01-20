# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 16:53:04 by jdussert          #+#    #+#              #
#    Updated: 2020/01/20 19:21:13 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def dot(x, y):
	"""Computes the dot product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have the same dimensions.
    Args:
     x: has to be an numpy.ndarray, a vector.
     y: has to be an numpy.ndarray, a vector.
    Returns:
     The dot product of the two vectors as a float.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	m = len(x)
	n = len(y)
	if m != n or m == 0 or n == 0:
	   return None
	dot_xy = 0
	for nb_x, nb_y in zip(x, y):
		dot_xy += float(nb_x * nb_y)
	return dot_xy

# Examples
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print("Mine : Dot =\n", dot(X, Y))
print("True : Dot =\n", np.dot(X, Y))
