from scripts.Canvas import *
import numpy as np
import sys

class Window():

    def __init__(self, network, worker):
        self.root = tkinter.Tk(className=' ART-1 Neural network')
        self.root.configure(background='white')
        self.root.resizable(False, False)
        self.canvases = []
        self.f_top = tkinter.Frame()
        self.f_top.pack()

        # self.root.bind("<Return>", lambda l: self.run(network, data))
        self.root.bind("<l>", lambda l: self.load_canvases(worker))
        self.root.bind("<Control-s>", lambda l: worker.save_arrays(self.get_codes()))
        self.root.bind("<Escape>", self.exit)

        for i in range(5):
            canvas = Canvas(self.f_top, width=100, height=75, background='white')
            canvas.pack(side="left")
            self.canvases.append(canvas)

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.mainloop()
        return


    def load_canvases(self, worker):
        data = worker.load_arrays()
        for idx, canvas in enumerate(self.canvases):
            canvas.color_from_code(data['inputs'][idx])


    def get_codes(self, event=None):
        inputs = []
        for canvas in self.canvases:
            inputs.append(canvas.get_code())
        return np.array(inputs)


    def exit(self, event=None):
        self.root.withdraw()
        sys.exit()
