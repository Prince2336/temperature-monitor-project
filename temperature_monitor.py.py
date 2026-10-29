 # Temperature Monitor and Alarm Checker
# ND1 Mechatronics Engineering, YabaTech

def temperature_monitor():
    print("===================================")
    print(" TEMPERATURE MONITOR AND ALARM")
    print("===================================")

    # Example temperature limit for this project
    safe_limit = 60

    # Create a list to store temperature readings
    temperatures = []

    # Collect five valid temperature readings
    for i in range(5):
        while True:
            try:
                reading = float(
                    input(f"Enter temperature {i + 1} in Celsius: ")
                )
                temperatures.append(reading)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Display all temperature readings
    print("\nAll temperature readings:", temperatures)

    # Calculate temperature statistics
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("Highest temperature:", highest, "°C")
    print("Lowest temperature:", lowest, "°C")
    print("Average temperature:", round(average, 2), "°C")

    # Check the overall machine status
    if highest > safe_limit:
        print("WARNING: Temperature is too high!")
        print("Machine status: CRITICAL")
    else:
        print("Machine status: NORMAL")

    # Identify readings that exceed the limit
    print("\nChecking individual readings:")

    for i in range(len(temperatures)):
        if temperatures[i] > safe_limit:
            print("Alert: Reading", i + 1, "is too high!")

    print("\nTemperature monitoring complete.")


# Run the program
temperature_monitor()