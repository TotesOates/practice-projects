#16.Password Generator
import random

while True:
    ask1 = input("Do you want to generate a password? (Y/N)")
    if ask1 == 'Y':
        try:
            ask2 = int(input("How many characters do you want your password to be?"))
            charchoice = ask2
            randpass = 'abcdefghiklmnopqrstuvwxyz1234567890!@#$%^&*()'
            password = "".join(random.sample(randpass, charchoice))
            print("I've generated this password " + "'" + password + "'" + " for you!")
        except:
            print('That is not a number')
            continue
    elif ask1 == "N":
        quit()
    else:
        continue


