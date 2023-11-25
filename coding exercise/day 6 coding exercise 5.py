"""
Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:

1. prompts the user to enter a new member.

2. adds that member to members.txt at the end of the existing members.
For example, the user here has entered the member Solomon Right.

Add a new member : Solomon Right

In the above example, Solomon Right will be added to members.txt updating the content of the file to:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right

"""

new_member = input("Add a new member: ")

file = open('members.txt', 'r')
names = file.readlines()
file.close()

# Here it adds the name at the end of the document
names.append(new_member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(names)
file.close()