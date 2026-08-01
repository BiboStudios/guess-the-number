import random
n=random.randint(1,100)
b=int(input("Guess a number between 1 and 100: "))
count=0
while b!=n:
    count+=1
    if b!=n:
        if b<n:
            print("Too low!")
        else:
            print("Too high!")
    b=int(input("Guess again: "))
print(f"Congratulations! You've guessed the number {n} in {count} attempts.")