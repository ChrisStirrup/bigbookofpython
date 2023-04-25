import random
import sys

Japan_Numbers = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Shi', 5: 'Go', 6: 'Roku'}

print('''Cho-Han, by Al Sweigart al@inventwithpython
In this traditional Japanese dice game, tow dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the 
total of the dice is an even (cho) or odd (han) number.   
''')

purse = 5000
while True:  #main game loop
    #place your bet
    print('You have', purse, 'mon. How much do you bet? (or Quit)')
    while True:
        pot = input('> ')
        if pot.upper() == 'Quit':
            print('thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You have insufficient funds to make this bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of the dice.')
    print('The dealer slams the cup on the floor, still covering the dice')
    print('and asks your bet.')
    print()
    print('    Cho (Even) or Han (Odd)?')

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "Cho" or "Han".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print("     ", Japan_Numbers[dice1], '-', Japan_Numbers[dice2])
    print("     ", dice1, '-', dice2)

    rolleven = (dice1 + dice2) % 2 == 0
    if rolleven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('you won! you take ', pot, 'mon.')
        pot = pot * 0.9
        purse = purse + pot
        print('The house collects their cut and you now have', purse, 'mon.')
    else:
        purse = purse - pot
        print('you lost!')
        print('you now have', purse, 'mon.')

    if purse == 0:
        print('you have run out of money')
        print('thanks for playing')
        sys.exit()
