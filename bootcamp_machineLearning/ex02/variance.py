# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variance.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 15:58:54 by jdussert          #+#    #+#              #
#    Updated: 2020/01/20 16:44:08 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
 
def variance(x):
	"""Computes the variance of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The variance as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
	m = float(len(x))
	if m == 0:
		return None
	mean_x = 0
	variance_x = 0
	for nb in x:
	   mean_x += float(nb)
	mean_x /= m
	for nb in x:
	   variance_x += float((nb - mean_x)**2)
	variance_x /= m
	return variance_x

# Examples :
X = np.array([0, 15, -9, 7, 12, 3, -21])
print("La variance est de :\n", variance(X))
print(np.var(X))
