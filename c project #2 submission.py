import random
print("One player dice game, Play to win special prize")

player1_user = input("Player 1 enter name here")

dice_per_roll = 3 
rolls = 1000; 
for i in range (3, rolls):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    a=[die1, die2, die3] 
    b=sum(a)
    print(b)

dice_faces = (1, 2, 3, 4, 5, 6)

random.choice(dice_faces)

roll_results = []
roll_counts = {1: 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
rolls = 0
while rolls < 10:
    this_roll = random.choice(dice_faces)
    roll_results.append(this_roll)
    roll_counts[this_roll] += 1
    rolls += 1

    print(roll_results)
    print(roll_counts)


    def roll_dice(num_dice):
        roll_results = []
        for _ in range(num_dice):
            roll = random.randiant(1,6)
            roll_results.append(roll)
            return roll_results
        
Number_of_rolls = input("What are your dice results, let's find out")
while Number_of_rolls:
    Die = str(random.randint(1,6))
    print(" Roll results")
if Die == "2" or Die == "2" or Die == "2": 
     print("Tupled out!")
elif Die == "5" or Die == "5" or Die == "5":
    print("Tupled out, you lose")

while Number_of_rolls: 
    Die = str(random.randint(1,6))
if Die == "1" or Die == "1" or Die == "1":
    print("fixed result, cannot continue")

    print("Continue to play as long as you like")
guessing = 0
score = guessing()
guess = 0
while dice_per_roll < 3: 
    number = random.randint(1,2)
dice_per_roll += 1
print(f"Round{dice_per_roll}")
if guess == number:
    print("Good job")
score == 1
elif
print("Don't recommend this move, maybe try again")
print()
print(f"Your score{score[0]} out of {score[1]} games.")

average = sum / dice_per_roll
print("You lose!!")
    




