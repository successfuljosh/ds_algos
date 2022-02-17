#Krusal algorithm

def minimumCost(connections) -> int:
    #sort by weight. our input [x,y,weight]
    connections = sorted(connections, key=lambda x: x[2])
    print(connections)
    #get vertices
    vertex = set()
    for a in connections:
        vertex.add(a[0])
        vertex.add(a[1])

    sum = 0
    visited_nodes = set()
    mst_edge_count = 0
    for i in range(0, len(connections)):
        # check if there is a cycle
        if connections[i][0] in visited_nodes and connections[i][1] in visited_nodes:
            continue
        else:
            visited_nodes.add(connections[i][0])
            visited_nodes.add(connections[i][1])
            mst_edge_count += 1
            sum += connections[i][2]
        if mst_edge_count == len(vertex) - 1:
            break
    #check is mst edges is |v| - 1
    print(mst_edge_count, sum)
    if mst_edge_count != len(vertex) - 1:
        return -1
    else:
        return sum

cities_link = [[2,1,87129],[3,1,14707],[4,2,34505],[5,1,71766],[6,5,2615],[7,2,37352]]
print(minimumCost(cities_link))