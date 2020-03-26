from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = {}
    current_level = 1
    ancestors_in_level = {}

    for relationship in ancestors:
        child = relationship[1]
        parent = relationship[0]

        if child in ancestor_graph:
            ancestor_graph[child].add(parent)
        else:
            ancestor_graph[child] = set()
            ancestor_graph[child].add(parent)

    if starting_node not in ancestor_graph:
        return -1

    s = Stack()
    visited = set()
    s.push([starting_node])
    path_list = []

    while s.size() > 0:
        path = s.pop()
        path_list.append(path)
        print(path_list)
        vertex = path[-1]

        if vertex not in visited and vertex in ancestor_graph:
            visited.add(vertex)

            for next_v in ancestor_graph[vertex]:
                new_path = list(path)
                new_path.append(next_v)
                s.push(new_path)

    if len(path_list[-1]) > len(path_list[-2]):
        return path_list[-1][-1]
    elif len(path_list[-1]) == len(path_list[-2]) and len(path_list[-2]) > len(path_list[-3]):
        return min(path_list[-1][-1], path_list[-2][-1])
    else:
        return min(path_list[-1][-1], path_list[-2][-1], path_list[-3][-1])
