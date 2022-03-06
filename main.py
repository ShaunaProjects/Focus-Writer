from tkinter import *
from tkinter.scrolledtext import ScrolledText

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Focus Writer")
        self.background_color = "#EAF6F6"
        self.config(padx=20, pady=20, bg=self.background_color)
        self.font = "Arial"
        self.run_countdown = False
        self.start_num_char = 0
        self.new_num_char = 0
        self.time_left = 10
        self.title_label = Label(text="Focus Writer",
                                 bg=self.background_color,
                                 font=(self.font, 26))
        self.title_label.grid(row=0, column=0, columnspan=2)
        self.explain = Label(text="Welcome to the Focus Writer app. You need to continuously input content in order to "
                                  "keep the app from erasing your data. If the app detects that you haven't written "
                                  "anything for more than 10 seconds, it will wipe everything, and you will need to "
                                  "start over. \n\nPress the start button when you are ready to begin.\n",
                             bg=self.background_color,
                             font=(self.font, 18),
                             wraplength=850,
                             justify="left",)
        self.explain.grid(row=1, column=0, columnspan=2)
        self.start_img = PhotoImage(file="play-button.png")
        self.start_button = Button(image=self.start_img,
                                   height=50,
                                   command=self.check_writing)
        self.start_button.grid(row=2, column=0)
        self.time_left_label = Label(text=self.time_left,
                                     bg=self.background_color,
                                     font=(self.font, 36))
        self.time_left_label.grid(row=2, column=1)
        self.entry_box = ScrolledText(width=80,
                                      height=20,
                                      wrap=WORD,
                                      font=(self.font, 14))
        self.entry_box.grid(row=3, column=0, columnspan=2)

    def countdown(self):
        if self.run_countdown:
            if self.time_left > 0:
                self.time_left -= 1
                self.time_left_label.configure(text=self.time_left)
                self.after(1000, self.countdown)
            elif self.time_left == 0:
                self.entry_box.delete(1.0, "end-1c")
                self.start_num_char = 0

    def start_wordcount(self):
        self.start_num_char = len(self.entry_box.get(1.0, "end-1c"))
        self.after(5000, self.get_wordcount)

    def get_wordcount(self):
        self.new_num_char = len(self.entry_box.get(1.0, "end-1c"))
        print(self.start_num_char)
        print(self.new_num_char)
        if self.new_num_char != self.start_num_char:
            self.run_countdown = False
            self.start_num_char = self.new_num_char
            self.time_left = 10
            self.time_left_label.configure(text=self.time_left)
        else:
            self.run_countdown = True
            self.countdown()
        self.after(5000, self.get_wordcount())

    def check_writing(self):
        self.start_button["state"] = DISABLED
        self.entry_box.focus()
        self.start_wordcount()

app = App()
app.mainloop()