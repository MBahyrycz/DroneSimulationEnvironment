class ObjectManager:
    def __init__(self):
        self.register = {}
        self.highest_id = 0
        self.used_ids = []
        self.returned_ids = []
        global g_ObjectTraces
        g_ObjectTraces = {}
        for i in range(4):
            g_ObjectTraces[i] = []

    @staticmethod
    def track(component):
        g_ObjectTraces[component.id].append((component.position[0], component.position[1]))

    @staticmethod
    def print_traces():
        print(g_ObjectTraces)

    @staticmethod
    def get_object_traces():
        return g_ObjectTraces

    def get_id(self):
        if self.returned_ids:
            self.returned_ids.sort()
            _id = self.returned_ids.pop(0)
        else:
            self.highest_id += 1
            _id = self.highest_id
        return _id

    def return_id(self, _id):
        _id_index = self.used_ids.index(_id)
        self.used_ids.pop(_id_index)
        self.returned_ids.append(_id)

    def get_from_layers(self, layers):
        self.register.clear()
        for l in layers:
            if l.is_computed:
                for c in l.components:
                    if hasattr(c, "id"):
                        self.register[c.id] = c

    def get_object_by_id(self, id):
        return self.register[id]
