


class DockingStation:
    def __init__(self, position, id):
        self.position = position
        self.id = id

    def on_update(self, step):
        print("Docking station {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))