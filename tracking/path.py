from tracking.sectors import *
path = [0, 1, 4]


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


path_node_sectors = select_node_sectors(all_node_sectors, path)
path_edge_sectors = select_edge_sectors(all_edge_sectors, path)

def sector_in_path(distances):
    return find_sector(distances, path_node_sectors, path_edge_sectors)


def in_path(distances):
    return in_sectors(distances, path_node_sectors, path_edge_sectors)


if __name__ == "__main__":
    print(in_path([None, 20, 20, None, None, None]))