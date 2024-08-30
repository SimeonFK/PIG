import random


def roll_dice():
    minimal_value = 1
    maximal_value = 6
    result = random.randint(minimal_value, maximal_value)
    return result


while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= int(players) <= 6:
            print(f'The number of players is: {players}')
            break
        else:
            print('Invalid, please stay in the given range!')
    else:
        print('Invalid, please input a digit!')

max_score = 10
players_scores = [0 for _ in range(players)]


while max(players_scores) < max_score:
    for player_index in range(players):
        print(f'\nPlayer {player_index + 1} turn has just started!\n')
        current_score = 0
        while True:
            should_roll = input('Would you like to roll (y) or (n)?: ')
            if should_roll.lower() == 'y':
                value = roll_dice()
                if value == 1:
                    print('You rolled a 1, your turn is over!')
                    current_score = 0
                    break
                else:
                    current_score += value
                    print('You rolled a:', value)
            elif should_roll.lower() == 'n':
                print(f'Your score is: {players_scores[player_index]}')
                break
            else:
                print('Invalid, type in (y) or (n)!')
            print('Your score is:', current_score)
        players_scores[player_index] += current_score
        print('Your total sccore is:', players_scores[player_index])
winner = max(players_scores)
print(f'Player {players_scores.index(winner) + 1} is the winner! :)')
