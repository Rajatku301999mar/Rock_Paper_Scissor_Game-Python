import random
comp_wins=0
player_wins=0

def Choose_Option():
    playerinput = input("What will you choose Rock, Paper or Scissor: ")
    if playerinput in ["Rock","rock", "r","R","ROCK"]:
        playerinput="r"
    elif playerinput in ["Paper","paper", "p","P","PAPER"]:
        playerinput="p"
    elif playerinput in ["Scissor","scissor", "s","S","SCISSOR"]:
        playerinput="s"
    else:
        print("I dont understand, try again.")
        Choose_Option()
    return playerinput

def Computer_Option():
    computerinput=random.randint(1,3)
    if computerinput==1:
        computerinput="r"
    elif computerinput==2:
        computerinput="p"
    else:
        computerinput="s"
    return computerinput

while True:
    print("")
    playerinput=Choose_Option()
    computerinput=Computer_Option()
    print("")

    if playerinput=="r":
        if computerinput=="r":
            print("You choose Rock, Computer choose Rock, Match Tied...")
        elif computerinput=="p":
            print("You choose Rock, Computer choose Paper, You Lose...")
            comp_wins+=1
        elif computerinput=="s":
            print("You choose Rock, Computer choose Scissor, You Win...")
            player_wins+=1
    elif playerinput=="p":
        if computerinput=="r":
            print("You choose Paper, Computer choose Rock, You Win...")
            player_wins+=1
        elif computerinput=="p":
            print("You choose Paper, Computer choose Paper, Match Tied...")
        elif computerinput=="s":
            print("You choose Paper, Computer choose Scissor, You Lose...")
            comp_wins+=1
    elif playerinput=="s":
        if computerinput=="r":
            print("You choose Scissor, Computer choose Rock, You Lose...")
            comp_wins+=1
        elif computerinput=="p":
            print("You choose Scissor, Computer choose Paper, You Win...")
            player_wins+=1
        elif computerinput=="s":
            print("You choose Scissor, Computer choose Scissor, Match Tied...")

    print("")
    print("Player wins: "+ str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    playerinput=input("Do you want to play again? (y,n)")
    if playerinput in ["Y","y","Yes","yes"]:
        pass
    elif playerinput in ["N","n","No","no"]:
        break
    else:
        break
