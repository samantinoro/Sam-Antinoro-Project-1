# main
# opens gui
from gui import *


def main():
    window = Tk()
    window.title('Student Grade Calculator')
    window.geometry('250x325')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
