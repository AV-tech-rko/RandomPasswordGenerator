import RandomPasswordGenerator as MyPassword

while 1:
  user_pass_length = int(input("Enter password length: \n"))
  print(MyPassword.GeneratePassword(user_pass_length)
  userreply = input("Do you want more passwords?  y/n ")
  if userreply == "y":
      continue
  elif userreply == "n":
	  break	
