# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mean.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 15:14:12 by jdussert          #+#    #+#              #
#    Updated: 2020/01/20 16:40:20 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean(x):
	"""Computes the mean of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The mean as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
	m = len(x)
	if m == 0:
	   return None
	mean_x = 0
	for nb in x:
		mean_x += float(nb)
	mean_x /= m
	return mean_x

# Examples :
X = np.array([0, 15, -9, 7, 12, 3, -21])
print("La moyenne est de :\n" + str(mean(X)))
X = np.array([0, 15, -9, 7, 12, 3, -21])
print("La moyenne est de :\n" + str(mean(X ** 2)))
