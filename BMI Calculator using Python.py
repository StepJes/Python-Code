# Program to calculate BMI
 
# Getting Inputs:
height = int(input('Enter height: '))
weight = int(input('Enter weight: '))

# Function to calculate BMI
def BMICalculator(height, weight):
    bmi = weight/(height**2)
    return bmi

# Calling BMI function
bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ", end='')
