#! /usr/bin/python3

import sys
import random
import csv
from game_massages import *


"""
	Kings Battle is game about war between men and machines.
"""

def check_correct_value(choise_of_option, diapason_of_choice):
	while True:
		if not choise_of_option.isdigit() or not int(choise_of_option) in range(1, diapason_of_choice + 1):
			print('Please, enter the correct value')
			return True
		else:
			return False

class Settings():
	"""Basic messages"""
	@staticmethod
	def hello():
		print(HELLO)
	@staticmethod
	def win():
		print(WIN)
	@staticmethod
	def lose():
		print(LOSE)


class Warrior():
	"""Basic class Warrior"""
	def __init__(self, option, name, power, skill, health):
		self.name = name
		self.power = power
		self.skill = skill
		self.health = health
		self.option = option

	def load_warriors():
		filename = 'warriors.csv'
		with open(filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)
			name_of_warriors, power, health, skill = [], [], [], []
			for row in reader:
				name_of_warriors.append(row[0])
				power.append(int(row[1]))
				health.append(int(row[2]))
				skill.append(float(row[3]))
			print(name_of_warriors)
			print(power)
			print(health)
			print(skill)
			print(header_row)

	def set_warrior(self):
		if self.option == 1:
			self.name = 'strong'
			self.power = int(self.power * 1.5)
		elif self.option == 2:
			self.name = 'healthy'
			self.health = int(self.health * 1.5)
		elif self.option == 3:
			self.name = 'skill'
			self.skill = self.skill * 1.5
		



class Fight(Warrior):
	"""Game function"""
	def __init__(self, option = None, name = '', power = 10, skill = 1.0, health = 100):
		super().__init__(option, name, power, skill, health)

	def get_damage(self):
		return (self.power * self.skill)

	def set_protagonist_kick(self):
		while  True:
			kick = input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
			if not check_correct_value(kick, 3):
				return int(kick)

	def set_protagonist_block(self):
		while True:
			block = input('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')
			if not check_correct_value(block, 3):
				print("your block " + str(block))
				return int(block)

	def set_antagonist_kick(self):
		kick = random.randint(1, 3)
		print('Enimal kick ' + str(kick))
		return kick

	def set_antagonist_block(self):
		return random.randint(1, 3)


def main():
	Settings.hello()
	win = False

	protagonist = Fight()
	while True:
		choise_of_option = input("Please select your warrior: 1 - strong, 2 - healthy, 3 - skill: ")
		if not check_correct_value(choise_of_option, 3):
			protagonist.option = int(choise_of_option)
			protagonist.set_warrior()
			break
	print('Your warrior:', protagonist.name)

	antagonist = Fight()
	antagonist.option = random.randint(1, 3)
	antagonist.set_warrior()
	print('Your antagonist: ', antagonist.name)
	
	while True:
		print('Your warrior HP: ' + str(protagonist.health))
		print('Your antagonist HP: ' + str(antagonist.health))
		print('\n')

		if protagonist.set_protagonist_kick() != antagonist.set_antagonist_block():
			print('You hit an opponent!')
			antagonist.health = antagonist.health - protagonist.get_damage()
		else:
			print('Opponent blocked you!')

		if protagonist.set_protagonist_block() != antagonist.set_antagonist_kick():
			print('Opponent hit you :( ')
			protagonist.health = protagonist.health - antagonist.get_damage()
		else:
			print('You blocked an opponent!')

		if protagonist.health <= 0:
			break

		if antagonist.health <= 0:
			win = True
			break

	Settings.win() if win else Settings.lose()

	return win


if __name__ == '__main__':
	main()