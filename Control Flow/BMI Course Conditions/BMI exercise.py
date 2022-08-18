print("Welcome to BMI calculator!")
your_weight = input("Enter your weight(kg) - ")
your_height = input("Enter your height(m) - ")

BMI = float(your_weight)/float(your_height)**2
rounded_BMI = round(BMI,1)
#print(rounded_BMI)

if rounded_BMI <= 18.5:
    print(f'Your BMI is {rounded_BMI}. You are Underweight.')
elif  rounded_BMI> 18.5 and float(rounded_BMI) <= 25:
    print(f'Your BMI is {rounded_BMI}. You are Normal.')
elif rounded_BMI> 25 and float(rounded_BMI) <= 30:
    print(f'Your BMI is {rounded_BMI}. You are Overweight.')
elif rounded_BMI> 30:
    print(f'Your BMI is {rounded_BMI}. You are Obese.')
else:
    print(f'Your BMI is {rounded_BMI}. Not in any category')

