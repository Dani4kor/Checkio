# def dfs(graph, start):
#     visited, stack = [], [start]
#     poop = graph
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             for x in graph[vertex]:
#                 if x not in visited:
#                     stack.extend(x)
#     return visited


# def bfs(graph, start):
#     queue = [[start]]
#     visited = set()
#     while queue:
#         path = queue.pop(0)
#         vertex = path[-1]
#         if vertex not in visited:
#             for current_neighbour in graph.get(vertex, []):
#                 new_path = list(path)
#                 new_path.append(current_neighbour)
#                 queue.append(new_path)
#             visited.add(vertex)





def checkio(teleports_string):
    route = ['1']
    node = dict()
    for i in teleports_string.split(','):
        node.setdefault(i[0], []).append(i[1]), node.setdefault(i[1], []).append(i[0])
    print node
    pre = 0
    while len(set(route)) != len(node) or route[-1] != '1':
        current = route[-1]
        open = [x for x in node[current] if x > pre]
        if not open:
            route.pop(-1)
            pre = current
            node[pre].append(route[-1])
            node[route[-1]].append(pre)

        else:
            m = min(open)
            route.append(m)
            node[m].remove(current)
            node[current].remove(m)
            pre = 0

    return ''.join(route)




#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    #assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    #assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    #assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"