print("Welcome to BMI calculator!")
your_weight = input("Enter your weight(kg) - ")
your_height = input("Enter your height(m) - ")

BMI = float(your_weight)*10000/float(your_height)**2
rounded_BMI = round(BMI,1)
print(rounded_BMI)

if float(rounded_BMI) <= 18.5:
    print(f'Your BMI is {rounded_BMI}. You are Underweight.')
elif  float(rounded_BMI)> 18.5 and float(rounded_BMI) <= 25:
    print(f'Your BMI is {rounded_BMI}. You are Underweight.')
else:
    print(f'Your BMI is {rounded_BMI}.')

