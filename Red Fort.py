a = 'Red Fort '
b = 'India'
c = 'Is In '
a_b_c = a+c+b
print (a_b_c)





class Person:
	def __init__(ID,Id,Name,Password):
		ID.ID = Id
		ID.Name = Name
		ID.Password = Password
	def __str__(ID):
		print('ID = ' + str(ID.ID),'Name = ' + str(ID.Name),'Password = ' + str(ID.Password),sep = '\n')
	def Join_Team(ID,Team_Password):
		print('Joining Team....')
		global Team_Passwords
		if Team_Password in Team_Passwords:
			print('Conecting....')
			Add_person_to_team(Team_Password,ID.ID)
			x = find(ID.ID,Team_Password)
			if x:
				print('Joined Succsesssfully....')
			else:
				import sys
				print('A Error Happend While Joining!!!!,Sorry...',file = sys.stderr)
