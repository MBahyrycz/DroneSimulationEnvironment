class ObjectManager():
    def __init__(self):
        self.register = {}
        self.unused_ids = [ x for x in range(1,100)]
        self.used_ids = []
        print(self.unused_ids[0:5])

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