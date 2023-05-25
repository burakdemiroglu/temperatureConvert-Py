unit = input("Celcius or Fahrenheit")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"{temp} Fahrenheit")
elif unit == "F":
    temp = (temp - 32) * 5 /9
    print(f"{temp} Celcius")
else:
    print(f"{unit} is an invalid unit")
