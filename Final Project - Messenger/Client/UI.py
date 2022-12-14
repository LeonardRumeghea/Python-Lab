from tkinter import *
from CONSTANTS import *
from utils_client import *
import socket

BUTTON_COLOR = "#4860A0"
BUTTON_FONT = "Helvetica 14 bold"
BUTTON_FG = "#EAECEE"

BACKGROUND_COLOR = "#343746"
PANEL_COLOR = "#282A36"

class GUI:
    def __init__(self, socket):
        self.socket = socket
        self.username = ""
        self.Window = Tk()
        self.Window.withdraw()

    def auth_window(self):
        self.Window.deiconify()
        self.Window.title("Python Messenger Application")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=400, height=500, bg=BACKGROUND_COLOR)

        Label(self.Window, bg=BACKGROUND_COLOR, fg=BUTTON_FG, text="Welcome!", font=BUTTON_FONT, pady=10) \
            .place(relwidth=1, rely=0.1)

        Label(self.Window, text="Username:", bg=BACKGROUND_COLOR, fg=BUTTON_FG, font=BUTTON_FONT) \
            .place(relx=0.05, rely=0.3, relwidth=0.3, relheight=0.1)

        self.entry_username = Entry(self.Window, bg=PANEL_COLOR, fg=BUTTON_FG, font=BUTTON_FONT)
        self.entry_username.place(relx=0.35, rely=0.31, relwidth=0.6, relheight=0.07)

        Label(self.Window, text="Password:", bg=BACKGROUND_COLOR, fg=BUTTON_FG, font=BUTTON_FONT) \
            .place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.1)

        self.entry_password = Entry(self.Window, bg=PANEL_COLOR, fg=BUTTON_FG, font=BUTTON_FONT, show="*")
        self.entry_password.place(relx=0.35, rely=0.41, relwidth=0.6, relheight=0.07)

        self.label_error = Label(self.Window, text="", bg=BACKGROUND_COLOR, fg="#FF4B43", font=BUTTON_FONT)
        self.label_error.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.1)

        Button(self.Window, text="Login", font=BUTTON_FONT, width=10, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.login) \
            .place(relx=0.15, rely=0.6, relwidth=0.3, relheight=0.1)

        Button(self.Window, text="Register", font=BUTTON_FONT, width=10, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.register) \
            .place(relx=0.55, rely=0.6, relwidth=0.3, relheight=0.1)

        Button(self.Window, text="Exit", font=BUTTON_FONT, width=10, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.close) \
            .place(relx=0.40, rely=0.80, relwidth=0.2, relheight=0.1)

        self.Window.mainloop()

    def main_window(self):

        self.Window.deiconify()
        self.Window.title("Python Messenger Application")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=720, height=480, bg=BACKGROUND_COLOR)

        Label(self.Window, bg=PANEL_COLOR, fg=BUTTON_FG, text="VS Messenger", font="Helvetica 13 bold", pady=5).place(relwidth=1)

        side_panel = Frame(self.Window, bg=PANEL_COLOR, width=200, height=430)
        side_panel.place(relx=0.01, rely=0.085)

        Button(side_panel, text="Send ", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.show_send_panel) \
            .place(relx=0.05, rely=0.05, relheight=0.1, relwidth=0.90)

        Button(side_panel, text="Inbox", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.show_inbox_panel) \
            .place(relx=0.05, rely=0.20, relheight=0.1, relwidth=0.90)

        Button(side_panel, text="Outbox", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.show_outbox_panel) \
            .place(relx=0.05, rely=0.35, relheight=0.1, relwidth=0.90)

        Button(side_panel, text="Exit", font=BUTTON_FONT, width=20, bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.close) \
            .place(relx=0.12, rely=0.85, relheight=0.1, relwidth=0.75)

        self.main_panel = Frame(self.Window, bg=PANEL_COLOR, width=495, height=430)
        self.main_panel.place(relx=0.30, rely=0.085)

        self.main_panel_header = Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="Wellcome!", font="Helvetica 13 bold", pady=5)
        self.main_panel_header.place(relwidth=1)

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

        self.remove_widgets(self.main_panel)

        Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="Send Message", font="Helvetica 13 bold", pady=5).place(relwidth=1)
        Label(self.main_panel, bg=BUTTON_COLOR).place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        Label(self.main_panel, text="To:", font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG).place(relx=0.05, rely=0.125)
        self.receiver_entry = Entry(self.main_panel, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        self.receiver_entry.place(relx=0.15, rely=0.125, relwidth=0.70)

        Label(self.main_panel, text="Content:", font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG).place(relx=0.05, rely=0.20)
        self.content_entry = Text(self.main_panel, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG, wrap=WORD, padx=10, pady=10)
        self.content_entry.place(relx=0.05, rely=0.30, relwidth=0.90, relheight=0.50)

        Button(self.main_panel, text="Attach", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG) \
            .place(relx=0.05, rely=0.85, relwidth=0.20)

        self.label_image_name = Label(self.main_panel, text="", font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG)
        self.label_image_name.place(relx=0.275, rely=0.86)

        Button(self.main_panel, text="Send", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG, command=self.send_message) \
            .place(relx=0.75, rely=0.90, relwidth=0.20, relheight=0.08)

        self.confirmation_label = Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="", font="Helvetica 20", pady=5)
        self.confirmation_label.place(rely=0.885, relx = 0.675)

    def show_inbox_panel(self):

        self.remove_widgets(self.main_panel)

        inbox_messages = load_inbox(self.socket)

        self.main_panel_header = Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="", font="Helvetica 13 bold", pady=5)
        self.main_panel_header.place(relwidth=1)

        self.messages_panel = Canvas(self.main_panel, bg=PANEL_COLOR)
        self.messages_panel.place(relx=0.05, rely=0.125, relwidth=0.90, relheight=0.85)

        Label(self.main_panel_header, text="Inbox", font="Helvetica 13 bold", bg=PANEL_COLOR, fg=BUTTON_FG).place(relx=0.05, rely=0.05)

        search = Entry(self.main_panel_header, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        search.place(relx=0.45, rely=0.2, relwidth=0.35)

        Button(self.main_panel_header, text="Search", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG,
                command=lambda: filter_messages(self.messages_panel, inbox_messages, True, search.get())) \
            .place(relx=0.825, rely=0.2, relwidth=0.15, relheight=0.8)

        Label(self.main_panel, bg=BUTTON_COLOR).place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        self.scrollbar = Scrollbar(self.main_panel, orient="vertical", command=self.messages_panel.yview)
        self.scrollbar.place(relx=0.95, rely=0.125, relheight=0.85)

        display_messages(self.messages_panel, inbox_messages, True)

        self.messages_panel.configure(scrollregion=self.messages_panel.bbox('all'), yscrollcommand=self.scrollbar.set)

    def show_outbox_panel(self):

        self.remove_widgets(self.main_panel)
        outbox_messages = load_outbox(self.socket)

        self.main_panel_header = Label(self.main_panel, bg=PANEL_COLOR, fg=BUTTON_FG, text="", font="Helvetica 13 bold", pady=5)
        self.main_panel_header.place(relwidth=1)    

        self.messages_panel = Canvas(self.main_panel, bg=PANEL_COLOR)
        self.messages_panel.place(relx=0.05, rely=0.125, relwidth=0.90, relheight=0.85)

        Label(self.main_panel_header, text="Outbox", font="Helvetica 13 bold", bg=PANEL_COLOR, fg=BUTTON_FG).place(relx=0.05, rely=0.05)

        search = Entry(self.main_panel_header, font="Helvetica 13", bg=BACKGROUND_COLOR, fg=BUTTON_FG)
        search.place(relx=0.45, rely=0.2, relwidth=0.35)

        Button(self.main_panel_header, text="Search", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG,
                    command=lambda: filter_messages(self.messages_panel, outbox_messages, False, search.get())) \
            .place(relx=0.825, rely=0.2, relwidth=0.15, relheight=0.8)

        Label(self.main_panel, bg=BUTTON_COLOR).place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.001)

        self.scrollbar = Scrollbar(self.main_panel, orient="vertical", command=self.messages_panel.yview)
        self.scrollbar.place(relx=0.95, rely=0.125, relheight=0.85)

        display_messages(self.messages_panel, outbox_messages, False)

        self.messages_panel.configure(scrollregion=self.messages_panel.bbox('all'), yscrollcommand=self.scrollbar.set)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "" or password == "":
            return

        result = login_function(self.socket, username, password)

        if result == True:
            self.username = username
            self.remove_widgets(self.Window)
            self.main_window()
        else:
            self.label_error.configure(text="Wrong username or password")

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "" or password == "":
            return

        result = register_function(self.socket, username, password)

        if result == True:
            self.username = username
            self.remove_widgets(self.Window)
            self.chat_window()
        else:
            self.label_error.configure(text="Username already exists")
    
    def send_message(self):
        receiver = self.receiver_entry.get()
        content = self.content_entry.get("1.0",'end-1c')

        if receiver == "" or content == "":
            return

        if receiver == self.username:
            self.confirmation_label.configure(text="✖")
            return

        result = send_message(self.socket, self.username, receiver, content)

        print(result)

        self.confirmation_label.configure(text="✔" if result == True else "✖")

    def close(self):
        close_connection(self.socket)
        self.Window.destroy()

    def remove_widgets(self, ofElement = None):
        for widget in ofElement.winfo_children():
            
            if widget.winfo_children() != ():
                for child in widget.winfo_children():
                    self.remove_widgets(child)
            widget.destroy()

def filter_messages(messages, buff, inbox, name = None):
    for widget in messages.winfo_children():
        widget.destroy()

    display_messages(messages, buff, inbox, name if name != "" else None)

def display_messages(messages, buff, inbox, name = None,):
    i = 0
    for msg in buff:
        if name == None or (inbox and msg.sender == name) or (not inbox and msg.receiver == name):

            frame = Frame(messages, bg=PANEL_COLOR, padx=10, pady=10)

            # preview = f'From: {msg.sender if inbox else msg.receiver} - {msg.content}'
            preview = f'From: {msg.sender}' if inbox else f'To: {msg.receiver}'
            preview += f' → {msg.content}'

            if len(preview) > 40:
                preview = preview[:40] + "..."

            message = Label(frame, text=preview, font="Helvetica 13", bg=PANEL_COLOR, fg=BUTTON_FG)
            message.place(relx = 0, rely = 0, relwidth=1, relheight=1)
            message.pack(side=LEFT, anchor="nw")

            btn = Button(frame, text="Open", font="Helvetica 13", bg=BUTTON_COLOR, fg=BUTTON_FG)
            btn.place(relx=0.75, rely=0.03, relwidth=0.20, relheight=0.90)
            btn.pack(side=RIGHT, anchor="nw")

            messages.create_window(0, i * 60, anchor='nw', window=frame, height=50, width=430)

            i += 1


# --------------------------------- MAIN --------------------------------- #

if __name__ == "__main__":
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 4000
    ADDR = (IP, PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    GUI(socket=client_socket).auth_window()