# gui
from tkinter import *
import logic


class Gui:
    # Variables to help calculation
    numb: int = 0
    tempval: float = 0
    # Variables to prevent code redundancy
    templist: list = []
    frame_sco: list = []
    entry_sco: list = []

    # Defines Gui instance variables to Set up UI
    def __init__(self, window) -> None:
        # Construct initial window
        self.window = window
        self.frame_shape = Frame(self.window)
        self.label_title = Label(self.frame_shape, font=('Ariel', 11), text='STUDENT GRADE CATALOGUER')
        self.label_name = Label(self.frame_shape, font=('Ariel', 10), text=f'{"Student Name:": <20}')
        self.entry_name = Entry(self.frame_shape, width=15)
        self.label_title.pack(side='top', fill='x', pady='10')
        self.label_name.pack(side='left', padx=5)
        self.entry_name.pack(side='right', padx=12)
        self.frame_shape.pack(anchor='n')

        self.frame_numb = Frame(self.window)
        self.label_numb = Label(self.frame_numb, font=('Ariel', 10), text=f'{"No of Attempts: ": <20}')
        self.entry_numb = Entry(self.frame_numb, width=15)
        self.label_numb.pack(side='left', padx=5)
        self.entry_numb.pack(side='right', padx=14)
        self.frame_numb.pack(anchor='n')

        self.frame_disc = Frame(self.window)
        self.label_disc = Label(self.frame_disc, font=('Ariel', 6), text=f'Tab or Enter to Select Number')
        self.label_blan = Label(self.frame_disc, font=('Ariel', 6), text='')
        self.label_disc.pack(side='top')
        self.label_blan.pack(side='bottom', pady=3)
        self.frame_disc.pack(anchor='nw')


        # Set up first input box and label, invisible on startup
        self.frame_sco1 = Frame(self.window)
        self.label_sco1 = Label(self.frame_sco1, font=('Ariel', 10), text=f'{"Score 1:": >15}')
        self.entry_sco1 = Entry(self.frame_sco1, width=20)
        self.label_sco1.pack(side='left', padx=20, fill='both')
        self.entry_sco1.pack(side='right', padx=20, fill='both')
        self.frame_sco1.pack(anchor='n', pady=8)
        self.frame_sco1.pack_forget()

        # Second input box and label, invisible on startup
        self.frame_sco2 = Frame(self.window)
        self.label_sco2 = Label(self.frame_sco2, font=('Ariel', 10), text=f'{"Score 2:": >15}')
        self.entry_sco2 = Entry(self.frame_sco2, width=15)
        self.label_sco2.pack(side='left', padx=20, fill='both')
        self.entry_sco2.pack(side='right', padx=20, fill='both')
        self.frame_sco2.pack(anchor='n', pady=8)
        self.frame_sco2.pack_forget()

        # Third input box and label, invisible on startup
        self.frame_sco3 = Frame(self.window)
        self.label_sco3 = Label(self.frame_sco3, font=('Ariel', 10), text=f'{"Score 3:": >15}')
        self.entry_sco3 = Entry(self.frame_sco3, width=15)
        self.label_sco3.pack(side='left', padx=20, fill='both')
        self.entry_sco3.pack(side='right', padx=20, fill='both')
        self.frame_sco3.pack(anchor='n', pady=8)
        self.frame_sco3.pack_forget()

        # Fourth input box and label, invisible on startup
        self.frame_sco4 = Frame(self.window)
        self.label_sco4 = Label(self.frame_sco4, font=('Ariel', 10), text=f'{"Score 4:": >15}')
        self.entry_sco4 = Entry(self.frame_sco4, width=15)
        self.label_sco4.pack(side='left', padx=20, fill='both')
        self.entry_sco4.pack(side='right', padx=20, fill='both')
        self.frame_sco4.pack(anchor='n', pady=8)
        self.frame_sco4.pack_forget()

        # Set up Submit Button and Feedback label, Invisible on startup
        self.frame_butt = Frame(self.window)
        self.butt_submit = Button(self.frame_butt, text='SUBMIT', command=self.collect_data)
        self.label_butt = Label(self.frame_butt, font=('Ariel', 8), text='')
        self.butt_submit.pack(anchor='n', pady=20)
        self.label_butt.pack(anchor='s')
        self.frame_butt.pack(anchor='n', pady=30)
        self.frame_butt.pack_forget()

        # Keybinds to check entry_num whenever 'enter' / clicks off textbox
        self.entry_numb.bind("<Return>", self.reveal)
        self.entry_numb.bind("<FocusOut>", self.reveal)
        self.entry_sco1.bind("<FocusOut>", self.reveal)
        self.entry_sco2.bind("<FocusOut>", self.reveal)
        self.entry_sco3.bind("<FocusOut>", self.reveal)
        self.entry_sco4.bind("<FocusOut>", self.reveal)

    '''
    Evaluates entry inside entry_num, reveals given number of score-frames (boxes and labels)
    :self: all of the class and instance variables
    :frame_sco: and :entry_sco: used to loop through ui items to prevent redundant code
    This method does not return anything, but results in either visible or invisible frames
    '''
    def reveal(self, event) -> None:
        self.frame_sco: list = [self.frame_sco1, self.frame_sco2, self.frame_sco3, self.frame_sco4]
        self.entry_sco: list = [self.entry_sco1, self.entry_sco2, self.entry_sco3, self.entry_sco4]
        self.label_butt.forget()

        try:
            if self.entry_numb.get().strip():
                self.numb = int(self.entry_numb.get().strip())
                if self.numb not in range(1, 5):
                    raise ValueError
                self.frame_butt.forget()

                for i in range(4):  # Iterate over indices 0 to 3
                    if self.numb > i:
                        self.frame_sco[i].pack()  # Access the frame using index i
                    else:
                        self.frame_sco[i].pack_forget()

                self.butt_submit.pack()
                self.frame_butt.pack()
            else:
                raise ValueError

        except ValueError:
            for i in range(4):
                self.entry_sco[i].delete('0', 'end')
                self.frame_sco[i].pack_forget()

            self.butt_submit.pack_forget()
            self.frame_butt.pack()
            self.label_butt.pack()
            self.label_butt.config(text='Please Enter Valid Integer (1-4)', fg='blue')

    '''
    Evaluates entries in score entry boxes
    :self: all of the class and instance variables
    :entry_sco: used to loop through ui items to prevent redundant code
    This method does not return anything, but forwards entries to submit_data if there are not errors
    '''
    def collect_data(self) -> None:
        self.templist: list = []
        self.tempval: float = 0
        self.entry_sco: list = [self.entry_sco1, self.entry_sco2, self.entry_sco3, self.entry_sco4]
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

    '''
    Takes data from entry boxes and sends it through logic.py
    :self: all of the class and instance variables
    This method does not return anything, but logic.py edits a csv file
    '''
    def submit_data(self) -> None:
        if self.entry_name.get().strip():
            logic.survey(self.entry_name.get().strip(), self.templist)
            self.label_butt.pack()
            self.label_butt.config(text='Submitted', fg='green')
            self.refresh_boxes()
        else:
            self.label_butt.pack()
            self.label_butt.config(text='Please Enter Valid Name', fg='blue')

    '''
    Clears all entry boxes and submission status label. Fills entry_num with instructions
    :self: all of the class and instance variables
    This method does not return anything
    '''
    def refresh_boxes(self) -> None:
        self.entry_name.delete("0", "end")
        self.entry_numb.delete("0", "end")
        for i in range(4):
            self.entry_sco[i].delete('0', 'end')
