K, N = map(int, input().split())

LAN_cables = []

for _ in range(K):
    cable_length = int(input())
    LAN_cables.append(cable_length)

start, end = 1, max(LAN_cables)

while start <= end:
    mid = (start + end) // 2
    total_lan_cables = sum(cable // mid for cable in LAN_cables)

    if total_lan_cables >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
