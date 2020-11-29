#US Election Voting System
name = input("What's your name?")
age = int(input("What's your age?"))
if age < 100 and age > 0:
        if age >= 18: 
               print(f'{name} is allowed to vote!')
        else: 
               print(f'{name} is not allowed this year!')
else: 
    print(f'{name}, Please enter a proper age!');