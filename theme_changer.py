import random
from properties import VS_DARK, VS_LIGHT, LC_DARK, LC_LIGHT, OL_DARK, OL_LIGHT

def change_theme(option, switcher):
	if option == 'vs':
		if switcher == 'd':
			select(VS_DARK)
		else:
			select(VS_LIGHT)

	elif option == 'lc':
		if switcher == 'd':
			select(LC_DARK)
		else:
			select(LC_LIGHT)

	else:
		if switcher == 'd':
			select(OL_DARK)
		else:
			select(OL_LIGHT)

###################################################################

def select(name):
	r = random.randint(0, len(name)-1)
	print(name[r])

###################################################################

if __name__ == '__main__':
	option = input("Enter platform ('vs', 'lc', or 'ol'): ")
	if option != 'vs' and option != 'lc' and option != 'ol':
		print('Invalid option')
		quit()

	switcher = input("Enter 'd' for dark thems; 'l' for light themes: ")
	if switcher != 'd' and switcher != 'l':
		print('Invalid option')
		quit()

	change_theme(option, switcher)
