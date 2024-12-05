import subprocess

def get_correct_orders_from_output(output):
    """
    Parse the output from the scripts. We expect lines like:
    Correct orders:
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    We'll return a set of tuples for easy comparison.
    """
    lines = output.strip().split("\n")
    correct_orders_found = False
    correct_orders = []

    for line in lines:
        line = line.strip()
        if line.lower().startswith("correct orders"):
            correct_orders_found = True
            continue
        if correct_orders_found and line:
            # Parse the order line like "75,47,61,53,29"
            pages = tuple(int(x.strip()) for x in line.split(","))
            correct_orders.append(pages)

    return set(correct_orders)

# Run part1.py
result_part1 = subprocess.run(["python3", "part1.py"], capture_output=True, text=True)
output_part1 = result_part1.stdout

# Run part1_gpt.py
result_part1_gpt = subprocess.run(["python3", "part1_gpt.py"], capture_output=True, text=True)
output_part1_gpt = result_part1_gpt.stdout

# Parse the correct orders
correct_orders_part1 = get_correct_orders_from_output(output_part1)
correct_orders_gpt = get_correct_orders_from_output(output_part1_gpt)

# Compare
if correct_orders_part1 == correct_orders_gpt:
    print("Both approaches produced the exact same set of correct orders.")
else:
    # Find differences
    only_in_part1 = correct_orders_part1 - correct_orders_gpt
    only_in_gpt = correct_orders_gpt - correct_orders_part1

    if only_in_part1:
        print("Orders only found in part1.py's output:")
        for order in only_in_part1:
            print(order)

    if only_in_gpt:
        print("Orders only found in part1_gpt.py's output:")
        for order in only_in_gpt:
            print(order)

    # Print a summary
    print("Number of correct orders in part1.py:", len(correct_orders_part1))
    print("Number of correct orders in part1_gpt.py:", len(correct_orders_gpt))
