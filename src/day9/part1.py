data = ''

with open('input.txt', 'r') as f:
    data += f.read().strip()

hard_drive = []
block_id = 0
for i in range(len(data)):
    curr_num = data[i]
    if i == 0 or i % 2 == 0:
        for j in range(int(curr_num)):
            hard_drive.append(block_id)
        block_id += 1
    elif i % 2 != 0:
        for j in range(int(curr_num)):
            hard_drive.append('.')

def swap_vals(a, b):
    holder = hard_drive[a]
    hard_drive[a] = hard_drive[b]
    hard_drive[b] = holder

l = 0
r = len(hard_drive) - 1

while l < r:
    # move left pointer until empt space
    while l < r and hard_drive[l] != '.':
        l += 1
    
    # move right pointer until non-empty space
    while l < r and hard_drive[r] == '.':
        r -= 1

    # swap values and increment
    if l < r:
        swap_vals(l,r)
        l += 1
        r -= 1

# calculate checksum

checksum = 0
for i, num in enumerate(hard_drive):
    if num == '.': break
    checksum += i*num

print(checksum)



