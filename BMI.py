print("### Are You at a Healthy Weight? ###")
weight=float(input("Weight (kg):"))
height=float(input("height (m):"))
BMI = weight/(height*height)
if BMI <= 17:
    print("Your Body Mass Index (BMI) is",round (BMI, 0),"you are underweight.")
elif BMI < 25:
    print("Your Body Mass Index (BMI) is",round (BMI, 0),"you are healthy weight.")
elif BMI < 30:
    print("Your Body Mass Index (BMI) is",round (BMI, 0),"you are overweight.")
elif BMI < 40:
    print("Your Body Mass Index (BMI) is",round (BMI, 0)," you are Obese.")
else:
    print("Your Body Mass Index (BMI) is",round (BMI, 0),"you are severely obese.")