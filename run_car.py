from cars.world import SimpleCarWorld
from cars.agent import SimpleCarAgent
from cars.physics import SimplePhysics
from cars.track import generate_map, generate_obstacles, get_partition
import numpy as np
import random

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--steps", type=int)
parser.add_argument("-f", "--filename", type=str)
parser.add_argument("-e", "--evaluate", type=bool)
parser.add_argument("--seed", type=int)
args = parser.parse_args()

print(args.steps, args.seed, args.filename, args.evaluate)

steps = args.steps
seed = args.seed if args.seed else 23
np.random.seed(seed)
random.seed(seed)
m = generate_map(20, 2, 1, 1)
radii = np.random.normal(loc=2.5, scale=0.2, size=8)
angles = get_partition(8, -np.pi, np.pi)
o = generate_obstacles(8, radii, angles, 0)

if args.filename:
    agent = SimpleCarAgent.from_file(args.filename)
    w = SimpleCarWorld(1, m, o, radii, angles, SimplePhysics, SimpleCarAgent, timedelta=0.2)
    if args.evaluate:
        with open('results.txt', 'a') as inf:
            circles, collisions = w.evaluate_agent(agent, SimplePhysics, steps, timedelta=0.2)
            inf.write('seed: {} circles: {} collisions: {} \n'.format(seed, circles, collisions))
    else:
        w.set_agents([agent])
        w.run(SimplePhysics, steps, timedelta=0.2)
else:
    SimpleCarWorld(1, m, o, radii, angles, SimplePhysics, SimpleCarAgent, timedelta=0.2).run(SimplePhysics, steps, timedelta=0.2)
