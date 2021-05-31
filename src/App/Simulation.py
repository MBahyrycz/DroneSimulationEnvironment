from time import perf_counter
import time

class Simulation:
    def __init__(self, name):
        self.name = name
        self.layers = []
        self.scenarios = {}
        print("Simulation {0} has been created!".format(self.name))     

    def run(self, step, sim_time, show=True):
        self.step = step
        self.steps_count = 0
        delta_time=0

        print("Running {0} simulation ...".format(self.name))

        start = 0
        while sim_time>start:
            start = perf_counter()

            for l in self.layers:
                l.on_update(delta_time)
                if show:
                    l.show(delta_time)
        
            # print("XD")

            stop = perf_counter()
            delta_time = stop-start
            if delta_time < step:
                time.sleep(step-delta_time)

            self.steps_count += 1


        print("Simulation {0} ended after {1} seconds ({2} steps)".format(self.name, sim_time, self.steps_count ))

    def add_layer(self, layer):
        self.layers.append(layer)

    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario
