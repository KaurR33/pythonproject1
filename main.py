print("Welcome to the Game!")
name = input("Your Name: ")
age = int(input("Your age : "))
health = 10
if(age >= 18):
    print("player named", name, " and aged ", age, "your game starts now.")
    print("your health points are ", health)
    wantToPlay = input("do you wan to play ? type yes or no only ").lower()
    if(wantToPlay=="yes"):
        print("Cool! Let's play in dude!")
        leftOrRight = input("left or right? ").lower()
        if(leftOrRight=="left"):
            health -= 5
            print("Your health points are ", health)
            choice2 = input("Bad haircut or bad dye job?")
            if(choice2 == "bad haircut"):
                health+= 10
                print("you got bald head hahahhahhahah, health points ", health)
            elif(choice2 == "bad dye job"):
                health=0
                print("Aw kiddo you lose this game ain't for losers. bye bye")
            else:
                print("choose something!")
                continueOrNot = input("continue or not?")
                if(continueOrNot=="continue"):
                    choice2 = input("Bad haircut or bad dye job?")
                    if (choice2 == "bad haircut"):
                        health += 10
                        print("you got bald head hahahhahhahah, health points ", health)
                    elif (choice2 == "bad dye job"):
                        health = 0
                        print("Aw kiddo you lose this game ain't for losers. bye bye")
                elif(continueOrNot=="no"):
                    health = 0
                    print("bye bye! Your health is ", health )

        else:
            health += 5
            print("you are absolutely right! your health points are : ", health)
    else:
        print("It's ok next time")
elif(age >= 14):
    print("You ca play with supervision, Tiny player. ")
    leftOrRight = input("left or right?")
    if(leftOrRight=="left"):
        health+=10
        print("you won!", health)
    else:
        health=0
        print("you lose. you lost all the health. health is ", health)
else:
    print("You are small hahah be big first! ;) ")