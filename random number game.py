import random 

def random_number_game():
    print("Try and guess my number!")

    while True:  # Outer loop for replay
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guess = None

        print("\nI'm thinking of a number between 1 and 100. Can you guess it?")

        while guess != number_to_guess:
            try:
                guess = int(input("Enter your number: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.\n")

                elif guess > number_to_guess:
                    print("Too high! Try again. \n")
    
                else:
                    print(f"Correct! The number was {number_to_guess}.")
                    print(f"You guessed it in {attempts} attempts.")

            except ValueError:
                print("Please enter a valid number.\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye")
            break  

                
if __name__ == "__main__":
    random_number_game()

