print("UNIT CONVERTER")

print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = int(input("Enter your choice: "))

value = float(input("Enter the value: "))

if choice == 1:
    result = value * 0.621371
    print("Miles =", result)

elif choice == 2:
    result = (value * 9/5) + 32
    print("Fahrenheit =", result)

elif choice == 3:
    result = value * 2.20462
    print("Pounds =", result)

else:
    print("Invalid choice")
