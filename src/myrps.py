# player should be able to type r p or s or q to quit
# Computer will pick, print results, and track history
# REPL read eval print loop
# have computer choose a random index 1-3 
import random

choices = ['r', 'p', 's']
wins = 0
losses = 0
ties = 0
won = 'you won!'
tie = ' you tied with the computer'
lost = "you've been beat!"
print('Welcome! Choose r for rock, p for paper, s for scissors, or q to quit and see your tally')
while True:
    #Read
    cmd = input("~~> ")
    cpu = random.choice(choices)
    
    if(cmd == 'q'):
        print(f'Have a great day! Wins:{wins} Losses: {losses} Ties: {ties}')
        break
    if(cmd == 'r'):
        print(f'Player chose {cmd}')
        print(f'Computer chose {cpu}')
        if(cpu == 'r'):
            ties += 1
            print(tie)
        elif(cpu == 'p'):
            losses += 1
            print(lost)
        elif(cpu == 's'):
            wins += 1
            print(won)
        else:
            print('Something is not working, please try r, p , or s to play, or q to quit')
    elif(cmd == 'p'):
        print(f'Player chose {cmd}')
        print(f'Computer chose {cpu}')
        if(cpu == 'r'):
            wins += 1
            print(won)
        elif(cpu == 'p'):
            ties += 1
            print(tie)
        elif(cpu == 's'):
            losses += 1
            print(lost)
        else:
            print('Something is not working, please try r, p , or s to play, or q to quit')
    elif(cmd == 's'):
        print(f'Player chose {cmd}')
        print(f'Computer chose {cpu}')
        if(cpu == 'r'):
            losses += 1
            print(lost)
        elif(cpu == 'p'):
            wins += 1
            print(won)
        elif(cpu == 's'):
            ties += 1
            print(tie)
        else:
            print('Something is not working, please try r, p , or s to play, or q to quit')
    else:
        print(f'{cmd} not working, please try r, p , or s to play, or q to quit')

