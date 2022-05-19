import random

print('Hi Welcome to the game of Rock Paper scissors!')
print('A bot is going to play with you!')
print('Type rock / scissor / paper to move!')
print('')
print('You can type quit or restart too!')

player_score = 0
bot_score = 0
running = True


choices = ['rock', 'paper', 'scissor']
win = ['rock scissor', 'paper rock', 'scissor paper']
draw = ['rock rock', 'paper paper', 'scissor scissor']
lose = ['scissor rock', 'rock paper', 'paper scissor']

def calc_result(player_move, bot_move):
    global player_score
    global bot_score
    string = player_move + ' ' + bot_move

    if string in win:
        player_score += 1
        result = 'Yay you won!'
        render_result(result)

    elif string in draw:
        result = 'Try Again! Its a Draw!'
        render_result(result)

    elif string in lose:
        bot_score +=1
        result = 'Sorry But you lost!'
        render_result(result)

def render_result(result):
    print(result)
    print(f'Your Move: {player_move}')
    print(f'Bot Move: {bot_move}')
    print(f'PLAYER SCORE: {player_score} BOT SCORE: {bot_score}')

def other_cmd(input):
    global running
    global player_score
    global bot_score
    if input == 'quit':
        running = False
        print('Ok Bye cya later!')
    if input == 'restart':
        player_score = 0
        bot_score = 0
        print(f'PLAYER SCORE: {player_score} BOT SCORE: {bot_score}')


while running:
    print(' ')
    player_move = input('Enter Your move: ').lower()
    bot_move = random.choice(choices)
    other_cmd(player_move)
    if running:
        calc_result(player_move,bot_move)


