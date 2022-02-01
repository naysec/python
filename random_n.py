import random

win = random.randint(0,20)
# print(win)
# win = 8

# name1=str
print("Before begin game|")
print("Enter your name|")
a = raw_input(":")
print("------------------------------------------------------------------------")
# print("your name is " + a + )
# a.upper()
print( "Hello %s,"%(a.title()))
print("1. You have to choose number between 0 to 20 ")
print("2. You have only 3 chance to guess the winner number:")
print("------------------------------------------------------------------------")
# print("Your 
# name is" + user)

# print("1. This is game where you have to select number from 0 to 10 ")
# print("2. You have only 3 chances to guess the number")
attempt=0
print("\nEnter number between 0 to 20|")
tkinput=int(input(":"))#first input
while attempt<3:
      attempt=attempt+1
      if tkinput==win :
        print("Congratulation, You have guess the right number:  %i"%(win))
        break
        #if number is above then 20;
      elif tkinput!=win and tkinput>20:
         print("You have enter %i and number is above then 20."%(tkinput))
         print("%s, you break the rule and now we are exiting;"%(a.title()))
         break
         # this will run when attempt 1 will fail 
         # this is for 10 to 20
      elif 10<win<20 and tkinput!=win:
          print("You guess the wrong number;")
          print("Your number of attempt is %i "%(attempt))
          print("Hint: Number is between 10 to 20")
          tkinput2=int(input("Try once more\n:"))#second input
          attempt=attempt+1
          if tkinput2==win:
                  print("Congratulation, You guess the right number;")
                  break
          elif tkinput2!=win and 10<=win<=15:#for 10 to 15
                  print("You guess the wrong number;")
                  print("Your number of attempt is %i "%(attempt))
                  print("Hint: Number is between 10 to 15")
                  tkinput3=int(input("Try once more\n:"))#Third input
                  attempt=attempt+1
                  if tkinput3==win:
                      print("Congratulation, You guess the right number;")
                  else:
                      print("Your number of attempt is %i."%(attempt))
                      print("Dear %s, your number of attempt is exceeded;" %(a.title()))
                      print("Better luck next time Bye Bye;")
                      break
          elif tkinput2!=win and 15<=win<=20:#for 15 to 20
              print("helo")
              print("You guess the wrong number;")
              print("Your number of attempt is %i "%(attempt))
              print("Hint: Number is between 15 to 20")
              tkinput4=int(input("Try once more\n:"))#Third input
              attempt=attempt+1
              if tkinput4==win:
                  print("Congratulation, You guess the right number;")
              else:
                  print("Your number of attempt is %i."%(attempt))
                  print("Dear %s, your number of attempt is exceeded;" %(a.title()))
                  print("Better luck next time Bye Bye;")
                  break
      elif 0<=win<=10 and tkinput!=win:
            print("You guess the wrong number;")
            print("Your number of attempt is %i "%(attempt))
            print("Hint: Number is between 0 to 10")
            tkinput5=int(input("Try once more\n:"))
            attempt=attempt+1
            if tkinput5==win:
                print("Congratulations, You made it and successfully guess the number;")
            elif tkinput5!=win and 0<=win<=5: #for 0 to 5
                print("You guess the wrong number;")
                print("Your number of attempt is %i "%(attempt))
                print("Hint: Number is between 0 to 5")
                tkinput6=int(input())
                attempt=attempt+1
                if tkinput6==win:
                    print("Congratulations, You made it and successfully guess the number;")
                else:
                    print("Your number of attempt is %i."%(attempt))
                    print("Dear %s, your number of attempt is exceeded;" %(a.title()))
                    print("Better luck next time Bye Bye;")
                    break
            elif tkinput5!=win and 5<=win<=10:
                print("You guess the wrong number;")
                print("Your number of attempt is %i "%(attempt))
                print("Hint: Number is between 5 to 10")
                tkinput7=int(input())
                attempt=attempt+1
                if tkinput7==win:
                    print("Congratulations, You made it and successfully guess the number;")
                else:
                    print("Your number of attempt is %i."%(attempt))
                    print("Dear %s, your number of attempt is exceeded;" %(a.title()))
                    print("Better luck next time Bye;")
                    break
print("Number is %s"%(win))
print("Exiting")
print("---------------------------------------------------------------------------")






                

             

