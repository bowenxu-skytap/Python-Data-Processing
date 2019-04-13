from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
target = randint(1, 100)
guesses = []
while True:
    cur_guess = int(input('Please enter your guess: '))
    guesses.append(cur_guess)
    if cur_guess < 1 or cur_guess > 100:
        print('OUT OF BOUNDS')
        continue
    if cur_guess == target:
        break
        
    if len(guesses) == 1:
        if abs(cur_guess - target) <= 10:
            print('WARN!')
        else:
            print('COLD!')
    else:
        if abs(cur_guess - target) < abs(guesses[-2] - target):
            print('WARMER!')
        else:
            print('COLDER!')


print(f'Great! You have guessed correctly. The target is {cur_guess}, and it takes you {len(guesses)} guesses')
