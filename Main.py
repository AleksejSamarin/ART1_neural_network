import scripts
import os

if __name__ == '__main__':

    conf = {'factor_L':         2,
            'factor_p':         0.80,
            'examples_count':   5,
            'examples_width':   4,
            'examples_height':  3}

    path = os.path.dirname(os.path.abspath(__file__))
    network = scripts.NetworkART1(conf)
    worker = scripts.FileWorker(os.path.join(path, './resources/arrays.npz'), conf)
    ui = scripts.Window(network, worker, conf)