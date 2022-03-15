# from tkinter import *
import tkinter as tk
from tkinter import ttk
import clipboard as cclip


# import tkinter as tk

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.grid()
        # self.pack()
        ttk.Label(text="Points: ").grid(column=0, row=0)
        self.ptsEntry = ttk.Entry()
        self.ptsEntry.grid(column=1, row=0)
        self.ptsVar = tk.StringVar()
        self.ptsVar.set("A B C D")
        self.ptsEntry["textvariable"] = self.ptsVar
        self.ptsEntry.bind('<Key-Return>', self.gen_bezier)

        ttk.Label(text="Bézier: ").grid(column=0, row=1)
        self.bezierLabel = ttk.Label(text="")
        self.bezierLabel.grid(column=1, row=1)

        ttk.Button(text="Quit", command=root.destroy).grid(column=0, row=2)

        self.ptsEntry.focus()

    def gen_bezier(self, event):
        #
        points_str = self.ptsVar.get()
        points = points_str.split()
        curve_str = ""
        match len(points):
            case 3:
                curve_str = self.gen_bezier_3(points)
            case 4:
                curve_str = self.gen_bezier_4(points)
            case 5:
                curve_str = self.gen_bezier_5(points)
            case 6:
                curve_str = self.gen_bezier_6(points)
            case _:
                self.bezierLabel['text'] = "Bad entry!"
                return
        self.bezierLabel['text'] = curve_str
        cclip.copy(curve_str)
        pass

    @staticmethod
    def gen_bezier_3(points):
        fmtstr = "Curve(x({A}) (1-t)^(2)+x({B})*2 t (1-t)+x({C})* t^(2),y({A}) (1-t)^(2)+y({B})*2 t (1-t)+y({C})* t^(" \
                 "2),t,0,1) "
        return fmtstr.format(A=points[0], B=points[1], C=points[2])

    @staticmethod
    def gen_bezier_4(points):
        fmtstr = "Curve(x({A}) (1-t)^(3)+x({B})*3 t (1-t)^(2)+x({C})*3 t^(2) (1-t)+x({D}) t^(3),y({A}) (1-t)^(3)+y({" \
                 "B})*3 t (1-t)^(2)+y({C})*3 t^(2) (1-t)+y({D}) t^(3),t,0,1) "
        return fmtstr.format(A=points[0], B=points[1], C=points[2], D=points[3])

    @staticmethod
    def gen_bezier_5(points):
        fmtstr = "Curve(" \
                 "x({A}) (1-t)^(4)" \
                 "+ x({B})*4 t (1-t)^(3)" \
                 "+ x({C})*6 t^(2) (1-t)^(2)" \
                 "+ x({D})*4 t^(3) (1-t)" \
                 "+ x({E}) t^(4)," \
                 "y({A}) (1-t)^(4)" \
                 "+ y({B})*4 t (1-t)^(3)" \
                 "+ y({C})*6 t^(2) (1-t)^(2)" \
                 "+ y({D})*4 t^(3) (1-t)" \
                 "+ y({E}) t^(4)," \
                 "t,0,1) "
        return fmtstr.format(A=points[0], B=points[1], C=points[2], D=points[3], E=points[4])

    @staticmethod
    def gen_bezier_6(points):
        fmtstr = "Curve(" \
                 "x({A}) (1-t)^(5)" \
                 "+ x({B})*5 t (1-t)^(4)" \
                 "+ x({C})*10 t^(2) (1-t)^(3)" \
                 "+ x({D})*10 t^(3) (1-t)^(2)" \
                 "+ x({E})*5 t^(4) (1-t)" \
                 "+ x({F}) t^(5)," \
                 "y({A}) (1-t)^(5)" \
                 "+ y({B})*5 t (1-t)^(4)" \
                 "+ y({C})*10 t^(2) (1-t)^(3)" \
                 "+ y({D})*10 t^(3) (1-t)^(2)" \
                 "+ y({E})*5 t^(4) (1-t)" \
                 "+ y({F}) t^(5)," \
                 "t,0,1) "
        return fmtstr.format(A=points[0], B=points[1], C=points[2], D=points[3], E=points[4], F=points[5])


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
