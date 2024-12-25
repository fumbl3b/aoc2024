locks = []
keys = []
data = []

MAX_VAL = 7

with open('input.txt','r') as f:
    data = f.read().split('\n\n')

def parse(data):
    arr = []
    for line in data.split('\n'):
        arr.append(list(line))
    return arr

for block in data:
    if all(value == '.' for value in block[0]):
        keys.append(block)
    else:
        locks.append(block)

def calc_column_heights(block):
    arr = [list(i) for i in block.split('\n')]
    heights = [0,0,0,0,0]
    for row in arr:
        for x in range(len(row)):
            if row[x] == '#':
                heights[x] += 1
    return heights
            

def check_overlap(lock, key):
    lock_heights = calc_column_heights(lock)
    key_heights = calc_column_heights(key)
    for i in range(len(lock_heights)):
        comb_height = lock_heights[i] + key_heights[i]
        if comb_height > MAX_VAL:
            return True 
    return False

print('locks list and keys list same length: ', len(locks) == len(keys))
pairs = []
for x in range(len(locks)):
    lock_to_check = locks[x]
    for key in keys:
        if not check_overlap(lock_to_check, key):
            pairs.append((lock_to_check, key))
print('unique pairs: ', len(pairs))

