import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import pyrebase
from tkinter import messagebox
import milk_rate



def view_data(animal):

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

    #def view_chart():


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
    project_heading = ttk.Label(heading_frame, text="Vyankateshwar Dairy Center", font=("Arial", 24), style="Heading.TLabel", padding=(47, 0))  # Added left and right padding
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
    admin_frame.pack(side="top", fill="x", padx=10, pady=(0, 5))  # Reduced bottom padding

    def call_milk_rate():
        root.destroy()
        milk_rate.milk_price()

    back_button = ctk.CTkButton(admin_frame, font=("Arial", 16), text="back", fg_color="#777782", bg_color="lightgray", hover_color="#65656D", width=50, command=lambda: call_milk_rate())
    back_button.pack(side="left", padx=10, pady=10)

    # Add label for Admin Dashboard with left alignment
    admin_dashboard_label = ttk.Label(admin_frame, text=f"{animal} milk rate chart", font=("Arial", 12), background='lightgray')
    admin_dashboard_label.pack(side="left", padx=(230,0), pady=10)  # Align to the left


    
    # Create second horizontal frame for cards
    cards_frame = ctk.CTkFrame(root, fg_color="#D2D2D2")  # Adjusted height
    cards_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(5, 0))  # Reduced top padding

    # Create a Treeview widget
    treeview = ttk.Treeview(cards_frame, columns=("Fat", "SNF", "Price"), show="headings")

    # Define the column headings and center align the values
    treeview.heading("Fat", text="Fat", anchor="center")
    treeview.heading("SNF", text="SNF", anchor="center")
    treeview.heading("Price", text="Price", anchor="center")

    # Configure the style for the Treeview widget
    style.configure("Treeview.Heading", font=("Arial", 12), background="#C7CAF6")


    # Create vertical scrollbar
    vscrollbar = ttk.Scrollbar(cards_frame, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=vscrollbar.set)
    vscrollbar.pack(side="right", fill="y")

    # Create horizontal scrollbar
    hscrollbar = ttk.Scrollbar(cards_frame, orient="horizontal", command=treeview.xview)
    treeview.configure(xscrollcommand=hscrollbar.set)
    hscrollbar.pack(side="bottom", fill="x")

    # Get a snapshot of all records under the specified animal node
    records_snapshot = db.child('milk').child(animal).get()

    # Loop through each record in the snapshot
    for record in records_snapshot.each():
        # Get the values of fat, snf, and price for the current record
        fat = record.val().get('fat')
        snf = record.val().get('snf')
        price = record.val().get('price')

        # Insert the record into the Treeview widget with spaces before each value
        treeview.insert("", "end", values=(" "*36 + fat, " "*36 + snf, " "*33 + price))

         
   


    # Pack the Treeview widget into the cards_frame
    treeview.pack(side="top", fill="both", expand=True)




    # Run the application
    root.mainloop()

#view_data(animal)
