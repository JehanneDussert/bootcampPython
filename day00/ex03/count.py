# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 17:48:02 by jdussert          #+#    #+#              #
#    Updated: 2020/01/13 18:50:03 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(text=""):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	i = 0
	upper_l = 0
	lower_l = 0
	spaces = 0
	marks = 0
	str_len = len(text)
	print("The text contains " + str(str_len) + " characters :")
	while (i < str_len):
		if text[i].islower() == True:
			upper_l += 1
		elif text[i].isupper() == True:
			lower_l += 1
		elif text[i] == ' ':
			spaces += 1
		else:
			marks += 1
		i += 1
	print("- " + str(upper_l) + " upper letters")
	print("- " + str(lower_l) + " lower letters")
	print("- " + str(marks) + " punctuation marks")
	print("- " + str(spaces) + " spaces")
	
