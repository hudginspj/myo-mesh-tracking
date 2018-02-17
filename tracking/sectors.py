


distances_1 = [10, None, None, None, None, None,]

#node1, node2, combined_distance limit
all_edge_sectors = [
    #[1, 2, 50]
]
all_node_sectors = [
    [0, 50],
    [1, 50],
    [2, 50],
    [3, 50],
    [4, 50]
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

def find_sector(distances, node_secs, edge_secs):
    for sec in node_secs:
        if in_node_sector(distances, sec):
            return sec[0]
    for sec in edge_secs:
        if in_edge_sector(distances, sec):
            return None  #TODO return both
    return None

#

######## Path to sectors




if __name__ == "__main__":
    print(in_sectors([None, None, 20, None, None, None], all_node_sectors, all_edge_sectors))