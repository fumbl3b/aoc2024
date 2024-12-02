arr = []
with open('./input.txt', 'r') as file:
    arr = file.readlines()
    for idx, line in enumerate(arr):
        arr[idx] = [int(num) for num in line.split()]

num_unsafe = 0

for report in arr:
    prev = None
    direction = None
    for n in report:
        if direction is None and prev is not None:
            if n > prev:
                direction = 'INCREASING'
            elif n < prev:
                direction = 'DECREASING'
        if prev is not None and direction is not None:
            if abs(n - prev) > 3:
                num_unsafe += 1
                print(f"{report} unsafe, change too great")
                break
            if direction == 'INCREASING' and prev > n:
                num_unsafe += 1
                print(f"{report} unsafe, change in direction")
                break
            if direction == 'DECREASING' and prev < n:
                num_unsafe += 1
                print(f"{report} unsafe, change in direction")
                break
        prev = n
    # print(f"Report: {report}, Unsafe Count: {num_unsafe}")


print('safe reports = ', len(arr) - num_unsafe)
