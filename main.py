import random

'''
1 for rock
2 for paper 
3 for scissor

'''

computer = random.choice([1, 2, 3])
youchoice = int(input("Enter your choice: "))
gamedict = {
    "r" : 1,
    "p" : 2,
    "s" : 3
}
reversedict = {
    1 : "rock",
    2 : "papaer",
    3 : "scissor"
}

print("your choise:", reversedict[youchoice], "and computer choice:",  reversedict[computer])

if(computer == youchoice):
    print("its a draw")

else:
    if(computer == 1 and youchoice == 2):
        print("u lose")

    elif(computer == 2 and youchoice == 1):
        print("u won")

    elif(computer == 2 and youchoice == 3):
        print("u lose")

    elif(computer == 3 and youchoice == 2):
        print("u won")

    elif(computer == 1 and youchoice == 3):
        print("u lose")

    elif(computer == 3 and youchoice == 1):
        print("u won")

    else:
        print("something went wrong")