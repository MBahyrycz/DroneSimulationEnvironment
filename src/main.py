import numpy as np

from Components.Drone import *

from Layers.Layer import *

from App.Environment import *

if __name__ == "__main__":

    step = 1/1
    properties = {'name':'Skulim environment'} 

    env=Environment(properties)

    drone1 = Drone(np.array([1,0,0]), 1)
    drone2 = Drone(np.array([0,0,0]), 1)
    drone3 = Drone(np.array([-1,0,0]), 1)
    drone4 = Drone(np.array([-2,0,0]), 1)

    components = [drone1, drone2, drone3]

    drone_layer = Layer(components) 
    drone_layer.add_component(drone4)
   

    simulation = env.create_simulation('symulacja')
    simulation.add_layer(drone_layer)
    simulation.run(step, 10)
