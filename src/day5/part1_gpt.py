# Read input from file
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

# Separate out the rule lines and update lines
rule_lines = [line for line in lines if '|' in line]
update_lines = [line for line in lines if ',' in line]

# Parse rules
rules = []
for line in rule_lines:
    a_str, b_str = line.split('|')
    a, b = int(a_str.strip()), int(b_str.strip())
    # a must appear before b
    rules.append((a, b))

# Parse updates
updates = []
for line in update_lines:
    pages = [int(x.strip()) for x in line.split(',')]
    updates.append(pages)

def is_correct_order(update, rules):
    # Check each rule against this update
    for (a, b) in rules:
        # Only consider the rule if both pages appear in the update
        if a in update and b in update:
            if update.index(a) > update.index(b):
                # a does not appear before b
                return False
    return True

correct_updates = [u for u in updates if is_correct_order(u, rules)]

print(len(correct_updates))
if correct_updates:
    # Sum the middle elements of each correct update
    # Middle page: u[len(u)//2]
    result = sum(u[len(u)//2] for u in correct_updates)
    print(result)
else:
    print(0)

print("Correct orders:")
for order in correct_updates:
    print(",".join(map(str, order)))
