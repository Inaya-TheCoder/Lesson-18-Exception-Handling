try:
    a = int(input("Enter a no.:"))
    print (a,"is the no.")
except ValueError as ex:
    print ("Exception:",ex)