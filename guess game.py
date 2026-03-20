secret_word="thailand"
guess=""
guess_count=0
guess_limit=5
guess_limit_over=False
while guess!=secret_word and not(guess_limit_over):
    if guess_count<guess_limit:
            guess = input("guess the country:")
            guess_count += 1
    else:
            guess_limit_over=True

if guess_limit_over:
        print("dont lose hope better luck next time")
else:
    print(f"You win a trip to {guess}")
