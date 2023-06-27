import sys
import time

# Representasi graf menggunakan dictionary
graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'C': 8, 'D': 12},
    'C': {'D': 11, 'E': 3, 'G': 9},
    'D': {'C': 11, 'E': 11, 'F': 10},
    'E': {'G': 7, 'F': 6},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9},
    'F': {}
}

# Algoritma TSP (Traveling Salesman Problem) dengan metode rekursif
def tsp(graph, current_vertex, visited, cost, path, start_vertex, iteration):
    visited[current_vertex] = True
    path.append(current_vertex)

    if len(visited) == len(graph) and start_vertex in graph[current_vertex]:
        path.append(start_vertex)
        cost += graph[current_vertex][start_vertex]
        print(f"Iterasi {iteration}: {' -> '.join(path)} (Cost: {cost})")
        return cost

    min_cost = sys.maxsize

    for next_vertex in graph[current_vertex]:
        if not visited[next_vertex]:
            new_cost = tsp(graph, next_vertex, visited.copy(), cost + graph[current_vertex][next_vertex],
                           path.copy(), start_vertex, iteration + 1)
            if new_cost < min_cost:
                min_cost = new_cost

    return min_cost

# Algoritma Dijkstra untuk mencari jalur terpendek
def dijkstra(graph, start_vertex):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start_vertex] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance = sys.maxsize
        current_vertex = None

        for vertex in graph:
            if distances[vertex] < min_distance and vertex not in visited:
                min_distance = distances[vertex]
                current_vertex = vertex

        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            distance = distances[current_vertex] + graph[current_vertex][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        print(f"{current_vertex}: {distances}")

    return distances

if __name__ == '__main__':
    print("=== Program Perhitungan Shortest Path ===")
    print("Pilih Algoritma:")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")
    choice = int(input("Masukkan pilihan (1/2): "))

    if choice == 1:
        start_vertex = 'A'
        visited = {vertex: False for vertex in graph}
        start_time = time.time()
        shortest_path_cost = tsp(graph, start_vertex, visited, 0, [], start_vertex, 1)
        end_time = time.time()
        print(f"\nWaktu Komputasi: {end_time - start_time} detik")
        print(f"Jalur Terpendek: {shortest_path_cost}")

    elif choice == 2:
        start_vertex = 'A'
        start_time = time.time()
        shortest_paths = dijkstra(graph, start_vertex)
        end_time = time.time()
        print(f"\nWaktu Komputasi: {end_time - start_time} detik")
        print("Jalur Terpendek (Dijkstra):")
        for vertex, distance in shortest_paths.items():
            print(f"{vertex}: {distance}")

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
