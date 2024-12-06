import random

input_data = None
rule_bible = {}

with open('input.txt', 'r') as f:
    input_data = f.readlines()

def validate_order(job):
    for i in range(len(job)):
        if job[i] in rule_bible:
            not_allowed = rule_bible[job[i]]
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
        data = []
        page_orders.append([int(num) for num in order.split(',')])
    return page_orders

pos = get_page_orders([l for l in input_data if ',' in l])
rules = get_rules([l for l in input_data if '|' in l])

# every page in the rule bible contains a set of pages that cannot be after it
for rule in rules:
    a, b = rule[0], rule[1]

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

fixed = []
index = 0
for update in incorrect_orders:
    print(f"fixing order {index} of {len(incorrect_orders)} \n {update}")
    while not validate_order(update):
        random.shuffle(update)
        print(f"trying: {update}")
    print("success!")
    fixed.append(update)
    index += 1

print("fixed orders: ", sum(order[len(order)//2] for order in fixed))
print(sum(order[len(order)//2] for order in correct_orders))

# commented out - use for debug only
# print("Correct orders:")
# for order in correct_orders:
#     print(",".join(map(str, order)))
