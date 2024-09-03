import time
import prologue
import game

print('')
print("Welcome to Text Based RPG!\n")

print("[1] - Prologue")
print("[2] - Start Game")
print("[3] - Quit\n")

start_game = input(">> ")

if start_game in ("1"):
    time.sleep(1)
    prologue.prologue()
    print('')
    print('[1] - Start Game')
    print('[2] - Quit\n')
    start_game = input('>> ')
    if start_game in ("1"):
        game.play_game()
    elif start_game in ("2"):
        exit()

elif start_game in ("2"):
    if __name__ == "__main__":
        game.play_game()

elif start_game in ("3"):
    exit()
