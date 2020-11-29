#Taking Inputs From Users

name = input("What's your name?");
weather = input("What's up  with the weather?");
print(f'{name} says "{weather}"');

#Small Excersice (Europe Floor -> US Floor)
europe = input("Europe: In which floor you are in?");
us = int(europe) + 1;
print(f'US: you are in {us} floor');

#Small Excersice (Hour -> Pay)
hour = input("How many hours have you worked?");
rate = input("What's the current  rate?");
pay = float(hour) * float(rate);
print(f'Here,s your pay ${pay}');
