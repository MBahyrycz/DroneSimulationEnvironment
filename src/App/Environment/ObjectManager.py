class ObjectManager():
    def __init__(self):
        self.register = {}
        self.unused_ids = [ x for x in range(1,100)]
        self.used_ids = []
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

    def get_from_layers(self, layers):
        self.register.clear()
        for l in layers:
            if l.is_computed:
                for c in l.components:
                    if hasattr(c, "id"):
                        self.register[c.id] = c

    def get_object_by_id(self, id):
        return self.register[id]

    def generate_id(self):
        id = self.ids[0]
        self.unused_ids.remove(id)
        self.used_ids.append(id)
        return id