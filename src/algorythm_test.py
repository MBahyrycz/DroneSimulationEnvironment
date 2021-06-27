from App.Environment.GeneticAlgorythm.GeneticAlgorythm import *
from App.Environment.GeneticAlgorythm.Individual import *

# from GeneticAlgorythm import *

import matplotlib.pyplot as plt
import numpy as np

drone_trace1 = [(400, 600), (450, 600), (500, 600), (550, 600), (600, 600), (600, 650), (600, 700), (600, 750),
                (600, 800)]
drone_trace2 = [(800, 100), (850, 100), (900, 100), (950, 100), (950, 100), (950, 150), (950, 200), (950, 250),
                (950, 300)]
drone_trace3 = [(600, 500), (650, 500), (700, 450), (750, 400), (800, 400), (850, 450), (900, 500), (950, 550),
                (1000, 550)]
drone_trace4 = [(400, 500), (450, 520), (500, 540), (550, 560), (600, 580), (650, 600), (700, 620), (700, 640),
                (700, 660)]

drone_trace = drone_trace1 + drone_trace2 + drone_trace3 + drone_trace4

GeneticAlgorythm.init(4, drone_trace)
result = GeneticAlgorythm.solve()

trace1 = np.array([[i[0], i[1]] for i in drone_trace1])
trace2 = np.array([[i[0], i[1]] for i in drone_trace2])
trace3 = np.array([[i[0], i[1]] for i in drone_trace3])
trace4 = np.array([[i[0], i[1]] for i in drone_trace4])
np_result = np.array([[i[0], i[1]] for i in result.chromosome])

plt.figure()
plt.plot(trace1[:, 0], trace1[:, 1])
plt.plot(trace2[:, 0], trace2[:, 1])
plt.plot(trace3[:, 0], trace3[:, 1])
plt.plot(trace4[:, 0], trace4[:, 1])
plt.scatter(np_result[:, 0], np_result[:, 1])
plt.xlim((0, 1000))
plt.ylim((0, 1000))
plt.show()

print("QUALITY: {0:.02f}".format(result.quality))
