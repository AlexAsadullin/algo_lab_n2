import os
import plotly.graph_objects as go
from iterate_through import main as iter_through
from map_rectangles import main as map_rectang
from tree import main as tree_rectang

algorithms = ["Перебор", "Карта", "Дерево"]

print("Перебор:")
iter_time, iter_mem = iter_through()

print("\nКарта:")
map_time, map_mem = map_rectang()

print("\nДерево:")
tree_time, tree_mem = tree_rectang()

times = [iter_time, map_time, tree_time]
mems = [iter_mem, map_mem, tree_mem]

os.makedirs("charts", exist_ok=True)

fig_time = go.Figure()
fig_time.add_trace(go.Bar(x=algorithms, y=times))
fig_time.update_layout(
    title="Сравнение времени работы алгоритмов",
    xaxis_title="Алгоритм",
    yaxis_title="Время (с)",
    yaxis_type="log",
)
fig_time.write_html("charts/time.html")

fig_mem = go.Figure()
fig_mem.add_trace(go.Bar(x=algorithms, y=mems))
fig_mem.update_layout(
    title="Сравнение памяти алгоритмов",
    xaxis_title="Алгоритм",
    yaxis_title="Память (МБ)",
    yaxis_type="log",
)
fig_mem.write_html("charts/memory.html")

print("\nГрафики сохранены в charts/time.html и charts/memory.html")
