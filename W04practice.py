## W04 Checkpoint Practice 
# f_temperature = float(input("What is the temperature in Fahrenheit? "))
# c_temp_conversion = (f_temperature - 32) * 5/9

# print (f"The temperature in Celsius is {c_temp_conversion:.1f} degrees.")

## W04 Team Activity
import math
print(f"Welcome to the velocity calculator. Please enter the following: ")
print()

mass = float(input ("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in second): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float (input ("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c_value = (1/2) * density * cross_sectional_area * drag_constant

print (f"The inner value of c is: {c_value:.3f}")

velocity = math.sqrt(mass * gravity / c_value) * (1 - math.exp ((-math.sqrt(mass * gravity * c_value) / mass) * time))

print(f"The velocity after {time:.1f} seconds is: {velocity:.3f} m/s")