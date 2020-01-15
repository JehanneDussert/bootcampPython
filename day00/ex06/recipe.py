# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 12:06:08 by jdussert          #+#    #+#              #
#    Updated: 2020/01/15 15:46:56 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {"sandwich": {'ingredients' : 'ham, bread, cheese and tomatoes', 'type of meal' : 'lunch', 'prep_time' : '10'},
		"cake" : {'ingredients' : 'flour, sugar and eggs', 'type of meal' : 'dessert', 'prep_time' : '60'},
		"salad": {'ingredients' : 'avocado, arugula, tomatoes and spinach', 'type of meal' : 'lunch', 'prep_time' : '15'}
	}

def my_choice():
	j = 4
	print("1" + ": Add a recipe")
	print("2" + ": Delete a recipe")
	print("3" + ": Print a recipe")
	print("4" + ": Print the cookbook")
	print("5" + ": Quit")
	rep = input("Please select an option by typing the corresponding number:\n")
	if rep.isdigit() == True:
		if rep == "1":
			add_it(j)
			j += 1
			my_choice()
		elif rep == "2":
			print("Please, delete a recipe :")
			delete_it(input)
			j -= 1
			my_choice()
		elif rep == "3":
			print_it()
			my_choice()
		elif rep == "4":
			print("\nHere is the cookbook :")
			for items in cookbook:
				print("- %s" %items)
			print("")
			my_choice()
		if rep == "5":
			exit(print("Cookbook closed."))
		else:
			print("\n[WARNING]\n\nWrong choice, please try again")
			my_choice()
	else:
		print("\n[WARNING]\n\nWrong choice, please try again")
		my_choice()

def add_it(j):
	new = input("Please, enter the name of the meal :\n")
	cookbook[new] = {}
	cookbook[new]['ingredients'] = input("Please, enter your ingredients :\n")
	cookbook[new]['type of meal'] = input("What is the type of the meal ?\n")
	cookbook[new]['prep_time'] = input("How long does it take to cook it ?\n")

def delete_it(j):
	old = input("Please, enter the name of the meal to delete :\n")
	del cookbook[old]

def print_it():
	to_print = input("Which recipe do you want to print ?\n")
	print(to_print + "'s ingredients are " + str(cookbook[to_print]['ingredients']) + ". It is a " + str(cookbook[to_print]['type of meal']) + " and it takes " + str(cookbook[to_print]['prep_time']) + " minutes of preparation.\n")

my_choice()
