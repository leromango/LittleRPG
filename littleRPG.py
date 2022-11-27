import random
 
def enemy_creation(lvl):
    global enemy
    enemy = {
        "Dmg": (random.randrange(0,lvl+1))+(lvl//5+1),
        "Health": (random.randrange(0,lvl+1))+(lvl//5+1)
    }

def attackCalc(type, luck, lvl, dmg):
    if lvl < 10:
        checker = 1
    else:
        checker = lvl/10
    if luck < 30:
        luckchecker = 1
    else:
        luckchecker = luck
    if type == "heavy":
        value = lvl + lvl*checker + (luckchecker//20)*checker + dmg
    elif type == "light":
        value = lvl*checker + dmg + luckchecker//30
    elif type == "monster":
        value = checker + (checker*2*lvl)//luckchecker + dmg
    return value

def attack(type):
    x = False
    hitDmg = attackCalc(type, char["luck"], lvl, char["damage"])
    enemy["Health"] = enemy["Health"] - hitDmg
    print("You have dealt", hitDmg, "damage!")
    if type == "heavy":
        skip = 2
    else: 
        skip = 1
    for i in range (skip):
        hitDmg = attackCalc("monster", char["luck"], lvl, enemy["Dmg"])
        char["health"] = int(char["health"]) - hitDmg
        print("Monster have dealt you", hitDmg, "damage!")
        if char["health"] > 0:
            print("You have", char["health"], "health left!")
        else:
            print("Game Over...")                        
            game = False
            exit()
global game
global x
game = True

print("Welcome to Mango's littleRPG")
expPoints = 10
print("Create your character first.")
print("How many points do you want to spend on your character's damage? You have ", expPoints, "experience points.")

x = True
while x:
    inputDmg = input()
    if inputDmg.isdigit() and int(inputDmg) < expPoints and int(inputDmg) != 0:
        print("Good, you have used", inputDmg, "points to upgrade your strength")
        expPoints = expPoints - int(inputDmg)
        x = False
    else:
        print("Type in a correct number")
print("How many point do you want to spend on your character health? You have ", expPoints,"experience points.")

x = True
f = True
while f:
    while x:
        inputHealth = input()
        if inputHealth.isdigit() and int(inputHealth)<=expPoints and int(inputHealth) != 0:
            print("Good, you have used", inputHealth, "points to upgrade your health")
            expPoints = expPoints - int(inputHealth)
            x = False
            f = False
        else:
            print("Type in a correct number")

    if expPoints != 0:
        print("You still have ", expPoints, "points left, use them!")

char = {
    "damage": int(inputDmg),
    "health": int(inputHealth),
    "luck": random.randrange(1, 100),
    "lvl": 1
}
initHealth = char["health"]

print("This is your character:")
print("Your character's damage is", char["damage"])
print("Your character's health is", char["health"])
if char["luck"]<20:
    print("Your character is not lucky")
elif char["luck"]<50 and char["luck"]>=20:
    print("Your character is fairly lucky")
elif char["luck"]<80 and char["luck"]>=50:
    print("Your character is lucky")
elif char["luck"]>=80:
    print("Your character is very lucky")

print("Let's start!")
lvl = char["lvl"]
while True:
    if lvl <= 0:
        lvl = 1
    enemy_creation(lvl)
    print ("You have encountered a monster!")
    x = True
    while x:
        while enemy["Health"]>0:
            print ("What attack do you want to use? Heavy or Light?")
            attackType = str(input()).lower()
            if attackType == "light" or attackType == "heavy":
                attack(attackType)
            else:
                print("Incorrect command")
        if game:
            print("You have slayed the monster!")
    print("You have gained an XP point!")
    print("What do you want to upgrade health or damage?")
    x = True
    lvl = lvl + 1

    while x:
        upgradeinput = input()
        upgradeinput.lower
        char["lvl"] = char["lvl"] + 1
        if upgradeinput == "health":
            x = False
            char["health"] = initHealth + 1
            initHealth = char["health"]
            print("You health now is", initHealth)
        elif upgradeinput == "damage":
            x = False
            char["damage"] = char["damage"] + 1
            print("You damage now is", char["damage"])
        else:
            print("Incorrect command")