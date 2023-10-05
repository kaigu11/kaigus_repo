#KAIGU ANN WANGARI SCT 211-0772/2022
#tip calculator

totalBill = float(input("Enter the total bill: "))
print("Enter the percentage of tip given: ")
print("10\t,12\t or 15\n")
choice = int(input())
totalTip = ((choice*totalBill)/100)
billAfterTip = totalBill+totalTip
numOfPeople = int(input("\nEnter the number of people splitting the bill:"))
eachPay = float(billAfterTip/numOfPeople)
roundedEachPay = round(eachPay,2)
print("\n\nThe amount each person should pay is:", roundedEachPay)
