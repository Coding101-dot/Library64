def remember_me():
  import json
  filename = 'username.json'
  try:
      with open(filename) as fn:
          username = json.load(fn)
  except FileNotFoundError:
      username = input("Please enter username here :")
      with open(filename,'w') as fn:
          json.dump(username,fn)

  else:
      print("Hello " + username + " It's great to have you back again.")

remember_me()