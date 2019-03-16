from scripts.NetworkART1 import *
from scripts.FileWorker import *
from scripts.Window import *

if __name__ == '__main__':
    network = NetworkART1()
    worker = FileWorker('../resources/arrays.npz')
    ui = Window(network, worker)