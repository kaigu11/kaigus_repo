#KAIGU ANN WANGARI SCT 211-0772/2022
#BMI calculator

print("Enter your weight in kilograms:")
weight = float(input())
print("Enter your height in metres:")
height = float(input())
BMI = float(weight/(height*height))
if BMI < 18.5:
    print("You are underweight")
elif (BMI >= 18.5) and (BMI <= 24.9):
    print("Your weight is normal")
elif BMI >= 25 and BMI <=29.9:
    print("You are overweight")
else:
    print("You are obese")
