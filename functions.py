import random
import time
import math

player = {
    "health": 100,
    "gold": 50,
    "sword": {"level": 1, "damage": 10},
    "shield": {"level": 1, "block_chance": 5},
    "armor": {"level": 1, "damage_reduction": 0},
    "healing_potion": 0,
}

shop_items = {
    "sword": {"price": 10},
    "shield": {"price": 15},
    "armor": {"price": 20},
    "healing_potion": {"price": 5,}
}

def game_pause():
    print('')
    input('Press enter to continue...')
    print('')

def calculate_upgrade_price(base_price, level):
    return math.ceil(base_price * (1.2 ** (level - 1)))

def shop_options():
    print('')
    print('Welcome to the shop!')
    print(f'Gold: {player["gold"]}\n')

    for item, details in shop_items.items():
        if item != "healing_potion":
            level = player[item]["level"]
            next_price = calculate_upgrade_price(details["price"], level + 1)
            print(f"[{list(shop_items.keys()).index(item) + 1}] - {item.capitalize()} (Level: {level}) - Next upgrade: {next_price} gold")
        else:
            print(f"[{list(shop_items.keys()).index(item) + 1}] - Healing Potion (Owned: {player['healing_potion']}) - Price: {details['price']} gold")

    print("\n[0] - Exit shop\n")

def buy_item(item_index):
    item_list = list(shop_items.keys())
    if 1 <= item_index <= len(item_list):
        item = item_list[item_index - 1]
        if player["gold"] >= shop_items[item]["price"]:
            player["gold"] -= shop_items[item]["price"]
            if item != "healing_potion":
                player[item]["level"] += 1
                print(f"Your {item} is now level {player[item]['level']}.")
            else:
                player["healing_potion"] += 1
                print(f"You now have {player['healing_potion']} healing potion(s).")
            game_pause()
        else:
            print("You don't have enough gold!")
            game_pause()
    else:
        print("Invalid option.")


def shop():
    while True:
        shop_options()
        choice = input(">> ").strip().lower()
        
        if choice in ('0'):
            break
        elif choice.isdigit():
            buy_item(int(choice))
        else:
            print("Invalid input. Please enter a number or 'exit'.")

def attempt_flee(chance):
    success_weight = chance
    failure_weight = 100 - chance
    return random.choices([True, False], weights=[success_weight, failure_weight], k=1)[0]

def generate_escape_chance():
    random_value = random.random() ** 2
    chance_of_escape = 30 + int(random_value * 70)
    return chance_of_escape

import random
import math
import time

def attack(player_hp, player_min_damage, player_max_damage, enemy_name, enemy_hp, enemy_bounty, enemy_min_damage, enemy_max_damage):
    
    sword_level = player["sword"]["level"]
    shield_level = player["shield"]["level"]
    armor_level = player["armor"]["level"]

    fixed_enemy_hp = enemy_hp
    fixed_player_hp = player_hp

    print(f'Bounty on {enemy_name}: {enemy_bounty}')
    while player_hp > 0 and enemy_hp > 0:
        player_attack_damage = random.randint(player_min_damage, player_max_damage) * (1 + 0.2 * (sword_level - 1))
        player_attack_damage = math.ceil(player_attack_damage)

        enemy_attack_damage = random.randint(enemy_min_damage, enemy_max_damage)
        damage_reduction = min(0.2 * (armor_level - 1), 0.8)
        enemy_attack_damage *= (1 - damage_reduction)
        enemy_attack_damage = math.ceil(enemy_attack_damage)

        block_chance = min(player["shield"]["block_chance"] + 5 * (shield_level - 1), 90)  # Cap at 90%

        chance_of_escape = generate_escape_chance()

        print('')
        print(f'Player hp: {player_hp}/{fixed_player_hp} | {enemy_name} hp: {enemy_hp}/{fixed_enemy_hp} | Chance of escape: {chance_of_escape}%')
        print('[1] - Attack')
        print('[2] - Attempt to escape\n')

        action = input('>> ')
        print('')
        if action in ("1"):
            time.sleep(0.5)
            enemy_hp -= player_attack_damage
            print(f'You attack {enemy_name} and deal {player_attack_damage} damage.')
            if enemy_hp <= 0:
                player["gold"] += enemy_bounty
                print(f'{enemy_name} is defeated! You earned {enemy_bounty} gold!')
                print('')
                break

            if random.random() * 100 < block_chance:
                print(f'You successfully blocked {enemy_name}\'s attack!')
            else:
                player_hp -= enemy_attack_damage
                print(f'{enemy_name} attacks you and deals {enemy_attack_damage} damage.\n')
                if player_hp <= 0:
                    print('Defeat!')
                    break

        elif action in ("2"):
            time.sleep(0.5)
            print('You attempt to escape!')
            if attempt_flee(chance_of_escape):
                print('You successfully escaped!\n')
                break
            else:
                player_hp -= enemy_attack_damage
                if player_hp <= 0:
                    print(f'{enemy_name} caught you. Defeat!')
                    break
                print(f'Escape failed! {enemy_name} damaged you and the battle continues.\n')
