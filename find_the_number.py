import random
computers_number = random.randint(1,100)
auto_guess = random.randint(1,100)
count = 0
while True:
    count += 1
    print(f"auto guessed: {auto_guess}")
    if auto_guess < computers_number:
            print("Too low!")
            auto_guess = random.randint(auto_guess,computers_number+1)
    elif auto_guess > computers_number:
            print("Too high!")
            auto_guess = random.randint(computers_number,auto_guess+1)
    else:
        print("Correct! The computer guessed the number.")
        print(f"Number of attempts: {count}")
        print(f"The computer's number was: {computers_number}")
        break   