import random
# Let's simulate roll 100 dice and print out each dice value
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

for rolls in range(100):
    dice = random.randint(1, 6)
    if dice == 1:
        ones += 1
    elif dice == 2:
        twos += 1
    elif dice == 3:
        threes += 1
    elif dice == 4:
        fours += 1
    elif dice == 5:
        fives += 1
    else:
        sixes += 1
    print(dice)
print(f"You rolled {ones} 1s, {twos} 2s, {threes} 3s, {four} 4s, {five} 5s, and {sixes} 6s")
#Now, let's count how many 1s, 2s, 3s, 4s, 5s, and 6s were rolled