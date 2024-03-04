import sys

row, col, inventory = map(int, sys.stdin.readline().split())
ground = []

for _ in range(row):
    ground += list(map(int, sys.stdin.readline().split()))

time = [0 for i in range(257)]
min_height = 0

for t_height in range(257):
    block_cnt = inventory
    for t_block in ground:
        if t_block <= t_height:
            time[t_height] += t_height - t_block
            block_cnt -= t_height - t_block
        else:
            time[t_height] += 2 * (t_block - t_height)
            block_cnt += (t_block - t_height)
    if block_cnt >= 0 and time[t_height] <= time[min_height]:
        min_height = t_height

print(time[min_height], min_height)