from password_generator import generate_password
from tkinter import *
from tkinter import messagebox



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = user_email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        web_warning = messagebox.showwarning(title="Website is blank", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                              f" Password: {password} \n "f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# logo arrangement
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website: ", font="bold")
web_label.grid(column=0, row=1)

user_email_label = Label(text="Email/Username: ", font="bold")
user_email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font="bold")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

user_email_entry = Entry(width=35)
user_email_entry.grid(column=1, row=2, columnspan=2)
user_email_entry.insert(0, "youremail@email.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons

password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
