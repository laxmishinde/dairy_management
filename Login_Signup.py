import customtkinter
from tkinter import *
from tkinter import messagebox
import admindashboard
import pyrebase

# Firebase configuration (replace with your own config)
firebase_config = {
    "apiKey": "AIzaSyBZWTCV1XKmYhunKIPpF1aETQMLhqos5uI",
    "authDomain": "dairy-management-a2c9a.firebaseapp.com",
    "databaseURL": "https://dairy-management-a2c9a-default-rtdb.firebaseio.com",
    "projectId": "dairy-management-a2c9a",
    "storageBucket": "dairy-management-a2c9a.appspot.com",
    "messagingSenderId": "607780938700",
    "appId": "1:607780938700:web:ab295222771b79811c3369",
    "measurementId": "G-TMDPHL7CLS"
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


app = customtkinter.CTk()
app.title('Login and Signup')

# Calculate the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set the window size
window_width = 750
window_height = 540

# Calculate the position for the window to appear centered
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

app.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')
app.config(bg='#fff')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')
font5 = ('Helvetica', 28, 'bold')

def switch_to_signup():
    login_frame.place_forget()
    signup_frame.place(x=0, y=0)

def switch_to_login():
    signup_frame.place_forget()
    login_frame.place(x=0, y=0)

def signup():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    user_data = {
        "name": name,
        "email": email,
        "contact": contact,
        "username": username,
        "password": password
    }
    try:
        db.child("admins").push(user_data)
        messagebox.showinfo("Success", "Account created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def login():
    username = username_entry2.get()
    password = password_entry2.get()
    try:
        admins = db.child("admins").get()
        for admin_id, admin_data in admins.val().items():
            if admin_data["username"] == username and admin_data["password"] == password:
                messagebox.showinfo("Success", "Login successful!")
                app.destroy()  # Close the login/signup window
                admindashboard.show_admin_dashboard()  # Open the admin dashboard window
                return
        messagebox.showerror("Error", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def toggle_password_visibility_signup():
    if show_password_var.get():
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

def toggle_password_visibility_login():
    if show_password_var_login.get():
        password_entry2.configure(show="")
    else:
        password_entry2.configure(show="*")

###################################### Login Frame ##############################################

# Login Frame
login_frame = customtkinter.CTkFrame(app, bg_color='#fff', fg_color='#fff', width=840, height=660)
login_frame.place(x=0, y=0)

image1 = PhotoImage(file="logo.png")
image1_label = Label(login_frame, image=image1, bg='#fff', width=280, height=400)
image1_label.place(x=25, y=90)
login_frame.image1 = image1

login_label = customtkinter.CTkLabel(login_frame, font=font5, text='Admin Login', text_color='#4c87d9')
login_label.place(x=452, y=80)

# Enter username
username_entry2 = customtkinter.CTkEntry(login_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Enter Username', placeholder_text_color='#5e5e5e', width=330, height=50)
username_entry2.place(x=380, y=140)

# Enter password
password_entry2 = customtkinter.CTkEntry(login_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Enter Password', placeholder_text_color='#5e5e5e', width=330, height=50, show="*")
password_entry2.place(x=380, y=225)

# Checkbutton to show/hide password for login frame
show_password_var_login = BooleanVar()
show_password_checkbox_login = Checkbutton(login_frame, text="Show Password", variable=show_password_var_login, command=toggle_password_visibility_login, font=("Arial", 11))
show_password_checkbox_login.place(x=380, y=279)

# Login Button
login_button = customtkinter.CTkButton(login_frame, font=("Arial", 19), text_color='#000000', text='Login', fg_color='#1BAE4A', hover_color='#178D3D', bg_color='#fff', cursor='hand2', corner_radius=9, width=230, height=50, command=login)
login_button.place(x=439, y=342)

# Signup link
signup_label = customtkinter.CTkLabel(login_frame, font=font3, text='Dont have an account ? Sign up', text_color="#1373B3", bg_color='#fff', cursor='hand2')
signup_label.place(x=449, y=393)
signup_label.bind("<Button-1>", lambda event: switch_to_signup())

###################################### Signup Frame ##############################################

# Signup Frame
signup_frame = customtkinter.CTkFrame(app, bg_color='#fff', fg_color='#fff', width=840, height=660)
signup_frame.place_forget()

image1 = PhotoImage(file="logo.png")
image1_label = Label(signup_frame, image=image1, bg='#fff', width=280, height=400)
image1_label.place(x=25, y=90)
signup_frame.image1 = image1

signup_label = customtkinter.CTkLabel(signup_frame, font=('Helvetica', 22, 'bold'), text='Admin Sign up', text_color='#4c87d9')
signup_label.place(x=455, y=44)

# Name
name_entry = customtkinter.CTkEntry(signup_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Enter Full Name', placeholder_text_color='#5e5e5e', width=330, height=48)
name_entry.place(x=380, y=90)

# Email ID
email_entry = customtkinter.CTkEntry(signup_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Enter Email id', placeholder_text_color='#5e5e5e', width=330, height=48)
email_entry.place(x=380, y=154)

# Contact
contact_entry = customtkinter.CTkEntry(signup_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Enter Contact no.', placeholder_text_color='#5e5e5e', width=330, height=48)
contact_entry.place(x=380, y=219)

# Set username
username_entry = customtkinter.CTkEntry(signup_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Set Username', placeholder_text_color='#5e5e5e', width=330, height=48)
username_entry.place(x=380, y=282)

# Set password
password_entry = customtkinter.CTkEntry(signup_frame, font=font2, text_color='#000000', fg_color='#dce4e8', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Set Password', placeholder_text_color='#5e5e5e', width=330, height=48, show="*")
password_entry.place(x=380, y=348)

# Checkbutton to show/hide password for signup frame
show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(signup_frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility_signup, font=("Arial", 10))
show_password_checkbox.place(x=380, y=397)

# Signup Button
signup_button = customtkinter.CTkButton(signup_frame, font=("Arial", 17), text_color='#000000', text='Sign up', fg_color='#1BAE4A', hover_color='#178D3D', bg_color='#fff', cursor='hand2', corner_radius=9, width=230, height=47,command=signup)
signup_button.place(x=437, y=448)

# Login link
login_label = customtkinter.CTkLabel(signup_frame, font=font3, text='Already have an account? Login', text_color="#1373B3", bg_color='#fff', cursor='hand2')
login_label.place(x=439, y=500)
login_label.bind("<Button-1>", lambda event: switch_to_login())

app.mainloop()
