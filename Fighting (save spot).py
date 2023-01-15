import json
import random

og = "\033[0;0m"
red = "\033[0;31m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
brown = "\033[0;33m"
italic = "\033[3m"
bold = "\033[1m"

class Hero:
    def __init__(self, health, attack, defence, coin, floor, xp, up, loot, equip, spell, level):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.coin = coin
        self.xp = xp
        self.floor = floor
        self.up = up
        self.loot = sorted(loot)
        self.equip = equip
        self.spell = spell
        self.level = level

    def checkStats(self):
        print(f"{red}Health: {self.health}{og}")
        print(f"{purple}Attack: {self.attack}{og}")
        print(f"{blue}Defence: {self.defence}{og}")
        print(f"{green}Coins: {self.coin}{og}")
        print(f"{green}Level {self.level}{og}")
        print(f"{green}XP: {self.xp}/{self.up}{og}")
        print(f"{green}Inventory: {clean(self.loot)}{og}")
        print(f"{green}Equipped: {clean(self.equip)}{og}")
        print(f"{green}Spells: {clean(self.spell)}{og}")
        print()

    def battle(self, Enemy):
        damage = round(Enemy.attack * (1 - (self.defence * 0.01)))
        self.health = self.health - damage
        if self.health <= 0:
            print(f"{italic}You have died.{og}")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def battle(self, Hero):
        self.health -= Hero.attack
        if self.health <= 0:
            print(f"{brown}{self.name}{og} {italic}is dead{og}")
            Hero.coin += 1
            print(f"{green}Earned 1 coin!{og}")
            earn = 10 + (10 * Hero.floor)
            Hero.xp += earn
            print(f"{green}Gained {earn} XP!{og}")
            self.levelup(Hero)
            dropped = things()
            hero.loot.append(dropped)
            print(f"{italic}{self.name} dropped {dropped}!{og}")
        else:
            print(f"{brown}{self.name}{og} has {brown}{self.health} health{og} left and {brown}{self.attack} attack{og}.")

    def levelup(self, Hero):
        if Hero.xp == Hero.up:
            Hero.xp = 0
            Hero.up += 50
            print(f"{green}Level up!{og}")
            Hero.health += 10
            Hero.attack += 10
            Hero.defence += 10
            Hero.coin += 20
            Hero.loot.append(things())
            Hero.level += 1
        elif Hero.xp > Hero.up:
            Hero.xp = Hero.xp-Hero.up
            Hero.up += 50
            print(f"{green}Level up!{og}")
            Hero.health += 10
            Hero.attack += 10
            Hero.defence += 10
            Hero.coin += 20
            Hero.loot.append(things())
            Hero.level += 1
        if Hero.level % 3 == 0:
            ability = magic()
            Hero.spell.append(ability)
            print(f"You got the spell: {ability}")

class Vampire(Enemy):
    def __init__(self, name, health, attack):
        Enemy.__init__(self, name, health, attack)
        self.max = health

    def battle(self, Hero):
        if self.health + self.attack/2 <= self.max:
            self.health += int(self.attack/2)
        else:
            self.health = self.max
        super().battle(Hero)

class Golem(Enemy):
    def __init__(self, name, health, attack):
        Enemy.__init__(self, name, health, attack)

    def battle(self, Hero):
        self.health -= int(Hero.attack/2)
        if self.health <= 0:
            print(f"{brown}{self.name}{og} {italic}is dead{og}")
            hero.coin += 1
            print(f"{green}Earned 1 coin!{og}")
            earn = 10 + (10 * hero.floor)
            hero.xp += earn
            print(f"{green}Gained {earn} XP!{og}")
            self.levelup(Hero)
            dropped = things()
            hero.loot.append(dropped)
            print(f"{italic}{self.name} dropped {dropped}!{og}")
        else:
            print(f"{brown}{self.name}{og} has {brown}{self.health} health{og} left and {brown}{self.attack} attack{og}.")

class Spell:
    def __init__(self, name, attack, health, defence, debuff, used, turn):
        self.name = name
        self.attack = attack
        self.health = health
        self.defence = defence
        self.debuff = debuff
        self.used = used
        self.turn = turn

    def timeup(self):
        if self.used:
            self.turn += 1
            if self.turn == 5:
                self.turn = 0
                self.used = 0
                hero.attack -= self.attack
                hero.defence -= self.defence
                enemy.attack += self.debuff
                vampire.attack += self.debuff
                golem.attack += self.debuff

    def cast(self):
        if self.attack != 0:
            hero.attack += self.attack
            print(f"{purple}Increased attack by {self.attack}!{og}")
        if self.health != 0:
            hero.health += self.health
            print(f"{red}Healed {self.health} hp!{og}")
        if self.defence != 0:
            hero.defence += self.defence
            print(f"{blue}Increased defence by {self.defence}!{og}")
        if self.debuff != 0:
            enemy.attack -= self.debuff
            vampire.attack -= self.debuff
            golem.attack -= self.debuff
            print(f"{italic}Debuff monsters attack by {self.debuff}!{og}")

class Item:
    def __init__(self, name, attack, defence, health, xp, type):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.xp = xp
        self.type = type

    def equip(self):
        if self.attack != 0:
            hero.attack += self.attack
            print(f"{italic}Equipped {self.name}.{og} {purple}Gained {self.attack} attack!{og}")
        if self.defence != 0:
            hero.defence += self.defence
            print(f"{italic}Equipped {self.name}.{og} {blue}Gained {self.defence} defence!{og}")
        if self.health != 0:
            hero.health += self.health
            print(f"{italic}Drank {self.name} potion.{og} {red}Gained {self.health} health!{og}")
        if self.xp != 0:
            hero.xp += self.xp
            print(f"{italic}Drank {self.name} potion.{og} {green}Gained {self.xp} xp!")

        hero.loot.remove(self.name)
        if self.type != "Potion":
            hero.equip.append(self.name)

def things():
    stuff = ["dagger", "boots", "gloves", "armour", "health potion", "xp potion"]
    num = random.randint(0, len(stuff)-1)
    return stuff[num]

def magic():
    m = ["Lunar Blaze", "Calling of Healing", "Aura of The Guard", "Burst of Devouring"]
    num = random.randint(0, len(m)-1)
    return m[num]

def clean(items):
    t = sorted(items)
    if len(t) == 0:
        return "Nothing here..."
    else:
        thing = ""
        for i in range(len(t)):
            if i + 1 == len(t):
                thing += t[i]
            else:
                thing += t[i] + ", "
        return thing

def damage(attack, defence):
    damage = round(attack * (1 - (defence * 0.01)))
    return damage

def loadhero():
    with open("herosave.json", "r") as read_file:
        return json.load(read_file)

def save():
    herosave = [hero.health, hero.attack, hero.defence, hero.coin, hero.floor, hero.xp, hero.up, hero.loot, hero.equip, hero.spell, hero.level]
    with open("herosave.json", "w") as write_file:
        json.dump(herosave, write_file)

itembuy = {"dagger": 10, "boots": 8, "gloves": 6, "armour": 20, "health potion": 30, "xp potion": 30}
itemsell = {"dagger": 5, "boots": 3, "gloves": 1, "armour": 15, "health potion": 25, "xp potion": 25}
spellbuy = {"Lunar Blaze": 30, "Calling of Healing": 30, "Aura of The Guard": 30, "Burst of Devouring": 30}
spellsell = {"Lunar Blaze": 25, "Calling of Healing": 25, "Aura of The Guard": 25, "Burst of Devouring": 25}

print(f"{bold}Would you like to load your previous save file? (yes/no){og}")
savefile = loadhero()
hero = Hero(savefile[0], savefile[1], savefile[2], savefile[3], savefile[4], savefile[5], savefile[6], savefile[7], savefile[8], savefile[9], savefile[10])
print(f"{brown}Floor {hero.floor}{og}")
hero.checkStats()

previous = input()
if previous == "no":
    hero = Hero(100, 20, 10, 0, 0, 0, 50, [], [], [], 1)
enemy = Enemy("Enemy", 50+hero.floor, 5+hero.floor)
vampire = Vampire("Vampire", 50+hero.floor, 5+hero.floor)
golem = Golem("Golem", 100+hero.floor, 1+hero.floor)

lunar = Spell("Lunar Blaze", 5, 0, 0, 0, False, 0)
heal = Spell("Calling of Healing", 0, 5, 0, 0, False, 0)
aura = Spell("Aura of The Guard", 0, 0, 5, 0, False, 0)
devour = Spell("Burst of Devouring", 0, 0, 0, 1, False, 0)

dagger = Item("dagger", 5, 0, 0, 0, "Equipment")
boots = Item("boots", 0, 3, 0, 0, "Equipment")
gloves = Item("gloves", 0, 1, 0, 0, "Equipment")
armour = Item("armour", 0, 7, 0, 0, "Equipment")
healthp = Item("health potion", 0, 0, 15, 0, "Potion")
xpp = Item("xp potion", 0, 0, 0, 15, "Potion")

print()
print(f"{bold}Type 'stats' to check stats{og}")
print(f"{bold}Type 'quit'' to quit{og}")
print(f"{bold}Type 'fight' to fight the monsters{og}")
print(f"{bold}Type 'shop' to buy items or spells by spending coins{og}")
print(f"{bold}Type 'sell' to sell items or spells and earn coins{og}")
print(f"{bold}Type 'equipment' to equip and unequip items{og}")
print()
print(f"{bold}Floor {hero.floor}")
print(f"{brown}{enemy.name}{og} has {brown}{enemy.health} health{og} and {brown}{enemy.attack} attack{og}.")
print(f"{brown}{vampire.name}{og} has {brown}{vampire.health} health{og} and {brown}{vampire.attack} attack{og}.")
print(f"{brown}{golem.name}{og} has {brown}{golem.health} health{og} and {brown}{golem.attack} attack{og}.")

action = input()
done = False

while action != "quit":

    if action == "fight":
        lunar.timeup()
        heal.timeup()
        aura.timeup()
        devour.timeup()

        print()
        print(f"{bold}Would you like to use a spell or melee it?{og}")
        brawl = input()
        if brawl == "spell":
            print()
            print(f"{bold}What spell would you like to use?{og} {green}{clean(hero.spell)}{og}")
            use = input()
            if use not in hero.spell:
                print(f"{italic}You do not have that spell. You will melee it.{og}")
                use = "melee"
            elif use == "Lunar Blaze":
                if lunar.turn != 0:
                    print(f"{italic}This skill is on cooldown. You will melee it.{og}")
                    use = "melee"
                else:
                    lunar.turn = 1
                    lunar.used = True
            elif use == "Calling of Healing":
                if heal.turn != 0:
                    print(f"{italic}This skill is on cooldown. You will melee it.{og}")
                    use = "melee"
                else:
                    heal.turn = 1
                    heal.used = True
            elif use == "Aura of The Guard":
                if aura.turn != 0:
                    print(f"{italic}This skill is on cooldown. You will melee it.{og}")
                    use = "melee"
                else:
                    aura.turn = 1
                    aura.used = True
            elif use == "Burst of Devouring":
                if devour.turn != 0:
                    print(f"{italic}This skill is on cooldown. You will melee it.{og}")
                    use = "melee"
                else:
                    devour.turn = 1
                    devour.used = True
            brawl = use
        if brawl == "melee":
            print()
            if enemy.health > 0:
                enemy.battle(hero)
                done = True
            if vampire.health > 0:
                vampire.battle(hero)
                done = True
            if golem.health > 0:
                golem.battle(hero)
                done = True
            if enemy.health <= 0 and vampire.health <= 0 and golem.health <= 0:
                hero.floor += 1
                print()
                hero.checkStats()
                print(f"{bold}Continue? (yes/no){og}")
                action = input()
                if action == "no":
                    break
                elif action == "yes":
                    print()
                    done = False
                    enemy = Enemy("Enemy", 50+hero.floor, 5+hero.floor)
                    vampire = Vampire("Vampire", 50+hero.floor, 5+hero.floor)
                    golem = Golem("Golem", 100+hero.floor, 1+hero.floor)
                    print()
                    print(f"{bold}Floor {hero.floor}{og}")
                    print(f"{brown}{enemy.name}{og} has {brown}{enemy.health} health{og} and {brown}{enemy.attack} attack{og}.")
                    print(f"{brown}{vampire.name}{og} has {brown}{vampire.health} health{og} and {brown}{vampire.attack} attack{og}.")
                    print(f"{brown}{golem.name}{og} has {brown}{golem.health} health{og} and {brown}{golem.attack} attack{og}.")
        else:
            if brawl == "Lunar Blaze":
                lunar.cast()
            elif brawl == "Calling of Healing":
                heal.cast()
            elif brawl == "Aura of The Guard":
                aura.cast()
            elif brawl == "Burst of Devouring":
                devour.cast()
            done = True
        if done:
            if hero.health > 0 and enemy.health > 0:
                print()
                print(f"{brown}{enemy.name}{og} has dealt {brown}{damage(enemy.attack, hero.defence)} damage{og}.")
                hero.battle(enemy)
            if hero.health > 0 and vampire.health > 0:
                if enemy.health <= 0:
                    print()
                print(f"{brown}{vampire.name}{og} has dealt {brown}{damage(vampire.attack, hero.defence)} damage{og}.")
                hero.battle(vampire)
            if hero.health > 0 and golem.health > 0:
                if enemy.health <= 0 and vampire.health <= 0:
                    print()
                print(f"{brown}{golem.name}{og} has dealt {brown}{damage(golem.attack, hero.defence)} damage{og}.")
                hero.battle(golem)
            if hero.health <= 0:
                print()
                print(f"{bold}Restart? (yes/no){og}")
                action = input()
                if action == "no":
                    break
                elif action == "yes":
                    done = False
                    savefile = loadhero()
                    hero = Hero(savefile[0], savefile[1], savefile[2], savefile[3], savefile[4], savefile[5], savefile[6], savefile[7], savefile[8], savefile[9], savefile[10])
                    enemy = Enemy("Enemy", 50+hero.floor, 5+hero.floor)
                    vampire = Vampire("Vampire", 50+hero.floor, 5+hero.floor)
                    golem = Golem("Golem", 100+hero.floor, 1+hero.floor)
                    print()
                    print(f"{bold}Floor {hero.floor}{og}")
                    print(f"{brown}{enemy.name}{og} has {brown}{enemy.health} health{og} and {brown}{enemy.attack} attack{og}.")
                    print(f"{brown}{vampire.name}{og} has {brown}{vampire.health} health{og} and {brown}{vampire.attack} attack{og}.")
                    print(f"{brown}{golem.name}{og} has {brown}{golem.health} health{og} and {brown}{golem.attack} attack{og}.")

    elif action == "stats":
        print()
        hero.checkStats()

    elif action == "shop":
        print()
        print(f"{bold}Would you like to access the {green}items section{og} {bold}or the{og} {green}spells section{og} {bold}of the shop?{og}")
        section = input()

        if section == "items":
            print()
            print(f"{bold}Would you like to buy or sell?{og}")

            choice = input()
            if choice == "buy":
                buying = ""
                while buying != "done":
                    print()
                    print(f"{bold}What would you like to buy?{og} {green}{itembuy}{og} {green}Coins: {hero.coin}{og} {italic}Input 'done' to stop{og}")
                    buying = input()
                    if buying == "done":
                        print(f"{italic}Exited.{og}")
                        print()
                        break
                    elif buying not in itembuy:
                        print(f"{italic}That item is not in the shop. Please try again.{og}")
                    else:
                        if itembuy.get(buying) > hero.coin:
                            if hero.coin == 1:
                                print(f"{italic}Sorry, you don't have enough money. You only have {green}{hero.coin} coin{og}")
                            else:
                                print(f"{italic}Sorry, you don't have enough money. You only have {green}{hero.coin} coins{og}")
                        else:
                            print(f"{italic}Bought {buying}{og}")
                            hero.loot.append(buying)
                            hero.coin -= itembuy.get(buying)

            if choice == "sell":
                selling = ""
                while selling != "done":
                    print()
                    print(f"{bold}What would you like to sell?{og} {green}{clean(hero.loot)}{og} {italic}Input 'done' to stop{og}")
                    selling = input()
                    if selling == "done":
                        print(f"{italic}Exited.{og}")
                        print()
                        break
                    elif selling not in hero.loot:
                        print(f"{italic}You do not own that item. Please try again.{og}")
                    else:
                        hero.coin += itemsell.get(selling)
                        hero.loot.remove(selling)
                        print(f"{italic}Sold {selling}. {green}Gained {itemsell.get(selling)} coins!{og}")

        elif section == "spells":
            print()
            print(f"{bold}Would you like to buy or sell?{og}")

            choice = input()
            if choice == "buy":
                buying = ""
                while buying != "done":
                    print()
                    print(
                        f"{bold}What would you like to buy?{og} {green}{spellbuy}{og} {green}Coins: {hero.coin}{og} {italic}Input 'done' to stop{og}")
                    buying = input()
                    if buying == "done":
                        print(f"{italic}Exited.{og}")
                        print()
                        break
                    elif buying not in spellbuy:
                        print(f"{italic}That spell is not in the shop. Please try again.{og}")
                    else:
                        if spellbuy.get(buying) > hero.coin:
                            if hero.coin == 1:
                                print(
                                    f"{italic}Sorry, you don't have enough money. You only have {green}{hero.coin} coin{og}")
                            else:
                                print(
                                    f"{italic}Sorry, you don't have enough money. You only have {green}{hero.coin} coins{og}")
                        else:
                            print(f"{italic}Bought {buying}{og}")
                            hero.spell.append(buying)
                            hero.coin -= spellbuy.get(buying)

            if choice == "sell":
                selling = ""
                while selling != "done":
                    print()
                    print(
                        f"{bold}What would you like to sell?{og} {green}{clean(hero.spell)}{og} {italic}Input 'done' to stop{og}")
                    selling = input()
                    if selling == "done":
                        print(f"{italic}Exited.{og}")
                        print()
                        break
                    elif selling not in hero.spell:
                        print(f"{italic}You do not own that item. Please try again.{og}")
                    else:
                        hero.coin += spellsell.get(selling)
                        hero.spell.remove(selling)
                        print(f"{italic}Sold {selling}. {green}Gained {spellsell.get(selling)} coins!{og}")

    elif action == "equipment":
        i = 0
        while i != "done":
            print()
            print(f"{green}Inventory: {clean(hero.loot)}{og}")
            print(f"{green}Equipped: {clean(hero.equip)}{og}")
            print(f"{bold}What would you like to equip? Input 'done' to stop{og}")
            i = input()
            if i == "done":
                print(f"{italic}Exited.{og}")
                print()
                break
            elif i in hero.equip:
                print(f"{italic}You already have that equipped.{og}")
                continue
            elif i not in hero.loot:
                print(f"{italic}You do not own that item. Please try again.{og}")
                continue
            else:
                if i == "dagger":
                    dagger.equip()
                if i == "boots":
                    boots.equip()
                if i == "gloves":
                    gloves.equip()
                if i == "armour":
                    armour.equip()
                if i == "health potion":
                    healthp.equip()
                if i == "xp potion":
                    xpp.equip()

    elif action == "menu":
        print()
        print(f"{bold}Spells{og}")
        print(f"{green}Aura of The Guard:{og} {italic}A long time ago, a great civilization existed. However, it was destroyed at its peak. Now, the souls of the guards roam, their guilt causing them to forever wander. They will protect those who are similar to the citizens they were once in charge of. When you cast it, you can feel their aunguish and determination inside you.{og}")
        print(f"{green}Burst of Devouring:{og} {italic}There were once monsters who killed their own kind to become stronger, devouring their skills and abilities for themselves. They were destroyed due to their immense greed causing them to crave for the power of the gods. When you use this spell, although it is weak now, you can sense the power that once was.{og}")
        print(f"{green}Calling of Healing:{og} {italic}The holy power inside fills you with a sense of responsibility to protect everyone. Strangely enough though, it makes you desire peace with some of the monsters as well. It may be that they were once humans as well? You've never seen any history of that though.{og}")
        print(f"{green}Lunar Blaze:{og} {italic}Every time you cast this spell, you feel the 'Burst of Devouring' rampage. Perhaps this is a relic of the gods power? The gods are very protective and secretive over their abilities though, surely they would have noticed you using it by now and taken it back?{og}")

        print()
        print(f"{bold}Items{og}")
        print(f"{green}Armour:{og} {italic}It is dropped by golems. There is a strange symbol on the back with foreign words written underneath.{og}")
        print(f"{green}Boots:{og} {italic}It is dropped by enemies. It is suprisingly light despite its appearance. It seems to be made out of a foreign material.{og}")
        print(f"{green}Dagger:{og} {italic}It is dropped by vampies. Strange how they never attack with the dagger despite the fact that it is in their pockets. Furthermore, aren't vampires scared of silver?{og}")
        print(f"{green}Glove:{og} {italic}It is dropped by all the monsters. They look like normal fingerless gloves, but when you put them on, you can sense a stronger power within. For now, it is only slightly useful for better grip.{og}")

        print()
        print(f"{bold}Potions{og}")
        print(f"{green}Health Potion:{og} {italic}It is dropped by enemies. The glass is suprisingly sturdy, and the potion has a strange red glow. It can work well as a flashlight in this dark tower. Weaker vampies and golems seem to be afraid of it, so it works as a deterrent. The stronger ones seem reluctant to approach it, but will still fight you nonetheless.{og}")
        print(f"{green}XP Potion:{og} {italic}It is dropped by enemies. The glass is suprisingly sturdy, and the potion has a strange blue glow. It can work well as a flashlight in this dark tower. Although enemies carry it around, they never seem to use it for themselves. Perhaps they just like the glow? It seems to attract vampires and golems as well, although they don't drink it either.{og}")

    action = input()

print()
print(f"You gained {green}{hero.xp} XP{og} and got to {brown}floor {hero.floor}{og}!")

if hero.health > 0:
    print()
    print(f"{bold}Do you want to save your progress? (yes/no){og}{italic} This will overwrite your previous one{og}")

    saving = input()
    if saving == "yes":
        save()