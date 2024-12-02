file = open("input.txt", 'r')

left, right = [], []

# for line in file.readlines():
#     numbers = line.split()
#     left.append(numbers[0])
#     right.append(numbers[1])
#
# total_dist = 0
#
# while(len(left) > 0):
#     min_left = min(left)
#     min_right = min(right)
#     left.remove(min_left)
#     right.remove(min_right)
#
#     total_dist += abs(int(min_left) - abs(int(min_right)))
#
# print("part 1:")
# print(total_dist)

for line in file.readlines():
    numbers = line.split()
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))
sim_score = 0
for n in left:
    print(sim_score, n, right.count)
    sim_score += n * right.count(n)

print("part 2:")
print(sim_score)

file.close()
