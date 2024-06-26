import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your choice Rock,Paper,Scissor \n")
computer_choice=random.choice(item_list)
print(f"{computer_choice} is computer's choice" )
if(user_choice==computer_choice):
  print("Match tie")
elif(user_choice=="Rock"):
    if(computer_choice=="Scissor"):
      print(f"computer win")
    else:
      print("You lose") 
elif(user_choice=="Paper"):
    if(computer_choice=="Scissor"):
      print("computer win")
    else:
      print("You lose")        
elif(user_choice=="Scissor"):
    if(computer_choice=="Paper"):
      print(f"you win")
    else:
      print("computer win") 
else: 
  print("Invalid choice")