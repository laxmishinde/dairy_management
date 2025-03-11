import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import pyrebase
import datetime
from tkinter import messagebox
from tkinter import END, Scrollbar, Y, BOTH, WORD, DISABLED, scrolledtext
import datetime
from tkcalendar import DateEntry
from PIL import Image, ImageGrab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tempfile import NamedTemporaryFile
import os





def show_history():

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
    project_heading = ttk.Label(heading_frame, text="Vyaknteshwar Dairy Center", font=("Arial", 24), style="Heading.TLabel", padding=(47, 0))  # Added left and right padding
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
        import admindashboard
        admindashboard.show_admin_dashboard()

    #button1 = ctk.CTkButton(buttons_frame, font=("Arial", 16), text="back", fg_color="#777782", bg_color="lightgray", hover_color="#65656D", width=50, command=lambda: call_admindashboard())
    #button1.grid(row=0, column=0, padx=10, pady=10)

    
    # Create third horizontal frame below the buttons frame to cover the remaining space
    remaining_frame = ctk.CTkFrame(root, fg_color="#D2D2D2", bg_color="white", width=300, height=340)  # Adjusted height
    remaining_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(5, 2))

    def todays_records():
        for widget in remaining_frame.winfo_children():
            widget.destroy()
        current_date = datetime.date.today().strftime("%d-%m-%Y")
        # Create a Treeview widget
        treeview = ttk.Treeview(remaining_frame, columns=("Customer id", "Name", "Date", "Shift", "Category", "Quantity", "Price"), show="headings")

        # Define the column headings and center align the values
        treeview.heading("Customer id", text="Customer id", anchor="center")
        treeview.heading("Name", text="Name", anchor="center")
        treeview.heading("Date", text="Date", anchor="center")
        treeview.heading("Shift", text="Shift", anchor="center")
        treeview.heading("Category", text="Category", anchor="center")
        treeview.heading("Quantity", text="Quantity", anchor="center")
        treeview.heading("Price", text="Price", anchor="center")

        treeview.column("Customer id", width=120)
        treeview.column("Name", width=200)
        treeview.column("Date", width=100)
        treeview.column("Shift", width=100)
        treeview.column("Category", width=100)
        treeview.column("Quantity", width=100)
        treeview.column("Price", width=100)

        # Configure the style for the Treeview widget
        style.configure("Treeview.Heading", font=("Arial", 11), background="#C7CAF6")

        # Create vertical scrollbar
        vscrollbar = ttk.Scrollbar(remaining_frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=vscrollbar.set)
        vscrollbar.pack(side="right", fill="y")

        #Create horizontal scrollbar
        hscrollbar = ttk.Scrollbar(remaining_frame, orient="horizontal", command=treeview.xview)
        treeview.configure(xscrollcommand=hscrollbar.set)
        hscrollbar.pack(side="bottom", fill="x")

        # Get a snapshot of the 'records' node
        records_snapshot = db.child('records').get().val()

        # Check if the 'records' node exists
        if records_snapshot:
            for record_key, record_data in records_snapshot.items():
                customer_id = record_data.get("customer_id", None)
                name = record_data.get('name')
                date = record_data.get('date')
                shift = record_data.get('shift')
                category = record_data.get('category')
                quantity = record_data.get('quantity')
                price = record_data.get('total')

                if date == current_date:
                    # Insert the record into the Treeview widget with spaces before each value
                    treeview.insert("", "end", values=(" "*10 + customer_id, " "*20 + name, " "*6 + date, " "*8 + shift, " "*8 + category, " "*13 + quantity, " "*10 + price))
        else:
            messagebox.showinfo("error", "no records")

        # Pack the Treeview widget into the remaining_frame
        treeview.pack(side="top", fill="both", expand=True)

            


    def week_records():
        for widget in remaining_frame.winfo_children():
            widget.destroy()

        # Create first horizontal frame for project heading
        date_frame = ctk.CTkFrame(remaining_frame, width=window_width, height=window_height // 6, bg_color="lightgray", fg_color="lightgray")  # Reduced height
        date_frame.pack(side="top", fill="x", padx=10, pady=1)

        # Create labels for "From" and "To"
        from_label = ttk.Label(date_frame, text="From:", font=("Arial", 10), background="lightgray")
        from_label.grid(row=0, column=2, padx=(140, 5), pady=(10, 0), sticky="e")

        # Create DateEntry widgets for "From" and "To"
        from_date = DateEntry(date_frame, date_pattern="dd/MM/yyyy", font=("Arial", 10))
        from_date.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))

        to_label = ttk.Label(date_frame, text="To:", font=("Arial", 10), background="lightgray")
        to_label.grid(row=0, column=4, padx=(5, 5), pady=(10, 0), sticky="e")

        to_date = DateEntry(date_frame, date_pattern="dd/MM/yyyy", font=("Arial", 10))
        to_date.grid(row=0, column=5, padx=(0, 10), pady=(10, 0))

        # Create button to show records based on selected date range
        show_records_button = ctk.CTkButton(date_frame, text="Show Records", command=lambda: show_records(from_date.get_date(), to_date.get_date()), width=20)
        show_records_button.grid(row=0, column=6, padx=(40, 0), pady=(10, 0))

        # Function to show records based on selected date range
        def show_records(from_date, to_date):
            current_date = datetime.date.today().strftime("%d-%m-%Y")
            # Create a Treeview widget
            treeview = ttk.Treeview(remaining_frame, columns=("Customer id", "Name", "Date", "Shift", "Category", "Quantity", "Price"), show="headings")

            # Define the column headings and center align the values
            treeview.heading("Customer id", text="Customer id", anchor="center")
            treeview.heading("Name", text="Name", anchor="center")
            treeview.heading("Date", text="Date", anchor="center")
            treeview.heading("Shift", text="Shift", anchor="center")
            treeview.heading("Category", text="Category", anchor="center")
            treeview.heading("Quantity", text="Quantity", anchor="center")
            treeview.heading("Price", text="Price", anchor="center")

            treeview.column("Customer id", width=120)
            treeview.column("Name", width=200)
            treeview.column("Date", width=100)
            treeview.column("Shift", width=100)
            treeview.column("Category", width=100)
            treeview.column("Quantity", width=100)
            treeview.column("Price", width=100)

            # Configure the style for the Treeview widget
            style.configure("Treeview.Heading", font=("Arial", 11), background="#C7CAF6")

            # Create vertical scrollbar
            vscrollbar = ttk.Scrollbar(remaining_frame, orient="vertical", command=treeview.yview)
            treeview.configure(yscrollcommand=vscrollbar.set)
            vscrollbar.pack(side="right", fill="y")

            # Create horizontal scrollbar
            hscrollbar = ttk.Scrollbar(remaining_frame, orient="horizontal", command=treeview.xview)
            treeview.configure(xscrollcommand=hscrollbar.set)
            hscrollbar.pack(side="bottom", fill="x")

            # Get a snapshot of the 'records' node
            records_snapshot = db.child('records').get().val()

            # Check if the 'records' node exists
            if records_snapshot:
                for record_key, record_data in records_snapshot.items():
                    customer_id = record_data.get("customer_id", None)
                    name = record_data.get('name')
                    date = record_data.get('date')
                    shift = record_data.get('shift')
                    category = record_data.get('category')
                    quantity = record_data.get('quantity')
                    price = record_data.get('total')

                    if from_date <= datetime.datetime.strptime(date, '%d-%m-%Y').date() <= to_date:
                        # Insert the record into the Treeview widget with spaces before each value
                        treeview.insert("", "end", values=(" "*10 + customer_id, " "*20 + name, " "*6 + date, " "*8 + shift, " "*8 + category, " "*13 + quantity, " "*10 + price))
            else:
                messagebox.showinfo("error", "no records")

            # Pack the Treeview widget into the remaining_frame
            treeview.pack(side="top", fill="both", expand=True)




        



    # Create a Treeview widget
    treeview = ttk.Treeview(remaining_frame, columns=("Customer id", "Name", "Date", "Shift", "Category", "Quantity", "Price"), show="headings")

    # Define the column headings and center align the values
    treeview.heading("Customer id", text="Customer id", anchor="center")
    treeview.heading("Name", text="Name", anchor="center")
    treeview.heading("Date", text="Date", anchor="center")
    treeview.heading("Shift", text="Shift", anchor="center")
    treeview.heading("Category", text="Category", anchor="center")
    treeview.heading("Quantity", text="Quantity", anchor="center")
    treeview.heading("Price", text="Price", anchor="center")

    treeview.column("Customer id", width=120)
    treeview.column("Name", width=200)
    treeview.column("Date", width=100)
    treeview.column("Shift", width=100)
    treeview.column("Category", width=100)
    treeview.column("Quantity", width=100)
    treeview.column("Price", width=100)

    # Configure the style for the Treeview widget
    style.configure("Treeview.Heading", font=("Arial", 11))
    


    # Create vertical scrollbar
    vscrollbar = ttk.Scrollbar(remaining_frame, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=vscrollbar.set)
    vscrollbar.pack(side="right", fill="y")

   #Create horizontal scrollbar
    hscrollbar = ttk.Scrollbar(remaining_frame, orient="horizontal", command=treeview.xview)
    treeview.configure(xscrollcommand=hscrollbar.set)
    hscrollbar.pack(side="bottom", fill="x")

    # Get a snapshot of the 'records' node
    records_snapshot = db.child('records').get().val()

    # Check if the 'records' node exists
    if records_snapshot:
        for record_key, record_data in records_snapshot.items():
            customer_id = record_data.get("customer_id", None)
            name = record_data.get('name')
            date = record_data.get('date')
            shift = record_data.get('shift')
            category = record_data.get('category')
            quantity = record_data.get('quantity')
            price = record_data.get('total')

            # Insert the record into the Treeview widget with spaces before each value
            treeview.insert("", "end", values=(" "*10 + customer_id, " "*20 + name, " "*6 + date, " "*8 + shift, " "*8 + category, " "*13 + quantity, " "*10 + price))
    else:
        messagebox.showinfo("error", "no records")

    # Pack the Treeview widget into the remaining_frame
    treeview.pack(side="top", fill="both", expand=True)

    button2 = ctk.CTkButton(buttons_frame, text="Today History", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=lambda: todays_records())  # Adjusted width and height
    button2.grid(row=0, column=1, padx=(100, 10), pady=(10, 10))  # Adjusted padding between buttons

    button3 = ctk.CTkButton(buttons_frame, text="Week History", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#D2D2D2", corner_radius=9, width=161, height=30, font=("Arial", 15), command=lambda: week_records())  # Adjusted width and height
    button3.grid(row=0, column=2, padx=(100, 10), pady=(10, 10))  # Adjusted padding between buttons

    

    frame = ctk.CTkFrame(remaining_frame)

    # Create a frame for the form
    btn_frame = ctk.CTkFrame(root, bg_color="#fff", fg_color="#fff", width=window_width, height=30, border_color='#fff', border_width=1)
    btn_frame.pack(side="bottom", fill="both", padx=10, pady=(2,1), expand=False) 

    def print_main_frame():
        # Take a screenshot of the main frame
        x, y, width, height = remaining_frame.winfo_rootx(), remaining_frame.winfo_rooty(), remaining_frame.winfo_width(), \
                              remaining_frame.winfo_height()
        screenshot = ImageGrab.grab((x, y, x + width, y + height))

         # Define the path to the folder where you want to save the file
        folder_path = "history_images"

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Construct the full path for the temporary image file
        temp_image_path = os.path.join(folder_path, "temp.png")


        # Add the screenshot to the PDF
        screenshot.save(temp_image_path)

        # Print the PDF
        os.startfile(temp_image_path, "print")


    
    # Add the buttons
    back_button = ctk.CTkButton(btn_frame, font=("Arial", 14), text="Back", bg_color="#fff", hover_color="#12580A", fg_color="#187A0D", width=100, command=lambda: call_admindashboard())
    back_button.grid(row=0, column=0, padx=(510,10), pady=(1,1), sticky="e")

    print_button = ctk.CTkButton(btn_frame, font=("Arial", 14), text="Print", bg_color="#fff", hover_color="#12580A", fg_color="#187A0D", width=100, command=print_main_frame)
    print_button.grid(row=0, column=1, padx=(10,1), pady=(1,1), sticky="e")


    
    


    # Run the application
    root.mainloop()

#show_history()
