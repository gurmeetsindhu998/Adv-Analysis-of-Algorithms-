import math
def dijkstraAlgo(source, varList):
    distDict = {v: [math.inf, None] for v in varList}
    distDict[source] = [0, source]
    unvisited = set(varList)

    while unvisited:
        curr = min(unvisited, key=lambda v: distDict[v][0])
        unvisited.remove(curr)

        for neighbor in varList:
            if neighbor not in unvisited:
                continue

            #cost = costDict[curr][neighbor]
            alt = distDict[curr][0] 
            if alt < distDict[neighbor][0]:
                distDict[neighbor] = [alt, distDict[curr][1] + neighbor]

        if curr == source and not unvisited:
            break

   
    return distDict

dijkstraAlgo("u",["u","v","w","x","y","z"])


for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for 
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        print(sorted(candidates, key = lambda x: x[1]))
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited
  