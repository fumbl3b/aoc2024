import sys
sys.setrecursionlimit(10**7)

input_data = None
rule_bible = {}

with open('input.txt', 'r') as f:
    # cleaning any possible whitespace
    input_data = [line.strip() for line in f if line.strip()]

def validate_order(job):
    for i in range(len(job)):
        if job[i] in rule_bible:
            not_allowed = rule_bible[job[i]]
            # If any of the pages that must come before job[i] appear after it, it's invalid
            if any(page in not_allowed for page in job[i + 1:]):
                return False
    return True

# get rules
def get_rules(rules):
    rule_list = []
    for line in rules:
        a, b = [int(num.strip()) for num in line.split('|')]
        rule_list.append([a,b])
    return rule_list

# get pageorders
def get_page_orders(orders):
    page_orders = []
    for order in orders:
        nums = [int(num.strip()) for num in order.split(',')]
        page_orders.append(nums)
    return page_orders

pos = get_page_orders([l for l in input_data if ',' in l])
rules = get_rules([l for l in input_data if '|' in l])

# Build rule_bible:
# If we have a|b, that means a must appear before b.
# store it as rule_bible[b].add(a) meaning "all these a's must come before b".
rule_bible.clear()
for a, b in rules:
    if b not in rule_bible:
        rule_bible[b] = set()
    rule_bible[b].add(a)

correct_orders = []
incorrect_orders = []

for job in pos:
    if validate_order(job):
        correct_orders.append(job)
    else:
        incorrect_orders.append(job)

# Backtracking to fix incorrect orders
def backtrack_find_order(pages):
    """
    Given a list of pages 'pages' (which is the update), 
    return a correct ordering of these pages if possible, else None.

    We'll use backtracking to find a sequence that satisfies all rules.
    """
    pages_set = set(pages)  # Store pages as a set
    return backtrack([], pages_set, pages_set)

def backtrack(current_order, remaining, update_pages):
    if not remaining:
        # All pages placed, final check not strictly necessary if we trust the logic
        return current_order

    for p in list(remaining):
        # Only consider rules relevant to pages in this update
        if p in rule_bible:
            relevant_required = rule_bible[p].intersection(update_pages)
            if not relevant_required.issubset(current_order):
                continue

        # If no issue, place p
        remaining.remove(p)
        result = backtrack(current_order + [p], remaining, update_pages)
        if result is not None:
            return result
        remaining.add(p)

    return None



fixed = []
index = 0

for update in incorrect_orders:
    print(f"fixing order {index+1} of {len(incorrect_orders)}\n {update}")
    new_order = backtrack_find_order(update)
    if new_order is not None:
        print("success!", new_order)
        fixed.append(new_order)
    else:
        print("No valid order found for", update)
    index += 1

# Now sum the middle pages of fixed and correct_orders
print("Fixed orders sum:", sum(order[len(order)//2] for order in fixed))
print("Correct orders sum:", sum(order[len(order)//2] for order in correct_orders))

# commented out - use for debug only
# print("Correct orders:")
# for order in correct_orders:
#     print(",".join(map(str, order)))
