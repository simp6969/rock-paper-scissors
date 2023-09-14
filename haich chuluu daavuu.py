import random
run = True
while run:
   lst = ["haich", "chuluu", "daavuu"]
   computer  = random.choice(lst)
   print("haich chuluu daavuu songonuu")
   usr = input().lower()
   

   if computer == usr:
      print("tentslee")
      print("computer " , computer)
      print("toglogch "+ usr)
   elif usr not in lst:
      print("zuv ug oruulnauu")
   elif usr == 'haich':
      if computer == 'chuluu':
         print("ylagdlaa ")
         print("toglogch " + usr)
         print("computer " + computer)
      if computer == "daavuu":
         print("ta yllaa ")
         print("computer " , computer)
         print("toglogch " , usr)
   elif usr == 'chuluu':
      if computer == 'daavuu':
         print("ylagdlaa ")
         print("toglogch " + usr)
         print("computer " + computer)
      if computer == "haich":
         print("ta yllaa")
         print("computer " ,computer)
         print("toglogch " , usr)
   elif usr == 'daavuu':
      if computer == 'haich':
         print("ylagdlaa ")
         print("toglogch " + usr)
         print("computer ", computer)
      if computer == "chuluu":
         print("ta yllaa")
         print("computer " + computer)
         print("toglogch " + usr)


   usr_on_end = input("dahin toglohuu y/n ").lower()
   if usr_on_end == "n":
      run = False

