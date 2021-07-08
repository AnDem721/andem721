import random
random_number = random.randint(1, 100)
point_counter = 5
for x in range(6):
    while True:
        print(random_number)
        user_guess = int(input("Give number between 1-100 -> "))
        if user_guess < random_number:
            print("too low")
            point_counter =- 1
        elif user_guess > random_number:
            print("too high")
            point_counter =- 1
        elif user_guess == random_number:
            print(f"awesome, congrats! You'ce got {point_counter * 10 + 10} points")
        break
