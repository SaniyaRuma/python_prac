weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() =="K":
    weight /= 0.45
    print("Weight in pound is: "+ str(weight))
else:
    weight *= 0.45
    print("Weight in kg is: "+ str(weight))
