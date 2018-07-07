# we can store test data in this module like users

users = [
	{"name": "invalid_user", "email": "invalidUser@test.com", "password": "qwert1235"},
	{"name": "valid_user", "email": "test_pubg@gmail.com", "password": "qwertypubg"},
]

def get_user(name):
	try:
		return (user for user in users if user["name"] == name).next()
	except:
		print "\n     User %s is not defined, enter a valid user.\n" %name