import time

K_ITER = 100

def prepare_map(rectangles):
    x_coords = set()
    y_coords = set()
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        x_coords.add(x1)
        x_coords.add(x2)
        y_coords.add(y1)
        y_coords.add(y2)
    
    x_sorted = sorted(x_coords)
    y_sorted = sorted(y_coords)
    
    map_grid = {}
    for i in range(len(x_sorted) - 1):
        for j in range(len(y_sorted) - 1):
            x_mid = x_sorted[i]
            y_mid = y_sorted[j]
            count = 0
            for rect in rectangles:
                x1, y1, x2, y2 = rect
                if x1 <= x_mid < x2 and y1 <= y_mid < y2:
                    count += 1
            map_grid[(i, j)] = count
    
    return x_sorted, y_sorted, map_grid

def query_map(x, y, x_sorted, y_sorted, map_grid):
    left, right = 0, len(x_sorted) - 1
    x_idx = -1
    while left <= right:
        mid = (left + right) // 2
        if x_sorted[mid] <= x:
            x_idx = mid
            left = mid + 1
        else:
            right = mid - 1
    
    left, right = 0, len(y_sorted) - 1
    y_idx = -1
    while left <= right:
        mid = (left + right) // 2
        if y_sorted[mid] <= y:
            y_idx = mid
            left = mid + 1
        else:
            right = mid - 1
    
    if x_idx >= 0 and y_idx >= 0 and x_idx < len(x_sorted) - 1 and y_idx < len(y_sorted) - 1:
        return map_grid.get((x_idx, y_idx), 0)
    else:
        return 0

N = 500
rectangles = []
for i in range(N):
    x1 = 100 * i
    y1 = 100 * i
    x2 = 100 * i + 50
    y2 = 100 * i + 50
    rectangles.append((x1, y1, x2, y2))

points = []
for i in range(100):
    x = 100 * i + 25
    y = 100 * i + 25
    points.append((x, y))

print("Прямоугольников:", N)
print("Уникальных x-координат:", 2 * N)
print("Уникальных y-координат:", 2 * N)

start = time.time()

x_sorted, y_sorted, map_grid = prepare_map(rectangles)
end = time.time()
print("Время подготовки:", end - start)

start = time.time()
total = 0
for _ in range(K_ITER-1):
    for x, y in points:
        query_map(x, y, x_sorted, y_sorted, map_grid)
for x, y in points:
    result = query_map(x, y, x_sorted, y_sorted, map_grid)
    total += result
end = time.time()
print("Время запросов:", (end - start) / K_ITER)


"""rectangles = [
    (1, 1, 5, 5),
    (3, 3, 7, 7),
    (2, 2, 6, 6),
    (0, 0, 10, 10)
]

x_coords = set()
y_coords = set()
for rect in rectangles:
    x1, y1, x2, y2 = rect
    x_coords.add(x1)
    x_coords.add(x2)
    y_coords.add(y1)
    y_coords.add(y2)

x_sorted = sorted(x_coords)
y_sorted = sorted(y_coords)

map_grid = {}
for i in range(len(x_sorted) - 1):
    for j in range(len(y_sorted) - 1):
        x_mid = x_sorted[i]
        y_mid = y_sorted[j]
        count = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            if x1 <= x_mid < x2 and y1 <= y_mid < y2:
                count += 1
        map_grid[(i, j)] = count

x, y = 4, 4

left, right = 0, len(x_sorted) - 1
x_idx = -1
while left <= right:
    mid = (left + right) // 2
    if x_sorted[mid] <= x:
        x_idx = mid
        left = mid + 1
    else:
        right = mid - 1

left, right = 0, len(y_sorted) - 1
y_idx = -1
while left <= right:
    mid = (left + right) // 2
    if y_sorted[mid] <= y:
        y_idx = mid
        left = mid + 1
    else:
        right = mid - 1

if x_idx >= 0 and y_idx >= 0 and x_idx < len(x_sorted) - 1 and y_idx < len(y_sorted) - 1:
    result = map_grid.get((x_idx, y_idx), 0)
else:
    result = 0

print(result)"""