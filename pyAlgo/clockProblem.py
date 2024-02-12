def calcAngle(h, m):
    # Function to calculate the angle between the hour and minute hands of a clock

    if (h < 0 or m < 0 or h > 12 or m > 60):
        # Check for invalid input
        print('Invalid input. Hours should be between 0 and 12, and minutes should be between 0 and 60.')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1
        if(h > 12):
            h = h - 12

    # Calculate the angles of the hour and minute hands
    hour_angle = 0.5 * (h * 60 + m)  # 0.5 degrees per minute
    minute_angle = 6 * m  # 6 degrees per minute

    # Calculate the absolute difference between the hour and minute angles
    angle = abs(hour_angle - minute_angle)

    # Find the smaller angle between the two possibilities (clockwise and counterclockwise)
    angle = min(360 - angle, angle)
    angle2 = max(360 - angle, angle)

    return angle, angle2


h = int(input("Enter the time in hours (0-12): "))
m = int(input("Enter the time in minutes (0-60): "))

# Calculate the angles between the hour and minute hands
angle1, angle2 = calcAngle(h, m)

# Print the results
print(f"Angle between hour and minute hand: {angle1:.2f} degrees")
print(f"Angle between minute and hour hand: {angle2:.2f} degrees")