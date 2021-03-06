from App.Environment.CollisionDetector import CollisionDetector
from App.Environment.ObjectManager import *

from time import perf_counter
import time
import pygame

from Layers.Layer import *


class Simulation:
    def __init__(self, name, layers=[], scenarios={}):
        self.name = name
        self.layers = layers
        self.scenarios = scenarios
        self.is_running = False
        self.colision_detector = CollisionDetector()
        self.object_manager = ObjectManager()

        self.window_size = self.window_width, self.window_height = 800, 800
        print("Simulation {0} has been created!".format(self.name))

    def run(self, step_time, sim_time, scenario_name="", show=True, log=False):
        # simulation variables initialisation
        self.is_running = True
        self.step_time = step_time
        self.steps_count = 0
        self.sim_start = 0
        delta_time = 0
        self.colision_detector.colliders.clear()
        self.object_manager.get_from_layers(self.layers)
        print(self.object_manager.register)

        # window creation and pygame initialisation
        if show:
            pygame.init()
            pygame.font.init()
            self.main_font = pygame.font.SysFont("comicsans", 50)
            self.window = pygame.display.set_mode(self.window_size)
            self.surface = pygame.Surface(self.window_size, pygame.SRCALPHA, 32)
            pygame.display.set_caption("{0}".format(self.name))

        if self.scenarios and scenario_name:
            self.scenarios[scenario_name].execute(self.object_manager)

        self.start = 0
        self.sim_start = perf_counter()
        print("Running {0} simulation ...".format(self.name))
        while sim_time > self.start and self.is_running:
            self.start = perf_counter() - self.sim_start

            # handling pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.is_running = False

            # print("\n================STEP={0}===================".format(self.steps_count))

            # collision detection
            self.colision_detector.detect()
            for d in self.colision_detector.detections:
                self.object_manager.get_object_by_id(d[0].id).on_collision(self.steps_count)

            # layers update
            for l in self.layers:
                l.on_update(self.steps_count)

            # collision detector update 
            self.colision_detector.get_from_layers(self.layers)

            # displaying logic

            if show:
                step_label = self.main_font.render("Step: {0}".format(self.steps_count), 1, (255, 255, 255))

                self.window.blit(self.surface, (0, 0))
                for l in self.layers:
                    l.on_display(self.surface)
                    # self.colision_detector.draw_boxes(self.surface)
                self.window.blit(step_label, (self.window_width - step_label.get_width() - 20, 20))
                pygame.display.update()

            stop = perf_counter() - self.sim_start
            delta_time = stop - self.start
            if delta_time < step_time:
                time.sleep(step_time - delta_time)

            self.steps_count += 1

        time.sleep(1)
        pygame.quit()

    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario

    def track_drones(self):
        traces = {}
        for l in self.layers:
            if l.type == Type.DRONE:
                for c in l.components:
                    traces[c.id] = c.trace

    def create_scenario(self):
        pass

    def add_layer(self, layer):
        self.layers.append(layer)

    def create_layer(self, type):
        self.layers.append(Layer(type, []))

    def shutdown(self):
        self.layers.clear()
        self.colision_detector.shutdown()

    def sum_up(self):
        return "Simulation {0} ended after {1:.2f} seconds ({2} steps)".format(self.name, self.start, self.steps_count)
