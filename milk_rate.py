import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import admindashboard
import pyrebase
from tkinter import messagebox
import view


def milk_price():

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
    
    # Create main window
    root = ctk.CTk()
    root.title("Admin Dashboard")


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

    # Create a frame for the Admin Dashboard label
    admin_frame = ctk.CTkFrame(root, fg_color="lightgray")
    admin_frame.pack(side="top", fill="x", padx=10, pady=(0, 5))  
    def call_admindashboard():
        root.destroy()
        admindashboard.show_admin_dashboard()

    back_button = ctk.CTkButton(admin_frame, font=("Arial", 16), text="back", fg_color="#777782", bg_color="lightgray", hover_color="#65656D", width=50, command=lambda: call_admindashboard())
    back_button.pack(side="left", padx=10, pady=10)

    # Add label for Admin Dashboard with left alignment
    admin_dashboard_label = ttk.Label(admin_frame, text="Set The Milk Rate", font=("Arial", 16), background='lightgray')
    admin_dashboard_label.pack(side="left", padx=230, pady=10)  # Align to the left

    def add_data():
        # Get the values entered by the user
        animal = animal_entry.get()
        fat = fat_entry.get()
        snf = snf_entry.get()
        price = price_entry.get()

        # Create a dictionary to store the data
        data = {
            'fat': fat,
            'snf': snf,
            'price': price
        }

        # Push the data under the appropriate child node
        db.child('milk').child(animal).push(data)
        messagebox.showinfo("Success", "Milk price has been added successfully.")

    def delete_data():
        # Retrieve the values for fat, snf, and price from the entry widgets
        animal = animal_entry.get()
        fat = fat_entry.get()
        snf = snf_entry.get()
        price = price_entry.get()

        try:
            # Get a snapshot of all records under the specified animal node
            records_snapshot = db.child('milk').child(animal).get()

            # Loop through each record in the snapshot
            for record in records_snapshot.each():
                # Get the values of fat, snf, and price for the current record
                current_fat = record.val().get('fat')
                current_snf = record.val().get('snf')
                current_price = record.val().get('price')

                # Check if the current record matches the specified values
                if current_fat == fat and current_snf == snf and current_price == price:
                    # Remove the current record from the database
                    db.child('milk').child(animal).child(record.key()).remove()
                    messagebox.showinfo("Success", "Record deleted successfully!")
                    return

            messagebox.showinfo("Error", "Record not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_data():
        # Retrieve the values for fat, snf, price, and animal from the entry widgets
        fat = fat_entry.get()
        snf = snf_entry.get()
        price = price_entry.get()
        animal = animal_entry.get()

        # Specify the path to the record you want to update (e.g., 'cow' node)
        #animal = 'cow'

        try:
            # Get a snapshot of all records under the specified animal node
            records_snapshot = db.child('milk').child(animal).get()

            # Loop through each record in the snapshot
            for record in records_snapshot.each():
                # Get the values of fat, snf, and price for the current record
                current_fat = record.val().get('fat')
                current_snf = record.val().get('snf')

                # Check if the current record matches the specified values
                if current_fat == fat and current_snf == snf:
                    # Update the price for the current record
                    db.child('milk').child(animal).child(record.key()).update({"price": price})
                    messagebox.showinfo("Success", "Price updated successfully!")
                    return

            messagebox.showinfo("Error", "Record not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_data():
            animal_entry.delete(0, "end")
            fat_entry.delete(0, "end")
            snf_entry.delete(0, "end")
            price_entry.delete(0, "end")

    def pass_data():
        animal = animal_entry.get()
        root.destroy()
        view.view_data(animal)
            


    # Create second horizontal frame for cards
    cards_frame = ctk.CTkFrame(root, fg_color="#D2D2D2")  # Adjusted height
    cards_frame.pack(side="top", fill="both", expand=False, padx=10, pady=(5, 0))  # Reduced top padding

    #first row
    animal_label = ttk.Label(cards_frame, text="Animal:", font=("Arial", 14), background="#D2D2D2")
    animal_label.grid(row=0, column=0, padx=(20,5), pady=(50,10))

    animal_entry = ctk.CTkEntry(cards_frame, font=("Arial", 16), width=150)
    animal_entry.grid(row=0, column=1, padx=10, pady=(50,10))

    #second row
    fat_label = ttk.Label(cards_frame, text="FAT:", font=("Arial", 14), background="#D2D2D2")
    fat_label.grid(row=1, column=0, padx=(20,5), pady=(20,30))

    fat_entry = ctk.CTkEntry(cards_frame, font=("Arial", 16), width=150)
    fat_entry.grid(row=1, column=1, padx=10, pady=(20,30))

    snf_label = ttk.Label(cards_frame, text="SNF:", font=("Arial", 14), background="#D2D2D2")
    snf_label.grid(row=1, column=2, padx=(5,5), pady=(20,30))

    snf_entry = ctk.CTkEntry(cards_frame, font=("Arial", 16), width=150)
    snf_entry.grid(row=1, column=3, padx=5, pady=(20,30))

    price_label = ttk.Label(cards_frame, text="Price:", font=("Arial", 14), background="#D2D2D2")
    price_label.grid(row=1, column=4, padx=(5,5), pady=(20,30))

    price_entry = ctk.CTkEntry(cards_frame, font=("Arial", 16), width=150)
    price_entry.grid(row=1, column=5, padx=5, pady=(20,30))

    # Create second horizontal frame for cards
    buttons_frame = ctk.CTkFrame(root, fg_color="#D2D2D2",bg_color="#D2D2D2", height=110)  # Adjusted height
    buttons_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(0, 5))  # Reduced top padding

    #third row
    add_button = ctk.CTkButton(buttons_frame, font=("Arial", 14), text="Add", fg_color="#191D65", hover_color="#1b2fa1", bg_color="#D2D2D2", width=90, command=lambda: add_data())
    add_button.grid(row=2, column=0, padx=(70,4), pady=(50,10))

    delete_button = ctk.CTkButton(buttons_frame, font=("Arial", 14), text="Delete", fg_color="#191D65", hover_color="#1b2fa1", bg_color="#D2D2D2", width=90, command=lambda: delete_data())
    delete_button.grid(row=2, column=1, padx=(30,4), pady=(50,10))

    update_button = ctk.CTkButton(buttons_frame, font=("Arial", 14), text="Update", fg_color="#191D65", hover_color="#1b2fa1", bg_color="#D2D2D2", width=90, command=lambda: update_data())
    update_button.grid(row=2, column=2, padx=(30,4), pady=(50,10))

    clear_button = ctk.CTkButton(buttons_frame, font=("Arial", 14), text="Clear", fg_color="#191D65", hover_color="#1b2fa1", bg_color="#D2D2D2", width=90, command=lambda: clear_data())
    clear_button.grid(row=2, column=3, padx=(30,4), pady=(50,10))

    View_button = ctk.CTkButton(buttons_frame, font=("Arial", 14), text="View", fg_color="#191D65", hover_color="#1b2fa1", bg_color="#D2D2D2", width=90, command=lambda: pass_data())
    View_button.grid(row=2, column=4, padx=(30,4), pady=(50,10))
    
    # Run the application
    root.mainloop()

#milk_price()
