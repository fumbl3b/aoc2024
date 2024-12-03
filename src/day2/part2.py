def is_safe(levels):

    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]

    # Check for equal adjacent levels
    if any(d == 0 for d in diffs):
        return False

    # Check if all increasing
    if all(d > 0 and 1 <= d <= 3 for d in diffs):
        return True

    # Check if all decreasing
    if all(d < 0 and 1 <= -d <= 3 for d in diffs):
        return True

    return False

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True

    return False

# Read input data and count safe reports
safe_reports = 0

with open('input.txt') as f:
    for line in f:
        levels = list(map(int, line.strip().split()))
        if is_safe_with_dampener(levels):
            safe_reports += 1

print("safe reports = ", safe_reports)
