import random
choices=["Rock","Paper","Scissor"]
computer_choice=random.choice(choices)

print("Choice of Computer is",computer_choice)    

user_choice=input("Choice of user: Rock Paper or Scissor ?")

if computer_choice==user_choice:
    print("Match is draw")
elif computer_choice=="Rock":
    if user_choice=="Paper":
        print("Winner is User  ")
    elif user_choice=="Scissor":
        print("Winner is Computer")
    else:
        print("Error")

elif computer_choice=="Paper":
    if user_choice=="Rock":
        print("Winner is Computer  ")
    elif user_choice=="Scissor":
        print("Winner is user")
    else:
        print("Error")

elif computer_choice=="Scissor":
    if user_choice=="Paper":
        print("Winner is Computer  ")
    elif user_choice=="Rock":
        print("Winner is user")
    else:
        print("Error")
else:
    print("Error")
    
    



