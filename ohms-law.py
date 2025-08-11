# ohms_law.py
# Description: Simple program to calculate Voltage (V) using Ohm's Law: V = I * R
# Get user input for current and resistance
current = float(input("Enter the current (in A): "))
resistance = float(input("Enter the resistance (in ohms): "))
# Calculate voltage
voltage = current * resistance
# Display result
print(f"The voltage is: {voltage} volts")
# End of ohms_law.py
# This program calculates the voltage based on user input for current and resistance using Ohm's Law