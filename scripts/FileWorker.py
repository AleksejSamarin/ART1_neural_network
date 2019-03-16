import numpy as np

class FileWorker:

    def __init__(self, path):
        self.path = path


    def load_arrays(self):
        for attempt in range(2):
            try:
                data = np.load(self.path)
            except:
                inputs = np.zeros((5, 12))
                self.save_arrays(inputs)
                print("There is no data file. Default file created.")
                continue
            return data


    def save_arrays(self, inputs):
        np.savez(self.path, inputs=inputs)