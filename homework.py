try:
    a = int(input("Enter your age:"))
    print ("your age is",a)
except SyntaxError:
    print ("there is a syntax error")
except:
    print("something is wrong")
finally:
    print("the program will be executed")