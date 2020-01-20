# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sum.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 13:47:32 by jdussert          #+#    #+#              #
#    Updated: 2020/01/20 15:07:32 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sum_(x, f):
	"""Computes the sum of a non-empty numpy.ndarray onto wich a function is
applied element-wise, using a for-loop.
	Args:
     x: has to be an numpy.ndarray, a vector.
     f: has to be a function, a function to apply element-wise to the
vector.
    Returns:
     The sum as a float.
     None if x is an empty numpy.ndarray or if f is not a valid function.
    Raises:
     This function should not raise any Exception.
	"""
	nb_sum = 0
	for nb in x:
		nb_sum += f(float(nb))
	return nb_sum

#Examples :
X = np.array([0, 15, -9, 7, 12, 3, -21])
print("La somme est :\n" + str(sum_(X, lambda x: x)))
X = np.array([0, 15, -9, 7, 12, 3, -21])
print("La somme est :\n" + str(sum_(X, lambda x: x**2)))
