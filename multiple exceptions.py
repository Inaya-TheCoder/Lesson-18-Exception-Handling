try:
    num1,num2 = eval(input("Enter two numbers, seperated by a comma(,):"))
    result = num1 / num2
    print("result is",result)
except ZeroDivisionError:
    print ("there is 0")
except SyntaxError:
    print ("there is a syntax error")
except:
    print ("somethng is wrong")
else:
    print("Nothing is wrong/no exceptions")
finally:
    print("The Program will be executed")