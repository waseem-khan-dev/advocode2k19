class Body():
    def __init__(self, name):
        self.children = []
        self.name = name

    def __str__(self):
        return self.name


def add_children_to_body(body, orbits):
    child_relationships = [
        orbit for orbit in orbits if orbit.startswith(body.name)]

    for child_relationship in child_relationships:
        orbits.remove(child_relationship)
        child_name = child_relationship.split(')')[1]
        child_body = Body(child_name)
        body.children.append(child_body)
        add_children_to_body(child_body, orbits)


def count_orbits(body, dist_to_com=1):
    return len(body.children) * dist_to_com + sum([count_orbits(child_body, dist_to_com + 1) for child_body in body.children])


if __name__ == '__main__':

    orbit_map = open("data/day_0601.txt").read()

    # Initialise network
    orbits = [orbit for orbit in orbit_map.split('\n') if orbit != '']
    com = Body('COM')
    add_children_to_body(com, orbits)
    print('Part 1 Solution')
    print(count_orbits(com))
