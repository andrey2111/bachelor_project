# with open('test.bat', 'w') as inf:
#     for i in range(2, 10):
#         inf.write('python run_car.py -s 1000 --seed {} -f network_config_agent_0_layers_13_26_13_1.txt -e True\n'.format(i))

# with open('train.bat', 'w') as inf:
#     for i in range(1, 20):
#         inf.write('python run_car.py -s 1000 --seed {}\n'.format(i))
#         inf.write('python run_car.py -s 1000 --seed {} -f network_config_agent_0_layers_13_130_91_52_1.txt -e True\n'.format(i))

with open('results1.txt','w') as ouf:
    with open('results.txt') as inf:
        for i in inf:
            line = i.split()
            line[3] = str(float(line[3])/(2*3.141592653589793))
            ouf.write(' '.join(a for a in line) + '\n')
