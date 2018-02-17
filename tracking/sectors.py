


distances_1 = [10, None, None, None, None, None,]

#node1, node2, combined_distance limit
all_edge_sectors = [
    [1, 2, 50]
]
all_node_sectors = [
    [1, 15],
    [2, 15]
]



def in_node_sector(distances, sector):
    (node_index, max_distance) = sector
    return distances[node_index] and distances[node_index] <= max_distance

def in_edge_sector(distances, sector):
    (index1, index2, max_distance) = sector
    if (not distances[index1]) or (not distances[index2]):
        return False
    combined_distance = distances[index1] + distances[index2]
    return combined_distance <= max_distance

def in_sectors(distances, node_secs, edge_secs):
    for sec in node_secs:
        if in_node_sector(distances, sec):
            return True
    for sec in edge_secs:
        if in_edge_sector(distances, sec):
            return True
    return False

# print(in_sectors([None, None, 20, None, None, None], node_sectors, edge_sectors))

######## Path to sectors

def select_node_sectors(node_secs, path):
    selected_secs = []
    for sec in node_secs:
        if sec[0] in path:
            selected_secs.append(sec)
    return selected_secs

def select_edge_sectors(edge_secs, path):
    selected_secs = []
    for sec in edge_secs:
        if (sec[0] in path) and (sec[1] in path):
            selected_secs.append(sec)
    return selected_secs


path = [1, 2]

path_node_sectors = select_node_sectors(all_node_sectors, path)
path_edge_sectors = select_edge_sectors(all_edge_sectors, path)

def in_path(distances):
    return in_sectors(distances, path_node_sectors, path_edge_sectors)

print(in_path([None, 20, 20, None, None, None]))