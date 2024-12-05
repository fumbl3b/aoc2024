input_data = None

with open('input.txt', 'r') as f:
    input_data = f.readlines()

# get rules
def get_rules(rules):
    rule_list = []
    for line in rules:
        a, b = [int(num.strip()) for num in line.split('|')]
        rule_list.append([a,b])
    return rule_list



# get pageorders
def get_page_orders(orders):
    print(orders)
    page_orders = []
    for order in orders:
        data = []
        page_orders.append([int(num) for num in order.split(',')])
    return page_orders

# print(get_rules([line for line in input_data if '|' in line]))
# print(get_page_orders([line for line in input_data if ',' in line]))


