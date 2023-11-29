import random
items=['r','s','p']
item_meaning={
    'r':'rock',
    'p':'paper',
    's':'scissors'
    }
game_round=int(input('Please enter the rounds of game  : '))
user_point=0
ai_point=0

def user_win():
    print('You Won')
    print('You got one point')
    print(f'YOU : {user_point} , AI : {ai_point}')

def ai_win():
    print('You Lose !')
    print('AI got one point')
    print(f'YOU : {user_point} , AI : {ai_point}')

for i in range(game_round):
    user_choice=input('enter your chose : (r(rock) p(paper) s(scissors))  ; ')
    ai_choise=random.choice(items)
    print(f'your choice is {item_meaning[user_choice]} and ai choice is {item_meaning[ai_choise]}')
    if user_choice in items:
        #r>s.s>p.p>r
        if user_choice==ai_choise:
            print('TIE')
            print('No one got point!')
        elif (user_choice =='r'and ai_choise=='s')or (user_choice =='s'and ai_choise=='p'):
            user_point+=1
            user_win()
        elif user_choice=='p'and ai_choise=='r':
            user_point+=1
            user_win()
        else:
            ai_point+=1
            ai_win()
    else:
        raise Exception('Invalid entry')

print(f'Played {game_round} times')
print(f'The final score is : You {user_point} , Ai {ai_point}')