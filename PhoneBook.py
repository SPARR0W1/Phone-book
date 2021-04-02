#Import to module
import pickle
#Uploading contacts
ab = pickle.load(open("ab_dumb.p", "rb"))
def contactlist():
	#Contact list
	for name, email in ab.items():
		print("Contact {} with address {}.".format(name, email))

def addcontact():
	#Add contact
	name = input("Name:")
	email = input("Email:")
	ab[name] = email
def savecontact():
	#Saving contacts
	pickle.dump(ab, open("ab_dumb.p", "wb"))
'''def addedcontact():
	#The contact that was added
	print("Added to the contact list ", name)'''

addcontact()
contactlist()
#addedcontact()
savecontact()
