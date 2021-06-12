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
        self.window_size = self.window_width, self.window_height = 800, 800
        print("Simulation {0} has been created!".format(self.name))     

    def run(self, step_time, sim_time, scenario_name="", show=True):
        # simulation variables initialisation
        self.is_running = True
        self.step_time = step_time
        self.steps_count = 0
        self.sim_start = 0
        delta_time=0

        # window creation and pygame initialisation
        pygame.init()
        pygame.font.init()
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("{0}".format(self.name))

        self.start = 0
        self.sim_start = perf_counter()
        print("Running {0} simulation ...".format(self.name))
        while sim_time>self.start and self.is_running:
            self.start = perf_counter() - self.sim_start

            #handling pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.is_running = False

            print("\n================STEP={0}===================".format(self.steps_count))

            if self.scenarios and scenario_name:
                self.scenarios[scenario_name].execute(self.steps_count, self.layers)

            for l in self.layers:
                l.on_update(self.steps_count)

            #displaying logic
            step_label = self.main_font.render("Step: {0}".format(self.steps_count), 1, (255, 255, 255))
            
            for l in self.layers:
                l.on_display(self.surface)  
            self.surface.blit(step_label, (self.window_width - step_label.get_width() - 20, 20))

            pygame.display.update()

            stop = perf_counter() - self.sim_start
            delta_time = stop-self.start
            if delta_time < step_time:
                time.sleep(step_time-delta_time)

            self.steps_count += 1

        # print("Simulation {0} ended after {1} seconds ({2} steps)".format(self.name, self.start, self.steps_count ))
        time.sleep(1)
        pygame.quit()

    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario

    def add_layer(self, layer):
        self.layers.append(layer)

    def sum_up(self):
        return "Simulation {0} ended after {1:.2f} seconds ({2} steps)".format(self.name, self.start, self.steps_count )
