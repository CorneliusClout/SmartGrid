class House:
    def __init__(self, x_coordinate, y_coordinate, output):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.output = output
        self.connected_battery = None
        self.cables = []


    def add_connected_battery(self, battery):
        self.connected_battery = battery


# TODO add cables function
    def add_cables(self, location):
        pass

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return self.id