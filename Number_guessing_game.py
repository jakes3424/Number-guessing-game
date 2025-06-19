import random

def main():
    number = random.randint(1, 100)
    attempts = 0
    print("🎯 Guess the Number (1 to 100)")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("🔼 Too low!")
        elif guess > number:
            print("🔽 Too high!")
        else:
            print(f"✅ Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    main()
