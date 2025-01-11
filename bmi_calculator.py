# BMI calculator 
name01 = "Nuruddeen"
height01 = 4
weight01 = 70

# second person 
name02 = "Arabee"
height02 = 3
weight02 = 140

# third person 
name03 = "Zakari"
height03 = 2.7
weight03 = 170

# defining BMI calculator 
def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 27:
        return name + " is not overweight"
    else:
        return name + " is overweight" 
# evaluation 
first_result = bmi_calculator(name01, weight01, height01)
second_result = bmi_calculator(name02, weight02, height02)
third_result = bmi_calculator(name03, weight03, height03)


# our final result evaluation 
print(first_result)
print(second_result)
print(third_result)