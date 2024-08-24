health = 100
gold = 50
player_attack_damage = 0
swords = ["None", "Wood", "Iron", "Steel"]
sword = swords[0]

def shop():
    global health, gold, player_attack_damage, swords, sword

    print("")
    print("Welcome to the shop!")
    print(f"you have {gold} gold.")
    print("")
    print("Swords:")
    print("[1] - Wood (Damage: 8) (cost: 15 gold)")
    print("[2] - Iron (damage: 12) (cost: 20 gold)")
    print("[3] - Steel (damage: 16) (cost: 30 gold)")
    print("")
    print("What would you like to buy?")
    buy_sword = input(">> ")

    if buy_sword in ("1"):
        if gold < 15:
            print("You don't have enough gold!")
        else:
            sword = swords[1]
            gold -= 15
            print(f"You have purchased a Wooden Sword! You have {gold} gold remaining.")

    elif buy_sword in ("2"):
        if gold < 20:
            print("You don't have enough gold!")
        else:
            sword = swords[2]
            gold -= 20
            print(f"You have purchased an Iron Sword! You have {gold} gold remaining.")
 
    elif buy_sword in ("3"):
        if gold < 30:
            print("You don't have enough gold!")
        else:
            sword = swords[3]
            gold -= 30
            print(f"You have purchased a Steel Sword! You have {gold} gold remaining.")


if sword == swords[0]:
    player_attack_damage += 2
elif sword == swords[1]:
    player_attack_damage += 8
elif sword == swords[2]:
    player_attack_damage += 12
elif sword == swords[3]:
    player_attack_damage += 16

shop()