from scripts.Canvas import *
import numpy as np
import sys

class Window():

    def __init__(self, network, worker, conf):
        self.root = tkinter.Tk(className=' ART-1 Neural network')
        self.root.configure(background='white')
        self.root.resizable(False, False)
        self.canvases = []
        self.f_top = tkinter.Frame()
        self.f_top.pack()
        self.c = conf['examples_count']
        self.w = conf['examples_width']
        self.h = conf['examples_height']
        self.size = 25

        self.root.bind("<Return>", lambda l: network.run(self.get_codes()))
        self.root.bind("<l>", lambda l: self.load_canvases(worker))
        self.root.bind("<Control-s>", lambda l: worker.save_arrays(self.get_codes()))
        self.root.bind("<Escape>", self.exit)

        for i in range(self.c):
            canvas = Canvas(self.w, self.h, self.size, self.f_top, width=self.size * self.w, height=self.size * self.h, background='white')
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
