import time
import functions

def play_game():
    time.sleep(1)
    print('')
    print('Starting...')
    print('')
    time.sleep(1)
    print('You wake up and find yourself somewhere. You can\'t remember anything.\n')
    functions.shop()
    functions.attack(100, 10, 15, "Bad Guy", 100, 100, 15, 20)
    print(f"You have {functions.player["gold"]} gold")