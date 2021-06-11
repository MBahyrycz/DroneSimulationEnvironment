from time import perf_counter
import time
import sys
import pygame
import os

from Layers.Layer import *

class Simulation:
    def __init__(self, name, layers=[], scenarios={}):
        self.name = name
        self.layers = layers
        self.scenarios = scenarios
        self.is_running = False
        self.window_size = self.window_width, self.window_height = 600, 600
        print("Simulation {0} has been created!".format(self.name))     

    def run(self, step_time, sim_time, scenario_name="", show=True):
        # simulation variables initialisation
        self.is_running = True
        self.step_time = step_time
        self.steps_count = 0
        delta_time=0

        # window creation and pygame initialisation
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("{0}".format(self.name))

        # retriving unique data from layers
        # path = ""
        # for l in self.layers:
        #     if l.type == Type.MAP:
        #         path = l.components[0].file_name

        # self.background = pygame.image.load(os.path.join(os.pardir, "assets", path))

        print("Running {0} simulation ...".format(self.name))
        start = 0
        while sim_time>start and self.is_running:
            start = perf_counter()

            #handling pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.is_running = False

            print("\n================STEP={0}===================".format(self.steps_count))

            if self.scenarios and scenario_name:
                self.scenarios[scenario_name].execute(self.steps_count, self.layers)

            for l in self.layers:
                l.on_update(self.steps_count)

            #displaying logic
            for l in self.layers:
                l.on_display(self.screen)  
            pygame.display.update()

            stop = perf_counter()
            delta_time = stop-start
            if delta_time < step_time:
                time.sleep(step_time-delta_time)

            self.steps_count += 1


        print("Simulation {0} ended after {1} seconds ({2} steps)".format(self.name, start, self.steps_count ))

    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario

    def add_layer(self, layer):
        self.layers.append(layer)
