#Gender Liking Machine
name = input("What's your name?")
print(f'Hello {name},')
print("NOTE: Type M (for male)")
print("      Type F (for female)")
print("      Type MF (for both)")

gender = input("Your gender: ").upper()
like = input("Your like: ").upper()

if gender == 'M' and like == 'F': 
    print(f'Congrats {name}, You are Straight')
elif gender == 'F' and like == 'M':
    print(f'Congrats {name}, You are Straight')
elif gender == 'M' and like == 'M':
    print(f'Congrats {name}, You are Gay')
elif gender == "F" and like == 'F': 
    print(f'Congrats {name}, You are Lesbian')
elif gender == "M" and like == "MF":
    print(f'Congrats {name}, You are Bisexual')
elif gender == "F" and like == "MF":
    print(f'Congrats {name}, You are Bisexual')
else:
    print("You are an Alien!")
    
