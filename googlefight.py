#! /usr/bin/python3

import kings_battle
from googleapi import Geodata
from game_massages import *
from api_constants import *

""" Battle anywhere with any warriors """

def main():
	print('Choose a place of battle')
	geoquery = Geodata()
	location = input('Please input location: ')
	region = input('and region: ')
	
	win = kings_battle.main()

	if win:
		print('This place is lucky for you, winner: ')
	else:
		print('This place is not lucky for you, loser: ')
	geoquery.get_location(location, region)
	

if __name__ == '__main__':
	main()