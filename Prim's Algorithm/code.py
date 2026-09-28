def prim_easy(graph):
  V = len(graph)
  selected = [False] * V
  selected[0] = True  # Start from the first node

  total_cost = 0
  print("Edge \tWeight")

  # There will be V-1 edges in the Minimum Spanning Tree
  for _ in range(V - 1):
    min_weight = float("inf")
    u, v = -1, -1

    # Find the minimum weight edge connecting a visited node to an unvisited node
    for i in range(V):
      if selected[i]:
        for j in range(V):
          if not selected[j] and graph[i][j] != 0:
            if graph[i][j] < min_weight:
              min_weight = graph[i][j]
              u = i
              v = j

    # Mark the chosen node as visited and add weight
    selected[v] = True
    total_cost += min_weight
    print(f"{u} - {v} \t{min_weight}")

  print(f"Total Cost: {total_cost}")