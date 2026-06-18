def angleClock(hour: int, minutes: int) -> float:
    """
    Calculate the smaller angle (in degrees) between the hour hand and the minute hand
    on a clock given the time (hour, minutes).

    Clock facts:
      - A full circle is 360 degrees.
      - The minute hand moves 360 degrees in 60 minutes → 6 degrees per minute.
      - The hour hand moves 360 degrees in 12 hours → 30 degrees per hour,
        and also moves as minutes pass: 30 degrees in 60 minutes → 0.5 degrees per minute.

    Algorithm:
      1. Compute the angle of the minute hand from 12 o'clock:
         min_angle = minutes * 6
      2. Compute the angle of the hour hand from 12 o'clock:
         hour_angle = (hour % 12) * 30 + (minutes * 0.5)
      3. Compute the absolute difference:
         diff = abs(hour_angle - min_angle)
      4. The smaller angle is min(diff, 360 - diff).

    Returns:
        The smaller angle in degrees as a float.
    """
    # Minute hand: 6 degrees per minute
    min_angle = minutes * 6

    # Hour hand: 30 degrees per hour + 0.5 degrees per minute
    hour_angle = (hour % 12) * 30 + (minutes * 0.5)

    # Absolute difference between the two angles
    diff = abs(hour_angle - min_angle)

    # Return the smaller angle (clock has two angles between hands)
    return min(diff, 360 - diff)


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
hour1 = 12
minutes1 = 30
print("hour1 =", hour1)
print("minutes1 =", minutes1)
print("angleClock =", angleClock(hour1, minutes1))
# min_angle = 30 * 6 = 180
# hour_angle = 0 * 30 + 30 * 0.5 = 15
# diff = 165, min(165, 195) = 165

hour2 = 3
minutes2 = 30
print("\nhour2 =", hour2)
print("minutes2 =", minutes2)
print("angleClock =", angleClock(hour2, minutes2))
# min_angle = 30 * 6 = 180
# hour_angle = 3 * 30 + 30 * 0.5 = 90 + 15 = 105
# diff = 75, min(75, 285) = 75

hour3 = 3
minutes3 = 0
print("\nhour3 =", hour3)
print("minutes3 =", minutes3)
print("angleClock =", angleClock(hour3, minutes3))
# min_angle = 0
# hour_angle = 3 * 30 + 0 = 90
# diff = 90, min(90, 270) = 90

hour4 = 12
minutes4 = 0
print("\nhour4 =", hour4)
print("minutes4 =", minutes4)
print("angleClock =", angleClock(hour4, minutes4))
# min_angle = 0
# hour_angle = 0 * 30 + 0 = 0
# diff = 0, min(0, 360) = 0

hour5 = 6
minutes5 = 0
print("\nhour5 =", hour5)
print("minutes5 =", minutes5)
print("angleClock =", angleClock(hour5, minutes5))
# min_angle = 0
# hour_angle = 6 * 30 = 180
# diff = 180, min(180, 180) = 180

# Detailed trace for hour=3, minutes=30
print("\nDetailed trace for hour=3, minutes=30:")
hour = 3
minutes = 30

min_angle = minutes * 6
hour_angle = (hour % 12) * 30 + (minutes * 0.5)
diff = abs(hour_angle - min_angle)
result = min(diff, 360 - diff)

print(f"min_angle = {minutes} * 6 = {min_angle}")
print(f"hour_angle = ({hour} % 12) * 30 + {minutes} * 0.5 = {hour_angle}")
print(f"diff = |{hour_angle} - {min_angle}| = {diff}")
print(f"min({diff}, 360 - {diff}) = {result}")