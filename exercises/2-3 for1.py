'''
Continuing with our basic authenitication mechanism, let's expand on it.

  1. The variable user_permissions has a list of user:group separated by a comma
  2. Print only the username where the group is 'admin'
'''

user_group = "user1:admin,user2:admin,user3:app,user4:database"

for x in (user_group.split(",")):
  # enter code here
