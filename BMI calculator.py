height = input("Enter the heights in meter:-  ")
weight = input("Enter the weights in Kg:-  ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print("Your Body mass index (BMI) Is ",bmi_as_int)
