# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 17:48:17 by jdussert          #+#    #+#              #
#    Updated: 2020/01/13 17:48:22 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 2):
	exit(print("ERROR"))
else:
	try:
	 nb = int(sys.argv[1])
	except ValueError:
	 exit(print("ERROR"))
	if (nb == 0):
		 exit(print("I'm Zero."))
	elif (nb % 2 == 0):
		 exit(print("I'm Even."))
	else:
		 exit(print("I'm Odd."))

