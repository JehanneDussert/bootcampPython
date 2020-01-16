# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/16 13:35:27 by jdussert          #+#    #+#              #
#    Updated: 2020/01/16 14:35:47 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def my_rules():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!")
	print()

def my_guess(nb_to_guess, i):
	nb = input("What's your guess between 1 and 99 ?\n")
	if nb == "exit":
		exit(print("Bye bye"))
	i += 1
	try:
		int(nb)
		int(nb_to_guess)
		if int(nb) < nb_to_guess:
			print("Too low!")
			my_guess(nb_to_guess, i)
		elif int(nb) > nb_to_guess:
			print("Too high!")
			my_guess(nb_to_guess, i)
		elif int(nb) == nb_to_guess:
			print("Congratulations, you've got it!")
			exit(print("You won in " + str(i) + " attempts"))
	except ValueError:
		print("Please, try again and enter a number")
		my_guess(nb_to_guess, i - 1)

my_rules()
nb_to_guess = random.randint(1,99)
my_guess(nb_to_guess, 0)
