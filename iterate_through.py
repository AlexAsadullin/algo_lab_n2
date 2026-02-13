import time
import tracemalloc

K_ITER = 10

def count_rectangles(rectangles, points):
    total_count = 0
    for x, y in points:
        count = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            if x1 <= x < x2 and y1 <= y < y2:
                count += 1
        total_count += count
    return total_count


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

    print("Прямоугольников:", N, "Точек:", len(points))

    tracemalloc.start()
    start = time.time()
    for _ in range(K_ITER-1):
        count_rectangles(rectangles, points)
    total_count = count_rectangles(rectangles, points)
    end = time.time()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    total_time = end - start
    peak_mem_mb = peak_mem / (1024 * 1024)
    print("Время:", total_time)
    print("Пиковая память:", round(peak_mem_mb, 2), "МБ")

    return total_time, peak_mem_mb

"""rectangles = [
    (1, 1, 5, 5),
    (3, 3, 7, 7),
    (2, 2, 6, 6),
    (0, 0, 10, 10)
]

x, y = 4, 4

count = 0
for rect in rectangles:
    x1, y1, x2, y2 = rect
    if x1 <= x < x2 and y1 <= y < y2:
        count += 1

print(count)
"""