a = True
while a:
  try:
       num = int(input("Enter a no.:"))
       while (a % 2 == 0):

        print ("bye")
       a = False
    
  except ValueError:
      print ("it is wrong")