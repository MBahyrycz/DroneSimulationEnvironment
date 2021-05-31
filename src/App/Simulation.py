from time import perf_counter
import time

class Simulation:
    def __init__(self, name, layers=[], scenarios={}):
        self.name = name
        self.layers = layers
        self.scenarios = scenarios
        print("Simulation {0} has been created!".format(self.name))     

    def run(self, step, sim_time, scenario_name="", show=True):
        self.step = step
        self.steps_count = 0
        delta_time=0

        print("Running {0} simulation ...".format(self.name))

        start = 0
        while sim_time>start:
            start = perf_counter()

            if self.scenarios and scenario_name:
                self.scenarios[scenario_name].execute(self.steps_count, self.layers)

            for l in self.layers:
                l.on_update(self.steps_count)

            stop = perf_counter()
            delta_time = stop-start
            if delta_time < step:
                time.sleep(step-delta_time)

            self.steps_count += 1


        print("Simulation {0} ended after {1} seconds ({2} steps)".format(self.name, sim_time, self.steps_count ))

    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario

    def add_layer(self, layer):
        self.layers.append(layer)
