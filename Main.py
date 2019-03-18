from scripts.NetworkART1 import *
from scripts.FileWorker import *
from scripts.Window import *
import os

if __name__ == '__main__':

    conf = {'factor_L':         2,
            'factor_p':         0.85,
            'examples_count':   5,
            'examples_width':   4,
            'examples_height':  3}

    path = os.path.dirname(os.path.abspath(__file__))
    network = NetworkART1(conf)
    worker = FileWorker(os.path.join(path, './resources/arrays.npz'), conf)
    ui = Window(network, worker, conf)