height = input("Enter the heights in meter:-  ")
weight = input("Enter the weights in Kg:-  ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
bmi = round(bmi_as_int)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
