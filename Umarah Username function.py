def the_user_names():
  #Get input for user 1.
  user1_name = input("User 1 enter your name: ")
  #Get input for user 2.
  user2_name = input("User 2 enter your name: ")

  #Return user names
  return user1_name, user2_name

#print usernames 
user1, user2 = the_user_names()
print(f"User 1: {user1}")
print(f"User 2: {user2}")

print(f"Welcome to the game {user1} and {user2}")