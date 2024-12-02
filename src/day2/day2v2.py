def is_safe(report):
    # Initialize variables to track direction
    increasing = True
    decreasing = True

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        # Check if the difference is valid
        if diff < 1 or diff > 3:
            return False

        # Check for direction consistency
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    # Report is safe if it's strictly increasing or strictly decreasing
    return increasing or decreasing


# Read input data
with open('./input.txt', 'r') as file:
    reports = [
        [int(num) for num in line.split()]
        for line in file.readlines()
    ]

# Count the number of safe reports
safe_count = sum(1 for report in reports if is_safe(report))

print("safe reports =", safe_count)
