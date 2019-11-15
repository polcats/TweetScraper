from scraper import *
from input import *

def do_action(inp):
	if inp == 0:
		exit()
	elif inp == 1:
		scraper_start()
	else:
		print("Invalid input.")

def print_actions():
	print("\n")
	print("0. Exit")
	print("1. Scrape Twitter")

while True:
	print_actions()
	do_action(get_input("Please choose what to do: ", min = 0, max = 1))



