
data = []

with open('input.txt', 'r') as f:
    for line in f:
        left, right = line.split(':')
        total = int(left.strip())
        nums = [int(n) for n in right.strip().split()]
        data.append({'total': total, 'nums': nums})

calibration_result = 0

for equation in data:
    target = equation['total']
    nums = equation['nums']

    # If only one number, just check it directly (depending on puzzle interpretation):
    if len(nums) == 1:
        if nums[0] == target:
            calibration_result += target
        continue

    # Number of operator positions:
    op_count = len(nums) - 1
    # We'll use a binary representation to iterate over all operator combinations
    # 0 -> '+', 1 -> '*'
    from itertools import product
    
    operators = list(product(['+', '*'], repeat=op_count))

    can_solve = False
    for ops in operators:
        # Evaluate the expression left-to-right
        result = nums[0]
        for i, op in enumerate(ops, start=1):
            if op == '+':
                result = result + nums[i]
            else:  # op == '*'
                result = result * nums[i]
        
        if result == target:
            can_solve = True
            break

    if can_solve:
        calibration_result += target

print(calibration_result)
