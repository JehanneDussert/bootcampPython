# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:31:22 by jdussert          #+#    #+#              #
#    Updated: 2020/01/16 11:03:01 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def my_list(s):
	lst = s.replace("...", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace(".", " ").replace(";", " ").replace("!", " ").split()
	return lst

def filter_word(s, nb):
	i = 0
	try:
		int(nb)
		a = int(nb)
	except ValueError:
		exit(print("ERROR"))
	try:
		str(s)
		tmp = my_list(s)
		while i < len(tmp):
			if tmp[i].isalpha() == False:
				exit(print("ERROR"))
			if len(tmp[i]) <= a:
				del tmp[i]
			else:
				i += 1
	except ValueError:
		exit(print("ERROR"))
	return tmp
	
if len(sys.argv) == 3:
	print(filter_word(sys.argv[1], sys.argv[2]))
else:
		exit(print("ERROR"))
