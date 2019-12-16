cost1=int(input("how much is that first item "))
cost2=int(input("how much is that other item "))
amountbeingpaid=int(input("how much are you paying "))
cost = cost1 + cost2
print("it will cost",cost)
if cost < (amountbeingpaid):
    print ("your change is", (amountbeingpaid - cost))
else:
    print("sorry. you are too poor for these items")
