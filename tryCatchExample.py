#Try Catch Example

no = input("Enter a no: ")
try:
    convert = int(no)
except:
    convert = -1
if convert > 0:
        print("Good Job!")
else:
    print("Not a no")