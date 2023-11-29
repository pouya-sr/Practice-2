import random
cups=int(input('How many cups? '))
chances=int(input('How many chances? '))
ai_goal=random.randint(1,cups)
LINE_LENGHT=15
print('-'*LINE_LENGHT)
word='s'
for i in range(chances):
    if chances-i==1:
        word=''
    print(f'{chances-i} chance{word} left .')
    user_gess=int(input(f'Gess [1-{cups}]: '))
    if user_gess==ai_goal:
        print('you guessed right.')
        break
    else:
        print('wronge guess.')
    print('-'*LINE_LENGHT)
if user_gess==ai_goal:
    print('-'*LINE_LENGHT)
    print('you won!')
else:
    print(f' the right answer is {ai_goal}')
    print('you lost. sorry!')