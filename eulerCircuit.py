def EulerCircuit(graph):
    tour = []

    current_vertex = graph[0][0]
    tour.append(current_vertex)

    while len(graph) > 0:
        print(graph, current_vertex)
        for edge in graph:
            if current_vertex in edge:
                if edge[0] == current_vertex:
                    current_vertex = edge[1]
                else:
                    current_vertex = edge[0]

                graph.remove(edge)
                tour.append(current_vertex)
                break
        else:
            print("Nie istnieje cykl Eulera")
            return None
    return tour