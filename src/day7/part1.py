data = []

with open('input.txt', 'r') as f:
    for line in f:
        # Parse each line: "total: num1 num2 ..."
        left, right = line.split(':')
        total = int(left.strip())
        nums = [int(n) for n in right.strip().split()]
        data.append({'total': total, 'nums': nums})

calibration_result = 0

test_data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''



for equation in data:
    target = equation['total']
    nums = equation['nums']

    # DP approach
    # dp[i] = set of possible results using the first i numbers
    dp = [set() for _ in range(len(nums) + 1)]
    dp[1] = {nums[0]}

    for i in range(1, len(nums)):
        current_num = nums[i]
        # For each possible value so far, extend with + and *
        new_results = set()
        for val in dp[i]:
            new_results.add(val + current_num)
            new_results.add(val * current_num)
        dp[i+1] = new_results
    # After filling dp, check if target is in dp[len(nums)]
    if target in dp[len(nums)]:
        print(f"{target} works")
        calibration_result += target

print(calibration_result)
