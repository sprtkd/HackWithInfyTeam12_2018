
from tkinter import *
import tkinter.ttk as ttk
py3 = True


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root1 = Tk()
    root1.withdraw()
    root = Toplevel(root1)
    top = Enrich__App (root)
    init(root, top)
    root.mainloop()
    root.destroy()


class Enrich__App:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("663x564+366+24")
        top.title("Enrich  App")
        top.configure(background="#d9d9d9")



        self.Button2_2 = Button(top)
        self.Button2_2.place(relx=0.23, rely=0.8, height=114, width=157)
        self.Button2_2.configure(activebackground="#d9d9d9")
        self.Button2_2.configure(activeforeground="#000000")
        self.Button2_2.configure(background="#d8a01e")
        self.Button2_2.configure(disabledforeground="#a3a3a3")
        self.Button2_2.configure(font=font9)
        self.Button2_2.configure(foreground="#000000")
        self.Button2_2.configure(highlightbackground="#d9d9d9")
        self.Button2_2.configure(highlightcolor="black")
        self.Button2_2.configure(pady="0")
        self.Button2_2.configure(relief=RIDGE)
        self.Button2_2.configure(text='''Add New QR''')
        self.Button2_2.configure(width=157)

        self.HistoryButton = Button(top)
        self.HistoryButton.place(relx=0.0, rely=0.8, height=114, width=157)
        self.HistoryButton.configure(activebackground="#d9d9d9")
        self.HistoryButton.configure(activeforeground="#000000")
        self.HistoryButton.configure(background="#d8a01e")
        self.HistoryButton.configure(disabledforeground="#a3a3a3")
        self.HistoryButton.configure(font=font9)
        self.HistoryButton.configure(foreground="#000000")
        self.HistoryButton.configure(highlightbackground="#d9d9d9")
        self.HistoryButton.configure(highlightcolor="black")
        self.HistoryButton.configure(pady="0")
        self.HistoryButton.configure(relief=RIDGE)
        self.HistoryButton.configure(text='''History''')
        self.HistoryButton.configure(width=157)

        self.Scan = Button(top)
        self.Scan.place(relx=0.45, rely=0.8, height=114, width=367)
        self.Scan.configure(activebackground="#d9d9d9")
        self.Scan.configure(activeforeground="#000000")
        self.Scan.configure(background="#d8a01e")
        self.Scan.configure(disabledforeground="#a3a3a3")
        self.Scan.configure(font=font10)
        self.Scan.configure(foreground="#000000")
        self.Scan.configure(highlightbackground="#d9d9d9")
        self.Scan.configure(highlightcolor="black")
        self.Scan.configure(pady="0")
        self.Scan.configure(relief=RIDGE)
        self.Scan.configure(text='''Scan''')
        self.Scan.configure(width=367)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=451, width=664)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self._img1 = PhotoImage(file="startup.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=664)






if __name__ == '__main__':
    vp_start_gui()



