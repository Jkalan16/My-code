from tkinter import *

class LabelListbox(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    def labels(self):
        return sorted(self.children)

    def add_label(self, text):
        Label(self, text=text).grid()

    def configure_text(self, idx, text):
        labels = self.labels
        if idx in range(0, len(labels)):
            self.children[labels[idx]].configure(text=text)

    def remove_last(self):
        if self.labels:
            self.children[self.labels[-1]].destroy()

    def remove_by_index(self, idx):
        labels = self.labels
        if idx in range(0, len(labels)):
            self.children[labels[idx]].destroy()

    def remove_by_text(self, text):
        for label in self.labels:
            if text in self.children[label]['text']:
                self.children[label].destroy()
    

class App(Tk):
    def __init__(self):
        super().__init__()
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        lbl_listbox = LabelListbox(self)
        lbl_listbox.grid(row=0, column=0)

        for _ in range(4):
            lbl_listbox.add_label('This is Label {}'.format(_))

        self.menubar.add_command(label='Remove last',
                                 command=lbl_listbox.remove_last)

        self.menubar.add_command(label='Remove by index 1',
                                 command=lambda:lbl_listbox.remove_by_index(1))

        self.menubar.add_command(label='Change Label text"',
                                 command=lambda:lbl_listbox.
                                 configure_text(0, 'The text changed to Label 1'))

        self.menubar.add_command(label='Remove by text "Label 1"',
                                 command=lambda:lbl_listbox.remove_by_text('Label 1'))

if __name__ == '__main__':
    App().mainloop()
