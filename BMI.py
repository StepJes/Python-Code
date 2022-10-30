def input_variables():
  
  print("Name:")
  name = input("Enter the name of the person.")
  
  print("Age:")
  age = int(input("Enter the age of the person."))

  print("Sex:")
  sex = input("Enter sex: M for male, F for female, O for non binary.")
  while sex!= 'M' and sex!='F' and sex!='O':
    print("Incorrect choice.")
    sex = input("Enter sex: M for male, F for female, O for non binary.")
  
  print("Weight:")
  unit_weight = input("Press 1 for kilograms, 2 for pounds.")
  while unit_weight!= '1' and unit_weight!='2':
    print("Incorrect choice.")
    unit_weight = input("Press 1 for kilograms, 2 for pounds.")
  if unit_weight == '1':
    weight_in_kg = float(input("Enter the weight of the person in kilograms."))
  else:
    weight_in_kg = float(input("Enter the weight of the person in pounds."))*0.453592
    
  print("Height:")
  unit_height = input("Press 1 for meters and centimeters, 2 for feet and inches")
  while unit_weight!= '1' and unit_weight!='2':
    print("Incorrect choice.")
    unit_height = input("Press 1 for meters and centimeters, 2 for feet and inches")
  if unit_height == '1':
    height_in_m = float(input("Enter the height of the person in meters.")) + float(input("Enter the remaining height of the person in centimeters"))*0.01
  else:
    height_in_m = (float(input("Enter the height of the person in feet"))*12 + float(input("Enter the remaining height of the person in inches")))*0.0254

  return name, age, sex, weight_in_kg, height_in_m

def calculate_BMI(info):
  wt = info[3]
  ht = info[4]
  BMI = wt/(ht**2)

  return BMI

def find_body_state(BMI):
  if BMI<18.5:
    body_state = 'underweight'
  elif BMI<24.9:
    body_state = 'normal'
  elif BMI<29.9:
    body_state = 'overweight'
  else:
    body_state = 'obese'

  return body_state

def output():
  info = input_variables()
  BMI = calculate_BMI(info)
  body_state = find_body_state(BMI)

  print("Name: {}\nAge: {}\nGender: {}\nWeight(in kg): {:.3f}\nHeight(in m): {:.2f}\nBody Mass Index: {:.2f}\nAcoording to your body mass index, you are {}.".format(info[0], info[1], info[2], info[3], info[4], BMI, body_state))

output()
  