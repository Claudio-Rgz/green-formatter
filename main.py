import os
from PIL import ImageTk
import customtkinter
from functions import uppercase, lowercase, remove_spaces

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window

root.geometry("400x240")
root.title('Green Formatter')
root.iconpath = ImageTk.PhotoImage(file=os.path.join("assets/green-formatter-icon.jpg"))
root.wm_iconbitmap()
root.iconphoto(False, root.iconpath)


def button1():  # First button that includes the uppercase function
    cliptext = root.clipboard_get()
    formatted_text = uppercase(cliptext)
    root.clipboard_clear()
    root.clipboard_append(string=formatted_text)


# Use CTkButton instead of tkinter Button
button_1 = customtkinter.CTkButton(master=root,
                                   text="Uppercase",
                                   command=button1,
                                   fg_color='#225B13',
                                   hover_color='#193C0A')

button_1.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)


def button2():  # Second button that includes the lowercase function
    cliptext = root.clipboard_get()
    formatted_text = lowercase(cliptext)
    root.clipboard_clear()
    root.clipboard_append(string=formatted_text)


button_2 = customtkinter.CTkButton(master=root,
                                   text="Lowercase",
                                   command=button2,
                                   fg_color='#225B13',
                                   hover_color='#193C0A')
button_2.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)


def button3():  # Third button that includes the remove_space function
    cliptext = root.clipboard_get()
    formatted_text = remove_spaces(cliptext)
    root.clipboard_clear()
    root.clipboard_append(string=formatted_text)


button_3 = customtkinter.CTkButton(master=root,
                                   text="Remove Spaces",
                                   command=button3,
                                   fg_color='#225B13',
                                   hover_color='#193C0A')
button_3.place(relx=0.5, rely=0.60, anchor=customtkinter.CENTER)

root.mainloop()
input()
