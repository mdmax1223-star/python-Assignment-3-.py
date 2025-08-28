import math

# Step 1: Ask the user for a number as input
try:
    num = float(input("Enter a number: "))

    # Step 2: Perform calculations using math module
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sine_result = math.sin(num)

    # Step 3: Display the results
    print("\nResults:")
    print(f"Square root of {num} = {sqrt_result}")
    print(f"Natural logarithm (log base e) of {num} = {log_result}")
    print(f"Sine of {num} (in radians) = {sine_result}")

except ValueError:
    print("Please enter a valid positive number.")
except Exception as e:
    print(f"An error occurred: {e}")
