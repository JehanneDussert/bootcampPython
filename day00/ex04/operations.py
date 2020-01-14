# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 18:58:05 by jdussert          #+#    #+#              #
#    Updated: 2020/01/13 19:55:41 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) > 3):
	exit(print("""InputError: too many arguments
Usage: python operations.py
Example:
    python operations.py 10 3"""))
else:
	try:
	 x = int(sys.argv[1])
	 y = int(sys.argv[2])
	except ValueError:
	 exit(print("""InputError: only numbers
Usage: python operations.py
Example:
    python operations.py 10 3"""))
	sum_xy = int(x) + int(y)
	product = int(x) * int(y)
	print("Sum:         " + str(sum_xy))
	difference = int(x) - int(y)
	print("Difference: " + str(difference))
	print("Product:     " + str(product))
	if int(x) == 0 or int(y) == 0:
		print("Quotient:    ERROR (div by zero)")
		print("Remainder: ERROR (modulo by zero)")
	else:
		quotient = int(x) / int(y)
		remainder = int(x) % int(y)
		print("Quotient:    " + str(quotient))
		print("Remainder: " + str(remainder))
