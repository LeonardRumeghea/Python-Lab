from tkinter import *
from message import Message

BUTTON_COLOR = "#4860A0"
BUTTON_FONT = "Helvetica 14 bold"
BUTTON_FG = "#EAECEE"

BACKGROUND_COLOR = "#343746"
PANEL_COLOR = "#282A36"

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

    def auth_menu(self):

        self.login = Toplevel()

        self.login.title("Authentication Menu")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=500)

        self.pls = Label(self.login, text="Please authenticate to continue", justify=CENTER, font=BUTTON_FONT)
        self.pls.place(relheight=0.15, relx=0.15, rely=0.07)
        
        self.enter_name_label = Label(self.login, text="Username:", font="Helvetica 13")
        self.enter_name_label.place(relheight=0.2, relx=0.1, rely=0.30)

        self.enter_name = Entry(self.login, font="Helvetica 14")
        self.enter_name.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.35)

        self.enter_password_label = Label(self.login, text="Password:", font="Helvetica 13")
        self.enter_password_label.place(relheight=0.2, relx=0.1, rely=0.50)

        self.enter_password = Entry(self.login, font="Helvetica 14", show="•")
        self.enter_password.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.55)

        self.enter_name.focus()  

        self.login_btn = Button(self.login, text="Login", font=BUTTON_FONT, 
            command=lambda: self.goAhead(self.enterName.get())
        )
        self.login_btn.place(relx=0.3, rely=0.75)

        self.register_btn = Button( self.login, text="Register", font=BUTTON_FONT, 
            command=lambda: self.goAhead(self.enterName.get())
        )
        self.register_btn.place(relx=0.5, rely=0.75)

        self.login.mainloop()

    def chat_box(self, name):
            
            self.Window.deiconify()
            self.Window.title("Messenger")
            self.Window.resizable(width=False, height=False)
            self.Window.configure(width=450, height=600, bg=BACKGROUND_COLOR)
    
            self.labelHead = Label(self.Window, bg=PANEL_COLOR, fg=BUTTON_FG, text=name, font="Helvetica 13 bold", pady=5)
            self.labelHead.place(relwidth=1)
    
            self.textCons = Text(self.Window, width=20, height=2, bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 14", padx=5, pady=5)
            self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)
    
            self.labelBottom = Label(self.Window, bg=BACKGROUND_COLOR, height=80)
            self.labelBottom.place(relwidth=1, rely=0.825)
    
            self.entryMsg = Entry(self.labelBottom, bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 14")
            self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.entryMsg.focus()
    
            self.buttonMsg = Button(self.labelBottom, text="Send", font="Helvetica 20 bold", width=20, bg=BUTTON_COLOR, 
                command=lambda: self.sendButton(self.entryMsg.get())
            )
            self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
    
            self.textCons.config(cursor="arrow")
    
            scrollbar = Scrollbar(self.textCons, bg=BACKGROUND_COLOR, activebackground=BUTTON_COLOR, cursor="arrow")
            scrollbar.place(relheight=1, relx=0.974)
            scrollbar.config(command=self.textCons.yview)
    
            self.textCons.config(state=DISABLED)

            self.Window.mainloop()

    def main_menu(self):
        self.Window.deiconify()
        self.Window.title("Messenger")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=720, height=480, bg=BACKGROUND_COLOR)

        self.labelHead = Label(self.Window, bg=PANEL_COLOR, fg=BUTTON_FG, text="Welcome to Messenger", font="Helvetica 13 bold", pady=5)
        self.labelHead.place(relwidth=1)

        side_panel = Frame(self.Window, bg=PANEL_COLOR, width=200, height=430)
        side_panel.place(relx=0.01, rely=0.085)

        self.btn_send = Button(side_panel, text="Send ", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG, 
            command=self.show_send_panel)
        self.btn_send.place(relx=0.05, rely=0.05, relheight=0.1, relwidth=0.90)

        self.btn_inbox = Button(side_panel, text="Inbox", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG,
            command=self.show_inbox_panel)
        self.btn_inbox.place(relx=0.05, rely=0.20, relheight=0.1, relwidth=0.90)

        self.btn_outbox = Button(side_panel, text="Outbox", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG,
            command=self.show_outbox_panel)
        self.btn_outbox.place(relx=0.05, rely=0.35, relheight=0.1, relwidth=0.90)

        self.btn_exit = Button(side_panel, text="Exit", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG)
        self.btn_exit.place(relx=0.12, rely=0.85, relheight=0.1, relwidth=0.75)

        self.main_panel = Frame(self.Window, bg=PANEL_COLOR, width=495, height=430)
        self.main_panel.place(relx=0.30, rely=0.085)

        self.main_panel_label = Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="Main Panel", font="Helvetica 13 bold", pady=5)
        self.main_panel_label.place(relwidth=1)

        self.Window.mainloop()

    def message_window(self):
        self.Window.deiconify()
        self.Window.title("Messenger")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=450, height=600, bg=BACKGROUND_COLOR)

        self.labelHead = Label(self.Window, text="Message from ", bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 13 bold", pady=5)
        self.labelHead.place(relwidth=1)

        self.text_Subject = Label(self.Window, text="Subject: ", bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 13 bold", pady=5)
        self.text_Subject.place(relwidth=1, rely=0.07)

        self.text_content = Label(self.Window, text="Content: ", bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 13 bold", pady=5)
        self.text_content.place(relwidth=1, rely=0.14)

        self.textCons = Text(self.Window, width=20, height=2, bg=PANEL_COLOR, fg=BUTTON_FG, font="Helvetica 14", padx=5, pady=5)
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.19)

        self.textCons.config(cursor="arrow")

        scrollbar = Scrollbar(self.textCons, bg=BACKGROUND_COLOR, activebackground=BUTTON_COLOR, cursor="arrow")
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

        self.Window.mainloop()

    def show_send_panel(self):

        self.remove_widgets()

        self.main_panel_label.config(text="Send Message")

        self.line = Label(self.main_panel, bg=BUTTON_COLOR)
        self.line.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        self.to = Label(self.main_panel, text="To:", font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG)
        self.to.place(relx=0.05, rely=0.125)

        self.to_entry = Entry(self.main_panel, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        self.to_entry.place(relx=0.15, rely=0.125, relwidth=0.70)

        self.content = Label(self.main_panel, text="Content:", font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG)
        self.content.place(relx=0.05, rely=0.20)

        self.content_entry = Text(self.main_panel, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG, wrap=WORD, padx=10, pady=10)
        self.content_entry.place(relx=0.05, rely=0.30, relwidth=0.90, relheight=0.50)

        self.attach = Button(self.main_panel, text="Attach", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG)
        self.attach.place(relx=0.05, rely=0.85, relwidth=0.20)

        self.send_button = Button(self.main_panel, text="Send", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG)
        self.send_button.place(relx=0.75, rely=0.90, relwidth=0.20, relheight=0.08)

    def remove_widgets(self):
        for widget in self.main_panel.winfo_children():
            
            if widget.winfo_children() != ():
                for child in widget.winfo_children():
                    child.destroy()
            if widget == self.main_panel_label:
                continue
            widget.destroy()

    def show_inbox_panel(self):

        self.remove_widgets()

        self.main_panel_label.config(text="")

        buff = seed()

        self.messages = Canvas(self.main_panel, bg=PANEL_COLOR)
        self.messages.place(relx=0.05, rely=0.125, relwidth=0.90, relheight=0.85)

        text = Label(self.main_panel_label, text="Inbox", font="Helvetica 13 bold", bg=PANEL_COLOR, fg=BUTTON_FG)
        text.place(relx=0.05, rely=0.05)

        search = Entry(self.main_panel_label, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        search.place(relx=0.45, rely=0.2, relwidth=0.35)

        button_search = Button(self.main_panel_label, text="Search", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG,
            command=lambda: filter_messages(self.messages, buff, search.get()))
        button_search.place(relx=0.825, rely=0.2, relwidth=0.15, relheight=0.8)

        self.line = Label(self.main_panel, bg=BUTTON_COLOR)
        self.line.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        self.scrollbar = Scrollbar(self.main_panel, orient="vertical", command=self.messages.yview)
        self.scrollbar.place(relx=0.95, rely=0.125, relheight=0.85)

        display_messages(self.messages, buff)

        self.messages.configure(scrollregion=self.messages.bbox('all'), yscrollcommand=self.scrollbar.set)

    def show_outbox_panel(self):
        self.remove_widgets()

        self.main_panel_label.config(text="")

        buff = seed()

        self.messages = Canvas(self.main_panel, bg=PANEL_COLOR)
        self.messages.place(relx=0.05, rely=0.125, relwidth=0.90, relheight=0.85)

        text = Label(self.main_panel_label, text="Outbox", font="Helvetica 13 bold", bg=PANEL_COLOR, fg=BUTTON_FG)
        text.place(relx=0.05, rely=0.05)

        search = Entry(self.main_panel_label, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        search.place(relx=0.45, rely=0.2, relwidth=0.35)

        button_search = Button(self.main_panel_label, text="Search", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG,
            command=lambda: filter_messages(self.messages, buff, search.get()))
        button_search.place(relx=0.825, rely=0.2, relwidth=0.15, relheight=0.8)

        self.line = Label(self.main_panel, bg=BUTTON_COLOR)
        self.line.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        self.scrollbar = Scrollbar(self.main_panel, orient="vertical", command=self.messages.yview)
        self.scrollbar.place(relx=0.95, rely=0.125, relheight=0.85)

        display_messages(self.messages, buff)

        self.messages.configure(scrollregion=self.messages.bbox('all'), yscrollcommand=self.scrollbar.set)
    
    def sendButton(self, msg):
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, "You: " + msg + '\n')



def filter_messages(messages, buff, name = None):
    for widget in messages.winfo_children():
        widget.destroy()

    display_messages(messages, buff, name if name != "" else None)

def display_messages(messages, buff, name = None):
    i = 0
    for msg in buff:
        if name == None or msg.from_user == name:

            frame = Frame(messages, bg=PANEL_COLOR, padx=10, pady=10)
            message = Label(frame, text=f"From: {msg.from_user} - {msg.content}", font="Helvetica 13",
                bg=PANEL_COLOR, fg=BUTTON_FG)
            message.place(relx = 0, rely = 0, relwidth=1, relheight=1)
            message.pack(side=LEFT, anchor="nw")

            btn = Button(frame, text="Open", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG)
            btn.place(relx=0.75, rely=0.03, relwidth=0.20, relheight=0.90)
            btn.pack(side=RIGHT, anchor="nw")

            messages.create_window(0, i * 60, anchor='nw', window=frame, height=50, width=430)

            i += 1

def seed():
    return [
        Message("Mihai", "Alex", "Buna", "Salut"),
        Message("Alex", "Mihai", "Salut", "Buna"),
        Message("Mihai", "Alex", "Ce faci?", "Bine"),
        Message("Alex", "Mihai", "Bine", "Ce faci?"),
        Message("Mihai", "Alex", "Bine", "Ce faci?"),
        Message("Alex", "Mihai", "Bine", "Ce faci?"),
        Message("Mihai", "Alex", "Bine", "Ce faci?"),
        Message("Mihai", "Alex", "Bine", "Ce faci?"),
        Message("Mihai", "Alex", "Bine", "Ce faci?"),
        Message("Mihai", "Alex", "Bine", "Ce faci?")
    ]
    
GUI().auth_menu()