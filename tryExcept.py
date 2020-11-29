#First Case (Something is wrong)
greetings = "Hello Bob,"
try:
    convert = int(greetings)
except:
    print("I Knew this won't work")
#Second Case (Nothing is wrong)
noOranges = 25;
noGrapes = 50;
try:
    fruitBasket = noOranges + noGrapes;
    print(f'There are totallt {fruitBasket} no of fruits in basket');
except:
    print("There are no fruits in basket!");