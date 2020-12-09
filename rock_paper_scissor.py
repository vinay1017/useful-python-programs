# A simple logic exercise: rock, paper, scissors examples using loops 
# (and nested conditionals)

def paperRockScissors():
    # I would say that this is a longer way than most other ways, but 
    # it shows exactly what's happening at every step of the way 
    # and it is kind of dummy proof

    print("Your choices are: \nrock\npaper\nscissors")
    player1 = input("(enter Player 1's choice): ").lower()
    for i in range (20):
        print(" NO CHEATING ")
    player2 = input("(enter Player 2's choice): ").lower
    print("SHOOT!")

    # Checks if player 1 entered a correct value for the game
    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        # Checks if player 2 entered a correct value for the game
        if player2 == "rock" or player2 == "paper" or player2 == "scissors":
            # Checks if they tied first.
            if player1 == player2:
                print("you tied! Try again")
                return
            # Logically, it makes sense to me that you would put everything else inside...an else.
            else:
                if player1 == "scissors":
                    if player2 == "rock":
                        print("player 2 wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
                elif player1 == "paper":
                    if player2 == "scissors":
                        print("player 2 wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
                elif player1 == "rock":
                    if player2 == "paper":
                        print("player 2 wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
        else:
            print("player 2 entered an invalid option, try again")
            return
    else:
        print("player 1 or player 2 entered an invalid option, try again")
        return
                
def paperRockScissorsShort():
    # This is probably one of the shortest ways to do this, but
    # you're mostly just going to be hoping the users don't enter something
    # that shouldn't be there. I.E. "Pikachu"
    # Yes, pikachu probably beats paper, and loses to rock and maybe scissors?

    p1 = input("Player 1: rock, paper, or scissors ")
    p2 = input("Player 2: rock, paper, or scissors ")
    
    # Checks p1 against p2 every time and if p1 doesn't win in any of these conditionals,
    # it must mean that p2 is the winner...right? It's kind of an honor system.
    if p1 == p2:
        print("Draw")
    elif p1 == "rock" and p2 == "scissors":
        print("p1 wins")
    elif p1 == "paper" and p2 == "rock":
        print("p1 wins")
    elif p1 == "scissors" and p2 == "paper":
        print("p1 wins")
    else:
        print("p2 wins")

def computerVsMan():
    import random
    # And finally, it's time for the final showdown of man vs machine.
    # Unfortunately, it's a rock, paper, scissors fight to the end.
    # Good luck. 
    # This is using the same code from the first iteration, with random import.

    print("Your choices are: \nrock\npaper\nscissors\n")
    print("The robot awaits...\n")
    player1 = input("enter your choice: ").lower()

    player2 = random.choice(["rock", "paper", "scissors"])

    print("SHOOT!")
    print(f"The robot chose {player2}\n")

    # Checks if player 1 entered a correct value for the game
    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        # Checks if player 2 entered a correct value for the game
        if player2 == "rock" or player2 == "paper" or player2 == "scissors":
            # Checks if they tied first.
            if player1 == player2:
                print("you tied! Try again to save humanity")
                return
            # Logically, it makes sense to me that you would put everything else inside...an else.
            else:
                if player1 == "scissors":
                    if player2 == "rock":
                        print("robot wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
                elif player1 == "paper":
                    if player2 == "scissors":
                        print("robot wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
                elif player1 == "rock":
                    if player2 == "paper":
                        print("robot wins!")
                        return
                    else:
                        print("player 1 wins!")
                        return
    else:
        print("player 1 entered an invalid option, try again")
        return

# paperRockScissors()
# paperRockScissorsShort()
computerVsMan()