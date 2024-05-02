# gui
from tkinter import *
import logic


class Gui:
    numb = 0
    templist = []
    tempval = 0
    entry_sco = []

    def __init__(self, window):
        # Construct initial window
        self.window = window
        self.frame_shape = Frame(self.window)
        self.label_title = Label(self.frame_shape, font=('Ariel', 11), text='STUDENT GRADE CATALOGUER')
        self.label_name = Label(self.frame_shape, font=('Ariel', 10), text=f'{"Student Name:": <20}')
        self.entry_name = Entry(self.frame_shape, width=15)
        self.label_title.pack(side='top', fill='x', pady='10')
        self.label_name.pack(side='left', padx=5)
        self.entry_name.pack(side='right', padx=15)
        self.frame_shape.pack(anchor='n')

        self.frame_numb = Frame(self.window)
        self.label_numb = Label(self.frame_numb, font=('Ariel', 10), text=f'{"No of Attempts: ": <20}')
        self.entry_numb = Entry(self.frame_numb, width=15)
        self.label_numb.pack(side='left', padx=5)
        self.entry_numb.pack(side='right', padx=15)
        self.entry_numb.insert(0, '(Enter = Choose)')
        self.frame_numb.pack(anchor='n', pady=15)

        self.frame_sco1 = Frame(self.window)
        self.label_sco1 = Label(self.frame_sco1, font=('Ariel', 10), text=f'{"Score 1:": >15}')
        self.entry_sco1 = Entry(self.frame_sco1, width=15)
        self.label_sco1.pack(side='left', padx=20, fill='both')
        self.entry_sco1.pack(side='right', padx=20, fill='both')
        self.frame_sco1.pack(anchor='n', pady=5)
        self.frame_sco1.pack_forget()

        self.frame_sco2 = Frame(self.window)
        self.label_sco2 = Label(self.frame_sco2, font=('Ariel', 10), text=f'{"Score 2:": >15}')
        self.entry_sco2 = Entry(self.frame_sco2, width=15)
        self.label_sco2.pack(side='left', padx=20, fill='both')
        self.entry_sco2.pack(side='right', padx=20, fill='both')
        self.frame_sco2.pack(anchor='n', pady=5)
        self.frame_sco2.pack_forget()

        self.frame_sco3 = Frame(self.window)
        self.label_sco3 = Label(self.frame_sco3, font=('Ariel', 10), text=f'{"Score 3:": >15}')
        self.entry_sco3 = Entry(self.frame_sco3, width=15)
        self.label_sco3.pack(side='left', padx=20, fill='both')
        self.entry_sco3.pack(side='right', padx=20, fill='both')
        self.frame_sco3.pack(anchor='n', pady=5)
        self.frame_sco3.pack_forget()

        self.frame_sco4 = Frame(self.window)
        self.label_sco4 = Label(self.frame_sco4, font=('Ariel', 10), text=f'{"Score 4:": >15}')
        self.entry_sco4 = Entry(self.frame_sco4, width=15)
        self.label_sco4.pack(side='left', padx=20, fill='both')
        self.entry_sco4.pack(side='right', padx=20, fill='both')
        self.frame_sco4.pack(anchor='n', pady=5)
        self.frame_sco4.pack_forget()

        self.frame_butt = Frame(self.window)
        self.butt_submit = Button(self.frame_butt, text='SUBMIT', command=self.collect_data)
        self.label_butt = Label(self.frame_butt, font=('Ariel', 8), text='')
        self.butt_submit.pack(anchor='n', pady=15)
        self.label_butt.pack(anchor='s')
        self.frame_butt.pack(anchor='n', pady=20)
        self.frame_butt.pack_forget()

        self.entry_numb.bind("<Return>", self.reveal)
        self.entry_numb.bind("<FocusOut>", self.reveal)
        self.entry_sco1.bind("<FocusOut>", self.reveal)
        self.entry_sco2.bind("<FocusOut>", self.reveal)
        self.entry_sco3.bind("<FocusOut>", self.reveal)
        self.entry_sco4.bind("<FocusOut>", self.reveal)

    def reveal(self, event):
        self.label_butt.forget()
        try:
            if self.entry_numb.get().strip():
                self.numb = int(self.entry_numb.get().strip())
                if self.numb not in range(1, 5):
                    raise ValueError

                self.frame_butt.forget()
                if self.numb >= 1:
                    self.frame_sco1.pack()
                else:
                    self.frame_sco1.pack_forget()

                if self.numb >= 2:
                    self.frame_sco2.pack()
                else:
                    self.frame_sco2.pack_forget()

                if self.numb >= 3:
                    self.frame_sco3.pack()
                else:
                    self.frame_sco3.pack_forget()

                if self.numb == 4:
                    self.frame_sco4.pack()
                else:
                    self.frame_sco4.pack_forget()

                self.butt_submit.pack()
                self.frame_butt.pack()
            else:
                raise ValueError

        except ValueError:
            self.entry_sco1.delete('0', 'end')
            self.frame_sco1.pack_forget()
            self.entry_sco2.delete('0', 'end')
            self.frame_sco2.pack_forget()
            self.entry_sco3.delete('0', 'end')
            self.frame_sco3.pack_forget()
            self.entry_sco4.delete('0', 'end')
            self.frame_sco4.pack_forget()
            self.butt_submit.pack_forget()

            self.frame_butt.pack()
            self.label_butt.pack()
            self.label_butt.config(text='Please Enter Valid Integer (1-4)', fg='blue')

    def collect_data(self):
        self.templist = []
        self.tempval = 0
        self.entry_sco = [self.entry_sco1, self.entry_sco2, self.entry_sco3, self.entry_sco4]
        self.label_butt.pack_forget()

        try:
            for i in range(self.numb):
                tempval = float(self.entry_sco[i].get().strip())
                if tempval < 0 or tempval > 100:
                    raise ValueError
                self.templist.append(tempval)

            self.label_butt.pack_forget()
            self.submit_data()

        except ValueError:
            self.label_butt.pack()
            self.label_butt.config(text='Please Enter Valid Scores', fg='red')

    def submit_data(self):
        if self.entry_name.get().strip():
            logic.survey(self.entry_name.get().strip(), self.templist)
            self.label_butt.pack()
            self.label_butt.config(text='Submitted', fg='green')
            self.refresh_boxes()
        else:
            self.label_butt.pack()
            self.label_butt.config(text='Please Enter Valid Name', fg='blue')

    def refresh_boxes(self):
        self.entry_name.delete("0", "end")
        self.entry_numb.delete("0", "end")
        self.entry_sco1.delete("0", "end")
        self.entry_sco2.delete("0", "end")
        self.entry_sco3.delete("0", "end")
        self.entry_sco4.delete("0", "end")
