import bisect
import time
import tracemalloc

K_ITER = 10

def prepare_tree(rectangles):
    y_coords = set()
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        y_coords.add(y1)
        y_coords.add(y2)
    y_sorted = sorted(y_coords)
    y_compress = {v: i for i, v in enumerate(y_sorted)}
    
    events = {}
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        y1_c = y_compress[y1]
        y2_c = y_compress[y2]
        
        if x1 not in events:
            events[x1] = []
        events[x1].append((1, y1_c, y2_c))
        
        if x2 not in events:
            events[x2] = []
        events[x2].append((-1, y1_c, y2_c))
    
    x_positions = sorted(events.keys())
    snapshots = {}
    active_intervals = []
    
    for x_pos in x_positions:
        for event_type, y1_c, y2_c in events[x_pos]:
            if event_type == 1:
                active_intervals.append((y1_c, y2_c))
            else:
                active_intervals.remove((y1_c, y2_c))
        snapshots[x_pos] = list(active_intervals)
    
    return x_positions, y_sorted, snapshots

def query_tree(x, y, x_positions, y_sorted, snapshots):
    idx = bisect.bisect_right(x_positions, x) - 1
    if idx >= 0:
        x_key = x_positions[idx]
        intervals = snapshots[x_key]
        
        y_idx = bisect.bisect_right(y_sorted, y) - 1
        
        count = 0
        for y1_c, y2_c in intervals:
            if y1_c <= y_idx < y2_c:
                count += 1
        return count
    else:
        return 0


def main():
    N = 10000
    rectangles = []
    for i in range(N):
        x1 = 10 * i
        y1 = 10 * i
        x2 = 10 * (2 * N - i)
        y2 = 10 * (2 * N - i)
        rectangles.append((x1, y1, x2, y2))

    center_x = 10 * N
    center_y = 10 * N
    radius = 5

    points = []
    p_x = 999983
    p_y = 1000003
    for i in range(1000):
        x = center_x + ((p_x * i) ** 31) % (2 * radius) - radius
        y = center_y + ((p_y * i) ** 31) % (2 * radius) - radius
        points.append((x, y))

    print("Прямоугольников:", N)
    print("Уникальных x-координат:", 2 * N)
    print("Уникальных y-координат:", 2 * N)

    tracemalloc.start()
    start = time.time()
    x_positions, y_sorted, snapshots = prepare_tree(rectangles)
    end = time.time()
    prep_time = end - start
    print("Время подготовки:", prep_time)


    start = time.time()
    total = 0
    for _ in range(K_ITER):
        for x, y in points:
            result = query_tree(x, y, x_positions, y_sorted, snapshots)
    for x, y in points:
        result = query_tree(x, y, x_positions, y_sorted, snapshots)
        total += result
    end = time.time()
    query_time = (end - start) / K_ITER
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    total_time = prep_time + query_time
    peak_mem_mb = peak_mem / (1024 * 1024)
    print("Время запросов:", query_time)
    print("Пиковая память:", round(peak_mem_mb, 2), "МБ")

    return total_time, peak_mem_mb



"""
import bisect

rectangles = [
    (1, 1, 5, 5),
    (3, 3, 7, 7),
    (2, 2, 6, 6),
    (0, 0, 10, 10)
]

y_coords = set()
for rect in rectangles:
    x1, y1, x2, y2 = rect
    y_coords.add(y1)
    y_coords.add(y2)
y_sorted = sorted(y_coords)
y_compress = {v: i for i, v in enumerate(y_sorted)}

events = {}
for rect in rectangles:
    x1, y1, x2, y2 = rect
    y1_c = y_compress[y1]
    y2_c = y_compress[y2]
    
    if x1 not in events:
        events[x1] = []
    events[x1].append((1, y1_c, y2_c))
    
    if x2 not in events:
        events[x2] = []
    events[x2].append((-1, y1_c, y2_c))

x_positions = sorted(events.keys())
snapshots = {}
active_intervals = []

for x_pos in x_positions:
    for event_type, y1_c, y2_c in events[x_pos]:
        if event_type == 1:
            active_intervals.append((y1_c, y2_c))
        else:
            active_intervals.remove((y1_c, y2_c))
    snapshots[x_pos] = list(active_intervals)

x, y = 4, 4

idx = bisect.bisect_right(x_positions, x) - 1
if idx >= 0:
    x_key = x_positions[idx]
    intervals = snapshots[x_key]
    
    y_idx = bisect.bisect_right(y_sorted, y) - 1
    
    count = 0
    for y1_c, y2_c in intervals:
        if y1_c <= y_idx < y2_c:
            count += 1
    print(count)
else:
    print(0)
"""