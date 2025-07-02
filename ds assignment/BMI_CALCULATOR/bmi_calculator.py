def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    # Get user input and units
    unit_system = input("Enter 'metric' for kilograms and meters, or 'imperial' for pounds and inches: ").strip().lower()

    try:
        if unit_system == "metric":
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
        elif unit_system == "imperial":
            weight = float(input("Enter your weight in pounds (lbs): "))
            height = float(input("Enter your height in inches (in): "))

            # Convert to metric
            weight *= 0.453592  # lbs to kg
            height *= 0.0254    # in to meters
        else:
            print("Invalid unit system. Please enter 'metric' or 'imperial'.")
            return

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        # Determine category and give health tips
        if bmi < 18.5:
            category = "Underweight"
            tip = "You may need to gain some weight. Consider consulting a healthcare provider for personalized advice."
        elif bmi < 25:
            category = "Normal"
            tip = "Great job! Maintain a balanced diet and regular physical activity."
        elif bmi < 30:
            category = "Overweight"
            tip = "Try to be more active and consider healthier eating habits to manage your weight."
        else:
            category = "Obese"
            tip = "It’s important to speak with a healthcare provider. Small lifestyle changes can have a big impact."

        # Output category and tip
        print(f"Category: {category}")
        print(f"Health Tip: {tip}")

    except ValueError:
        print("Please enter valid numbers for weight and height.")

# Call the function to run the calculator
if __name__ == "__main__":
    calculate_bmi()
