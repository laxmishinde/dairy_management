import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import admindashboard, view_bill
import pyrebase
from tkinter import messagebox, END
import datetime, view_bill


def bill():

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
    admin_frame.pack(side="top", fill="x", padx=10, pady=(0, 5))  
    def call_admindashboard():
        root.destroy()
        admindashboard.show_admin_dashboard()

    back_button = ctk.CTkButton(admin_frame, font=("Arial", 16), text="back", fg_color="#777782", bg_color="lightgray", hover_color="#65656D", width=50, command=lambda: call_admindashboard())
    back_button.pack(side="left", padx=10, pady=10)

    # Add label for Admin Dashboard with left alignment
    admin_dashboard_label = ttk.Label(admin_frame, text="Bill Generation", font=("Arial", 16), background='lightgray')
    admin_dashboard_label.pack(side="left", padx=230, pady=10)  # Align to the left

    form1_frame = ctk.CTkFrame(root, fg_color="lightgray")
    form1_frame.pack(side="top", fill="x", padx=10, pady=(0, 2))

    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    # Add label and entry for Date
    date_label = ttk.Label(form1_frame, text="Date:", font=("Arial", 14), background='lightgray')
    date_label.grid(row=0, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    date_entry = ctk.CTkEntry(form1_frame, font=("Arial", 14))
    date_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")  # Align to the right

    date_entry.insert(0, current_date)

    # Add label and entry for Shift
    shift_label = ttk.Label(form1_frame, text="Shift:", font=("Arial", 14), background='lightgray')
    shift_label.grid(row=0, column=2, padx=(90,10), pady=10, sticky="w")  # Align to the left

    shift_entry = ctk.CTkEntry(form1_frame, font=("Arial", 14))
    shift_entry.grid(row=0, column=3, padx=10, pady=10, sticky="e")  # Align to the right

    # Add label and entry for Category
    animal_label = ttk.Label(form1_frame, text="Category:", font=("Arial", 14), background='lightgray')
    animal_label.grid(row=1, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    animal_entry = ctk.CTkEntry(form1_frame, font=("Arial", 14))
    animal_entry.grid(row=1, column=1, padx=10, pady=8, sticky="e")  # Align to the right


    form2_frame = ctk.CTkFrame(root, fg_color="lightgray")
    form2_frame.pack(side="top", fill="x", padx=10, pady=(0, 2))

     # Add label and entry for Customer ID
    customer_id_label = ttk.Label(form2_frame, text="Customer ID:", font=("Arial", 14), background='lightgray')
    customer_id_label.grid(row=0, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    customer_id_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")  # Align to the right
    

    # Add label and entry for Name
    name_label = ttk.Label(form2_frame, text="Name:", font=("Arial", 14), background='lightgray')
    name_label.grid(row=0, column=2, padx=(30,5), pady=10, sticky="w")  # Align to the left

    name_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14), width=220)
    name_entry.grid(row=0, column=3, padx=(4,40), pady=10, sticky="e")  # Align to the right

    def fetch_customer_name(event=None):
        # Get the user ID from the entry box
        user_id = customer_id_entry.get()

        # Check if the user ID is not empty
        if user_id:
            # Try to fetch the user data from Firebase
            try:
                # Find the user data by ID
                users = db.child("users").get().val()
                if users:
                    for key, value in users.items():
                        if value["id"] == user_id:
                            fetched_customer_name = f"{value.get('name', '')}"

                            name_entry.delete(0, END)  # Delete all the text in the widget
                            name_entry.insert(END, fetched_customer_name)
                            break
                    else:
                        name_entry.delete(0, END)
                        name_entry.insert(END, f"No user found with ID {user_id}")
                else:
                    name_entry.delete(0, END)
                    name_entry.insert(END, "No users found in the database.")
            except Exception as e:
                name_entry.delete(0, END)
                name_entry.insert(END, "An error occurred while fetching user data.")
        else:
            name_entry.delete(0, END)
            name_entry.insert(END, "Please enter a user ID.")

    customer_id_entry.bind('<KeyRelease>', fetch_customer_name)

    

    # Add label and entry for Quantity
    fat_label = ttk.Label(form2_frame, text="Fat:", font=("Arial", 14), background='lightgray')
    fat_label.grid(row=1, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    fat_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    fat_entry.grid(row=1, column=1, padx=10, pady=8, sticky="e")  # Align to the right

    # Add label and entry for Fat
    snf_label = ttk.Label(form2_frame, text="Snf:", font=("Arial", 14), background='lightgray')
    snf_label.grid(row=1, column=2, padx=(30,10), pady=10, sticky="w")  # Align to the left

    snf_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    snf_entry.grid(row=1, column=3, padx=(10,120), pady=8, sticky="e")  # Align to the right

    # Add label and entry for SNF
    per_liter_rate_label = ttk.Label(form2_frame, text="Per Liter Rate:", font=("Arial", 14), background='lightgray')
    per_liter_rate_label.grid(row=2, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    per_liter_rate_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    per_liter_rate_entry.grid(row=2, column=1, padx=10, pady=8, sticky="e")  # Align to the right

    # Add label and entry for Per Liter Rate
    quantity_label = ttk.Label(form2_frame, text="Quantity:", font=("Arial", 14), background='lightgray')
    quantity_label.grid(row=2, column=2, padx=(30,10), pady=10, sticky="w")  # Align to the left

    quantity_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    quantity_entry.grid(row=2, column=3, padx=(10,120), pady=8, sticky="e")  # Align to the right

     # Bind the fetch_per_liter_rate function to the animal, fat, and snf entry widgets
    
    def fetch_milk_price(event=None):
        animal = animal_entry.get()
        fat = fat_entry.get()
        snf = snf_entry.get()

        
        # Check if all values are provided
        if animal and fat and snf:
            try:
                # Fetch the animal node from Firebase
                animal_node = db.child("milk").child(animal).get().val()

                # Check if the animal exists
                if animal_node:
                    for record_key, record_value in animal_node.items():
                        # Fetch the fat and snf values
                        fat_value = record_value.get("fat", None)
                        snf_value = record_value.get("snf", None)

                        # Check if fat and snf values exist and match the provided fat and snf
                        if fat_value is not None and snf_value is not None and fat == fat_value and snf == snf_value:
                            # Fetch the price
                            price = record_value.get("price", "No price found")
                            modified_price = float(price) - 2.00

                            if animal == "bufflow":
                                bonus = 3.00
                            elif animal == "cow":
                                bonus = 2.50
                            else:
                                bonus = 0.00

                            bonus_entry.delete(0, END)
                            bonus_entry.insert(END, bonus)

                            # Update the price entry with the fetched price
                            per_liter_rate_entry.delete(0, END)
                            per_liter_rate_entry.insert(END, modified_price)
                            break
                    else:
                        per_liter_rate_entry.delete(0, END)
                        per_liter_rate_entry.insert(END, "Fat or snf value not found")
                else:
                    per_liter_rate_entry.delete(0, END)
                    per_liter_rate_entry.insert(END, "Animal not found")

            except Exception as e:
                # Handle exceptions
                per_liter_rate_entry.delete(0, END)
                per_liter_rate_entry.insert(END, "Error fetching price: " + str(e))







    animal_entry.bind('<KeyRelease>', fetch_milk_price)
    fat_entry.bind('<KeyRelease>', fetch_milk_price)
    snf_entry.bind('<KeyRelease>', fetch_milk_price)

    # Add label and entry for Bonus
    bonus_label = ttk.Label(form2_frame, text="Bonus:", font=("Arial", 14), background='lightgray')
    bonus_label.grid(row=3, column=0, padx=(40,10), pady=10, sticky="w")  # Align to the left

    bonus_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14))
    bonus_entry.grid(row=3, column=1, padx=10, pady=8, sticky="e")  # Align to the right

    # Add label and entry for Total Amount
    total_amount_label = ttk.Label(form2_frame, text="Total Amount:", font=("Arial", 14), background='lightgray')
    total_amount_label.grid(row=3, column=2, padx=(30,10), pady=10, sticky="w")  # Align to the left

    total_amount_entry = ctk.CTkEntry(form2_frame, font=("Arial", 14), border_color='#F81717', border_width=2)
    total_amount_entry.grid(row=3, column=3, padx=(10,120), pady=8, sticky="e")

    def calculate_total_amount(event=None):
        # Get the quantity value
        quantity = quantity_entry.get()
        bonus = bonus_entry.get()

        # Get the price value
        price = per_liter_rate_entry.get()

        # Calculate the total amount if both quantity and price are provided
        if quantity and bonus and price:
            try:
                total_amount = float(quantity) * float(price) + float(bonus)

                # Update the total amount entry with the calculated value
                total_amount_entry.delete(0, END)
                total_amount_entry.insert(END, str(total_amount) + " Rs")
            except Exception as e:
                # Handle exceptions
                total_amount_entry.delete(0, END)
                total_amount_entry.insert(END, "Error calculating total amount")

    quantity_entry.bind('<KeyRelease>', calculate_total_amount)


    form3_frame = ctk.CTkFrame(root, fg_color="lightgray")
    form3_frame.pack(side="top", fill="x", padx=10, pady=(0, 4))

    # Add the save, clear, and view buttons
    save_button = ctk.CTkButton(form3_frame, font=("Arial", 14), text="Save", bg_color="#E3DBB7", hover_color="#12580A", fg_color="#187A0D", width=100, command=lambda: save())
    save_button.grid(row=0, column=1, padx=(150,10), pady=10, sticky="w")

    
    def save():
        date = date_entry.get()
        shift = shift_entry.get()
        category = animal_entry.get()
        customer_id = customer_id_entry.get()
        name = name_entry.get()
        fat = fat_entry.get()
        snf = snf_entry.get()
        per_liter_rate = per_liter_rate_entry.get()
        quantity = quantity_entry.get()
        bonus = bonus_entry.get()
        total = total_amount_entry.get()

        data = {
            "date": date,
            "shift": shift,
            "category": category,
            "customer_id": customer_id,
            "name": name,
            "fat" : fat,
            "snf" : snf,
            "per_liter_rate" : per_liter_rate,
            "quantity" : quantity,
            "bonus" : bonus,
            "total" : total
        }
        db.child("records").push(data)
        messagebox.showinfo("Success", "Bill generated successfully.")


    clear_button = ctk.CTkButton(form3_frame, font=("Arial", 14), text="Clear", bg_color="#E3DBB7", fg_color="#BB0707", hover_color="#AA0000", width=100, command=lambda: clear())
    clear_button.grid(row=0, column=2, padx=(50,10), pady=10, sticky="w")

    def clear():
            date_entry.delete(0, "end")
            shift_entry.delete(0, "end")
            animal_entry.delete(0, "end")
            customer_id_entry.delete(0, "end")
            name_entry.delete(0, "end")
            fat_entry.delete(0, "end")
            snf_entry.delete(0, "end")
            per_liter_rate_entry.delete(0, "end")
            quantity_entry.delete(0, "end")
            bonus_entry.delete(0, "end")
            total_amount_entry.delete(0, "end")

    view_button = ctk.CTkButton(form3_frame, font=("Arial", 14), text="View", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", width=100, command=lambda: view())
    view_button.grid(row=0, column=3, padx=(50,10), pady=10, sticky="w")

    def view():
        todays_date = date_entry.get()
        shift = shift_entry.get()
        category = animal_entry.get()
        customer_id = customer_id_entry.get()
        name = name_entry.get()
        fat = fat_entry.get()
        snf = snf_entry.get()
        per_liter_rate = per_liter_rate_entry.get()
        quantity = quantity_entry.get()
        bonus = bonus_entry.get()
        total = total_amount_entry.get()

        root.destroy()
        view_bill.print_bill(todays_date, shift, category, customer_id, name, fat, snf, per_liter_rate, quantity, bonus, total)


  

    root.mainloop()

#bill()