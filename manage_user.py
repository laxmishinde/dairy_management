import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import pyrebase
import random
import string
import admindashboard
from tkinter import messagebox
from tkinter import END, Scrollbar, Y, BOTH, WORD, DISABLED, scrolledtext





def show_manage_user():

    # Firebase configuration
    config = {
        "apiKey": "AIzaSyBZWTCV1XKmYhunKIPpF1aETQMLhqos5uI",
        "authDomain": "dairy-management-a2c9a.firebaseapp.com",
        "databaseURL": "https://dairy-management-a2c9a-default-rtdb.firebaseio.com",
        "projectId": "dairy-management-a2c9a",
        "storageBucket": "dairy-management-a2c9a.appspot.com",
        "messagingSenderId": "607780938700",
        "appId": "1:607780938700:web:ab295222771b79811c3369",
        "measurementId": "G-TMDPHL7CLS"

    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()


    root = ctk.CTk()
    root.title("Manage Users")

    # Set window dimensions
    window_width = 750
    window_height = 540

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate window position to center it on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set window geometry
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set minimum and maximum size for the window
    root.minsize(window_width, window_height)
    root.maxsize(window_width, window_height)



    # Create first horizontal frame for project heading
    heading_frame = ctk.CTkFrame(root, width=window_width, height=window_height // 5, bg_color="#39ACF8", fg_color="#39ACF8")  # Reduced height
    heading_frame.pack(side="top", fill="x", padx=10, pady=10)

    # Load left image and resize
    left_image_path = "left1.png"
    left_image = Image.open(left_image_path)
    left_image = left_image.resize((99, 99), Image.LANCZOS)  # Adjusted size
    left_image = ImageTk.PhotoImage(left_image)

    # Add left image
    left_label = ttk.Label(heading_frame, image=left_image, background="#39ACF8")
    left_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Align to extreme left

    # Create a ttk style
    style = ttk.Style(root)

    # Set the background color for the label
    style.configure("Heading.TLabel", background="#39ACF8")  # You can change "lightblue" to any color you want

    # Add label for project heading with left and right padding
    project_heading = ttk.Label(heading_frame, text="Vyakteshwar Dairy Center", font=("Arial", 24), style="Heading.TLabel", padding=(47, 0))  # Added left and right padding
    project_heading.grid(row=0, column=1, padx=10, pady=10)  # Centered

    # Load right image and resize
    right_image_path = "right4.png"
    right_image = Image.open(right_image_path)
    right_image = right_image.resize((90, 95), Image.LANCZOS)  # Adjusted size
    right_image = ImageTk.PhotoImage(right_image)

    # Add right image
    right_label = ttk.Label(heading_frame, image=right_image, background="#39ACF8")
    right_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")  # Align to extreme right

    # Create second horizontal frame for buttons
    buttons_frame = ctk.CTkFrame(root, fg_color="#D2D2D2", height=window_height // 6) # Adjusted height
    buttons_frame.pack(side="top", fill="x", padx=10, pady=(2, 0))  # Reduced top padding

    def call_admindashboard():
            root.destroy()
            admindashboard.show_admin_dashboard()


    def add():
        def generate_id():
            random_id = ''.join(random.choices(string.digits, k=6))
            id_entry.delete(0, "end")
            id_entry.insert(0, random_id)

        def save_data(name, email, contact, address, id):
            data = {
                "name": name,
                "email": email,
                "contact": contact,
                "address": address,
                "id": id
            }
            db.child("users").push(data)
            messagebox.showinfo("Success", "User has been added successfully.")

        def clear_form():
            name_entry.delete(0, "end")
            email_entry.delete(0, "end")
            contact_entry.delete(0, "end")
            address_entry.delete(0, "end")
            id_entry.delete(0, "end")

        for widget in remaining_frame.winfo_children():
            widget.destroy()

        # Create a frame for the form
        frame1 = ctk.CTkFrame(remaining_frame, fg_color="#E3DBB7", width=400, height=200)
        frame1.pack(side="top", fill="both", expand=True)
        # Labels
        name_label = ttk.Label(frame1, text="Name:", font=("Arial", 14), background="#E3DBB7")
        email_label = ttk.Label(frame1, text="Email:", font=("Arial", 14), background="#E3DBB7")
        email_label = ttk.Label(frame1, text="Email:", font=("Arial", 14), background="#E3DBB7")
        contact_label = ttk.Label(frame1, text="Contact:", font=("Arial", 14), background="#E3DBB7")
        address_label = ttk.Label(frame1, text="Address:", font=("Arial", 14), background="#E3DBB7")
        id_label = ttk.Label(frame1, text="ID:", font=("Arial", 14), background="#E3DBB7")

        name_label.grid(row=0, column=0, padx=(200,5), pady=10)
        email_label.grid(row=1, column=0, padx=(200,5), pady=10)
        contact_label.grid(row=2, column=0, padx=(200,5), pady=10)
        address_label.grid(row=3, column=0, padx=(200,5), pady=10)
        id_label.grid(row=4, column=0, padx=(200,2), pady=10)

        # Entry fields
        name_entry = ctk.CTkEntry(frame1, font=("Arial", 14), width=270)
        email_entry = ctk.CTkEntry(frame1, font=("Arial", 14), width=270)
        contact_entry = ctk.CTkEntry(frame1, font=("Arial", 14), width=270)
        address_entry = ctk.CTkEntry(frame1, font=("Arial", 14), width=270)
        id_entry = ctk.CTkEntry(frame1, font=("Arial", 14), width=220)

        name_entry.grid(row=0, column=1, padx=10, pady=10)
        email_entry.grid(row=1, column=1, padx=10, pady=10)
        contact_entry.grid(row=2, column=1, padx=10, pady=10)
        address_entry.grid(row=3, column=1, padx=10, pady=10)
        id_entry.grid(row=4, column=1, padx=(0,10), pady=10)

        # Generate ID button
        generate_id_button = ctk.CTkButton(frame1, font=("Arial", 12), fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", text="Generate", command=generate_id, width=50)
        generate_id_button.grid(row=4, column=2, padx=(10,30), pady=10)

        

        back_button = ctk.CTkButton(frame1, font=("Arial", 16), text="back", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", width=120, command=lambda: call_admindashboard())
        back_button.grid(row=5, column=0, padx=(150,4), pady=(30,10))

        # Save and clear buttons
        save_button = ctk.CTkButton(frame1, font=("Arial", 14), text="Save", bg_color="#E3DBB7", hover_color="#12580A", fg_color="#187A0D", command=lambda: save_data(name_entry.get(), email_entry.get(), contact_entry.get(), address_entry.get(), id_entry.get()), width=120)
        clear_button = ctk.CTkButton(frame1, font=("Arial", 14), text="Clear", bg_color="#E3DBB7", fg_color="#BB0707", hover_color="#AA0000", command=clear_form, width=120)

        save_button.grid(row=5, column=1, padx=(1,4), pady=(30,10))
        clear_button.grid(row=5, column=2, padx=(1,4), pady=(30,10))

        

        
    def delete():
        for widget in remaining_frame.winfo_children():
            widget.destroy()

        # Create a frame for the form
        frame2 = ctk.CTkFrame(remaining_frame, fg_color="#E3DBB7", width=400, height=200)
        frame2.pack(side="top", fill="both", expand=True)

        # Label for ID
        id_label = ttk.Label(frame2, text="Enter ID:", font=("Arial", 14), background="#E3DBB7")
        id_label.grid(row=0, column=0, padx=(130, 2), pady=20)

        # Entry for ID
        id_entry = ctk.CTkEntry(frame2, font=("Arial", 14), width=250)
        id_entry.grid(row=0, column=1, padx=(0, 10), pady=(10,5))
        
        fetched_user_info_text = scrolledtext.ScrolledText(frame2, width=40, height=10, font=("Arial", 12))
        fetched_user_info_text.grid(row=1, column=0, columnspan=2, padx=(170,10), pady=(2,30))


        def fetch_user_info(event=None):
            # Get the user ID from the entry box
            user_id = id_entry.get()

            # Check if the user ID is not empty
            if user_id:
                # Try to fetch the user data from Firebase
                try:
                    # Find the user data by ID
                    users = db.child("users").get().val()
                    if users:
                        for key, value in users.items():
                            if value["id"] == user_id:
                                fetched_user_info = f"\tName:       {value.get('name', '')}\n\n"
                                fetched_user_info += f"\tID:              {value.get('id', '')}\n\n"
                                fetched_user_info += f"\tEmail:        {value.get('email', '')}\n\n"
                                fetched_user_info += f"\tContact:    {value.get('contact', '')}\n\n"
                                fetched_user_info += f"\tAddress:   {value.get('address', '')}\n\n"

                                fetched_user_info_text.delete(1.0, END)  # Delete all the text in the widget
                                fetched_user_info_text.insert(END, fetched_user_info)
                                break
                        else:
                            fetched_user_info_text.delete(1.0, END)
                            fetched_user_info_text.insert(END, f"No user found with ID {user_id}")
                    else:
                        fetched_user_info_text.delete(1.0, END)
                        fetched_user_info_text.insert(END, "No users found in the database.")
                except Exception as e:
                    fetched_user_info_text.delete(1.0, END)
                    fetched_user_info_text.insert(END, "An error occurred while fetching user data.")
            else:
                fetched_user_info_text.delete(1.0, END)
                fetched_user_info_text.insert(END, "Please enter a user ID.")

        id_entry.bind('<KeyRelease>', fetch_user_info)

        def delete_user_data():
            user_id = id_entry.get()

                # Check if the user ID is not empty
            if user_id:
                # Try to delete the user data from Firebase
                try:
                    # Find the user data by ID and delete it from the database
                    users = db.child("users").get().val()
                    if users:
                        for key, value in users.items():
                            if value["id"] == user_id:
                                db.child("users").child(key).remove()
                                messagebox.showinfo("Success", "User has been deleted successfully.")
                                break
                        else:
                            messagebox.showinfo("Error", "User with no such id not found in the database.")

                    else:
                        messagebox.showinfo("Error", "No user found id database.")

                except Exception as e:
                    messagebox.showinfo("Error", "An error occurred while deleting user data:",e)
            else:
                messagebox.showinfo("Warning", "Please enter a user id to delete.")

        back_button = ctk.CTkButton(frame2, font=("Arial", 16), text="back", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", width=120, command=lambda: call_admindashboard())
        back_button.grid(row=1, column=0, padx=(180,4), pady=(220,10))

        # Delete button
        delete_button = ctk.CTkButton(frame2, font=("Arial", 15), text="Delete", bg_color="#E3DBB7", fg_color="#BB0707", hover_color="#AA0000", command=delete_user_data, width=120)
        delete_button.grid(row=1, column=1, columnspan=2, padx=(80, 4), pady=(220, 10))



       
    def update():
        for widget in remaining_frame.winfo_children():
            widget.destroy()

        def clear_form():
            id_entry.delete(0, "end")
            key_entry.delete(0, "end")
            new_value_entry.delete(0, "end")
            
        # Create a frame for the form
        frame3 = ctk.CTkFrame(remaining_frame, fg_color="#E3DBB7", width=400, height=200)
        frame3.pack(side="top", fill="both", expand=True)

        # Label for ID
        id_label = ttk.Label(frame3, text="User ID:", font=("Arial", 14), background="#E3DBB7")
        id_label.grid(row=0, column=0, padx=(200, 2), pady=(60,10))

        # Entry for ID
        id_entry = ctk.CTkEntry(frame3, font=("Arial", 14), width=220)
        id_entry.grid(row=0, column=1, padx=(10, 10), pady=(60,10))

        # Label for key
        key_label = ttk.Label(frame3, text="Attribute:", font=("Arial", 14), background="#E3DBB7")
        key_label.grid(row=1, column=0, padx=(200, 2), pady=10)

        # Entry for key
        key_entry = ctk.CTkEntry(frame3, font=("Arial", 14), width=220)
        key_entry.grid(row=1, column=1, padx=(10, 10), pady=10)

        # Label for new value
        new_value_label = ttk.Label(frame3, text="New Value:", font=("Arial", 14), background="#E3DBB7")
        new_value_label.grid(row=2, column=0, padx=(200, 2), pady=10)

        # Entry for new value
        new_value_entry = ctk.CTkEntry(frame3, font=("Arial", 14), width=220)
        new_value_entry.grid(row=2, column=1, padx=(10, 10), pady=10)

        back_button = ctk.CTkButton(frame3, font=("Arial", 16), text="back", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", width=90, command=lambda: call_admindashboard())
        back_button.grid(row=3, column=0, padx=(180,0), pady=(40,10))


        # Update button
        update_button = ctk.CTkButton(frame3, font=("Arial", 14), bg_color="#E3DBB7", hover_color="#12580A", fg_color="#187A0D", text="Update", width=90)
        update_button.grid(row=3, column=1, columnspan=2, padx=(5, 130), pady=(40, 10))

        # Update button
        clear_button = ctk.CTkButton(frame3, font=("Arial", 14),  bg_color="#E3DBB7", fg_color="#BB0707", hover_color="#AA0000", text="Clear", width=90, command=clear_form)
        clear_button.grid(row=3, column=1, columnspan=2, padx=(120, 0), pady=(40, 10))


        def update_user_data():
            user_id = id_entry.get()
            key = key_entry.get()
            new_value = new_value_entry.get()

            # Check if the user ID, key, and new value are not empty
            if user_id and key and new_value:
                # Try to update the user data in Firebase
                try:
                    # Find the user data by ID
                    users = db.child("users").get().val()
                    if users:
                        for user_key, user_value in users.items():
                            if user_value["id"] == user_id:
                                # Update the value of the specified key
                                db.child("users").child(user_key).update({key: new_value})
                                messagebox.showinfo("Success", "User data updated successfully!")
                                break
                        else:
                            messagebox.showinfo("Error", "User with no such id found in the database.")
                    else:
                        messagebox.showinfo("Error", "User not found.")
                except Exception as e:
                    messagebox.showinfo("Error", "An error occurred while updating user data")
            else:
                messagebox.showinfo("Warning", "Fill all the details.")

        # Bind update_user_data to the command of update_button
        update_button.configure(command=update_user_data)

    def view():
        for widget in remaining_frame.winfo_children():
            widget.destroy()
            
        frame4 = ctk.CTkFrame(remaining_frame, fg_color="#E3DBB7", width=400, height=200)
        frame4.pack(side="top", fill="both", expand=True)

        scrollbar = Scrollbar(frame4)
        scrollbar.pack(side="right", fill=Y)

        user_text = scrolledtext.ScrolledText(frame4, wrap=WORD, bg="#E3DBB7", yscrollcommand=scrollbar.set, font=("Arial", 12), width=60, height=20)
        user_text.pack(side="left", fill=BOTH, expand=True)
        scrollbar.config(command=user_text.yview)

        try:
            users = db.child("users").get().val()
            if users:
                sorted_users = sorted(users.values(), key=lambda x: x['name'], reverse=True)
                for user in sorted_users:
                    user_info = f"\n Name:       {user.get('name', '')}\n\n"
                    user_info += f"ID:              {user.get('id', '')}\n\n"
                    user_info += f"Email:        {user.get('email', '')}\n\n"
                    user_info += f"Contact:    {user.get('contact', '')}\n\n"
                    user_info += f"Address:   {user.get('address', '')}\n\n"
                    user_info += f"--------------------------------------------------------------------------------------------------------------------------\n"

                    # Insert the user information into the text widget
                    user_text.insert(END, user_info)

                # Tag the attribute names with a blue color
                user_text.tag_configure("black", foreground="black")
                user_text.tag_add("black", "2.0", "end-1c")  # Tag the entire content as blue
            else:
                user_text.insert(END, "No users found in the database.")
        except Exception as e:
            user_text.insert(END, f"An error occurred while fetching user data: {e}")

        user_text.config(state=DISABLED, padx=28, pady=10)




    # Create four buttons and place them in the horizontal frame
    button1 = ctk.CTkButton(buttons_frame, text="Add user", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=add)  # Adjusted width and height
    button1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))  # Adjusted padding between buttons

    button2 = ctk.CTkButton(buttons_frame, text="Delete user", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=delete)  # Adjusted width and height
    button2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))  # Adjusted padding between buttons

    button3 = ctk.CTkButton(buttons_frame, text="Update user", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=update)  # Adjusted width and height
    button3.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))  # Adjusted padding between buttons

    button4 = ctk.CTkButton(buttons_frame, text="View user", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=view)  # Adjusted width and height
    button4.grid(row=0, column=3, padx=(10, 10), pady=(10, 10))  # Adjusted padding between buttons

     # Create third horizontal frame below the buttons frame to cover the remaining space
    remaining_frame = ctk.CTkFrame(root, fg_color="#D2D2D2", bg_color="white", width=300, height=340)  # Adjusted height
    remaining_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(5, 2))

    frame = ctk.CTkFrame(remaining_frame)

    
    


    # Run the application
    root.mainloop()

# Uncomment the line below to test the function independently
#show_manage_user()
