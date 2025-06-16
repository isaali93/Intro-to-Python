'''
Let's assume that you have a program that checks username, password and group
before granting access to a file.

  1. Write a program that asks a user for their username and password.
  2. The program then checks to see if it matches either of the usernames
  provided in the user1_permission and user2_permission variables
  3. If there is a match, print the group level

TIP
- Use the .split on the variables
- Use string "addition": "username" + ":" + "password"
- Some of the code has already been provided
'''

#Structure - username:password:group
user1_permission = "user1:password1:admin"
user2_permission = "user2:PassWord2:normal"

# Input from user
user_name = input("Enter your username: ")


