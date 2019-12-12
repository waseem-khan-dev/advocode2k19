class Body():
    def __init__(self, name, parent):
        self.children = []
        self.name = name
        self.parent = parent


def add_children_to_body(body, orbits):
    child_relationships = [
        orbit for orbit in orbits if orbit.startswith(body.name)]

    for child_relationship in child_relationships:
        orbits.remove(child_relationship)
        child_name = child_relationship.split(')')[1]
        child_body = Body(child_name, parent=body)
        body.children.append(child_body)
        add_children_to_body(child_body, orbits)


def find_parent_body(node, body_name, result):
    for child in node.children:
        if child.name == body_name:
            result.append(node)
        else:
            find_parent_body(child, body_name, result)  # Depth first search


def search_children(node, node_to_find_name, dist=0):
    for child in node.children:
        if child.name == node_to_find_name:
            return dist
        else:
            result = search_children(child, node_to_find_name, dist+1)
            if result is not None:
                return result


def find_dist_to_node(parent_node, node_to_find_name):
    result = search_children(parent_node, node_to_find_name)
    if result is None:
        return 1 + find_dist_to_node(parent_node.parent, node_to_find_name)
    return result


if __name__ == '__main__':

    puzzle_input = open("data/day_0602.txt").read()

    # Initialise network
    orbits = [orbit for orbit in puzzle_input.split('\n') if orbit != '']
    com = Body('COM', None)
    add_children_to_body(com, orbits)

    result = []
    find_parent_body(com, 'YOU', result)
    you_parent = result[0]

    print('Part 2 Solution', find_dist_to_node(you_parent, 'SAN'))
