from heapq import heappush, heappop

lists = [[1,4,5],[1,3,4],[2,6]]

heap = []
res = []

# Har list ka pehla element heap me
for i, arr in enumerate(lists):
    if arr:
        heappush(heap, (arr[0], i, 0))

while heap:
    val, row, col = heappop(heap)
    res.append(val)

    if col + 1 < len(lists[row]):
        heappush(heap, (lists[row][col + 1], row, col + 1))

print(res)