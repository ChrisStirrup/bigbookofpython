import random
import sys

# variable
japnum = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Shi', 5: 'Go', 6: 'Roku'}

# rules
print('''
In the game of Cho Han, two six-sided dice are rolled in a cup and you have to guess if the total is even (cho), or 
odd (Han).
The house cut is 10%.
''')

# determinism
print('''Before the game proper begins you must decide two things:
1)How large are your family's debts (10000 is typical)
2)How much money you start with (2500 is typical)
''')
# game set up

while True:
    print('How much debt has your family accrued?')
    debt = input('> ')
    if debt.isdecimal():
        debt = int(debt)
        print('Your family accrued', debt, 'in debt.')
        break
    else:
        print('Please enter a number')

while True:
    print('How large is your starting purse?')
    purse = input('> ')
    if purse.isdecimal():
        purse = int(purse)
        if purse < debt:
            print('You have', purse, 'money.')
            break
        elif purse > debt:
            print('Your starting purse cannot start larger than your debt.')
    else:
        print('Please enter a number')

# while True:
#    print('as a percentage how large is the house cut? (for example for 10% type 10)')
#    cut = input('> ')
#    if cut.isdecimal():
#        cut = float(cut)
#        if cut > 99:
#            print("The house cant take more than 100% of the bet (they're not that bad)")
#        else:
#            print('The house will take a', cut, '% cut.')
#            break
#    else:
#        print('Please enter a number')

# cut = (100 - cut)//100

cut = 0.9

# intro loop
print('''You are the scion of a noble house fallen on hard times, your creditors are tired of your family's excuses, and 
have demanded that all debts are paid in full upon the morning. 
There is but one chance; You have with you a purse containing the last of your family's money, and approach the 
gamboling house, curses and drunken laughing drifts from the rundown building, the smell of harsh alcohol assails your 
nostrils, as you find a open seat the game master looks up and says 'Cho Han'. 
''')
# game loop

while True:
    debtleft = debt - purse
    print('You have', purse, 'money. You need to accumulate', debt, 'money only', debtleft, 'to go!')
    print('The game master looks at you expectantly, how much do you bet?')
    while True:
        pot = input('> ')
        if not pot.isdecimal():
            print('Please input a number.')
        elif int(pot) > purse:
            print('Unfortunately you have insufficient money to make this bet.')
        else:
            pot = int(pot)
            break

    # set dice
    dice2 = random.randint(1, 6)
    dice1 = random.randint(1, 6)

    print('The game master swiftly takes your bet, and rolls the dice in his batted tin cup.')
    print('The dealer slams his cup, tilting it slightly, he looks at the dice then at you, Cho Han?')
    print('Make your decision Cho (even) or Han (odd)?')

# player bet
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('The game master looks at you "Cho (even) or Han(odd)?"')
            continue
        else:
            break

    print('The dealer slowly lift the cup and reveals')
    print('     ', japnum[dice1], '  ', japnum[dice2], '      ')
    print('      ', dice1, '   ', dice2, '          ')

# determine correct bet
    evenroll = (dice1 + dice2) % 2 == 0
    if evenroll:
        correctbet = 'CHO'
    else:
        correctbet = 'HAN'

    playerwon = bet == correctbet

# outcomes
    if playerwon:
        pot = pot * cut
        pot = int(pot)
        print("You win, the game master gives you the pot of", pot, "money.")
        purse = purse + pot
        debtleft = debt - purse
    else:
        purse = purse - pot
        print('The game master tucks your bet away.')

    if int(purse) >= int(debt):
        print('''Your debt is repaid and your family has a chance of rebuilding their fortunes, you leave the house 
        filled with hope''')
        sys.exit()
    elif purse == 0:
        print("The sun comes up and you have lost everything, your family has no more chances.")
        sys.exit()


