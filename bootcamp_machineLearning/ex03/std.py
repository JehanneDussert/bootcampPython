# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    std.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 16:44:22 by jdussert          #+#    #+#              #
#    Updated: 2020/01/20 16:52:43 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import math

def std(x):
	"""Computes the standard deviation of a non-empty numpy.ndarray, using a
for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The standard deviation as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
	m = float(len(x))
	if m == 0:
		return None
	mean_x = 0
	variance_x = 0
	std_x = 0
	for nb in x:
	   mean_x += float(nb)
	mean_x /= m
	for nb in x:
	   variance_x += float((nb - mean_x)**2)
	variance_x /= m
	std_x = math.sqrt(variance_x)
	return std_x

X = np.array([0, 15, -9, 7, 12, 3, -21])
print("Mine : Racine carree :\n", std(X))
print("True : Racine carree :\n", np.std(X))
