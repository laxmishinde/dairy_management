import customtkinter as ctk
import tkinter as ttk
from PIL import Image, ImageGrab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tempfile import NamedTemporaryFile
import os
import bill



def print_bill(todays_date, shift, category, customer_id, name, fat, snf, per_liter_rate, quantity, bonus, total):
    app = ctk.CTk()
    app.title('Bill')

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

    # Create a frame for the bill
    main_frame = ctk.CTkFrame(app, bg_color="#fff", fg_color="#fff", width=window_width, height=500, border_color='#000000', border_width=2)
    main_frame.pack(side="top", fill="both", padx=10, pady=(10,0), expand=True) 

    # heading frame
    name_frame = ctk.CTkFrame(main_frame, bg_color="#fff", fg_color="#fff", width=window_width, height=495)
    name_frame.pack(side="top", fill="both", padx=3, pady=(3,10), expand=False) 

    name_label = ttk.Label(name_frame, text="Vyankateshwar Dairy Center, Ramapur", background="#fff", font=("Arial", 20))
    name_label.pack(side="left", padx=(125,10), pady=(5,5), expand=False)

    # Create a Canvas widget
    canvas = ttk.Canvas(main_frame, bg="#fff", width=720, height=5)
    canvas.pack()
    # Draw a horizontal line
    canvas.create_line(1, 0, 730, 0, fill="#000000", width=8)

    form1_frame = ctk.CTkFrame(main_frame, fg_color="#fff", width=window_width)
    form1_frame.pack(side="top", fill="x", padx=2, pady=(1, 2))

   
    date_label = ttk.Label(form1_frame, text="Date:", font=("Arial", 14), background="#fff")
    date_label.grid(row=0, column=0, padx=(10,10), pady=10, sticky="w")  # Align to the left

    date_value = ttk.Label(form1_frame, text=todays_date, font=("Arial", 14), background="#fff")
    date_value.grid(row=0, column=1, padx=(10,50), pady=10, sticky="e")  # Align to the left

    shift_label = ttk.Label(form1_frame, text="Shift:", font=("Arial", 14), background='#fff')
    shift_label.grid(row=0, column=2, padx=(290,5), pady=10, sticky="e")  # Align to the left

    shift_value = ttk.Label(form1_frame, font=("Arial", 14), text=shift, background='#fff')
    shift_value.grid(row=0, column=3, padx=(10,3), pady=10, sticky="e")  # Align to the right

    # Add label and entry for Category
    animal_label = ttk.Label(form1_frame, text="Category:", font=("Arial", 14), background='#fff')
    animal_label.grid(row=1, column=0, padx=(10,5), pady=10, sticky="w")  # Align to the left

    animal_value = ttk.Label(form1_frame, font=("Arial", 14), text=category, background='#fff')
    animal_value.grid(row=1, column=1, padx=(5,70), pady=8, sticky="e")  # Align to the right

    # Create a Canvas widget
    canvas = ttk.Canvas(main_frame, bg="#fff", width=720, height=5)
    canvas.pack()
    # Draw a horizontal line
    canvas.create_line(1, 0, 730, 0, fill="#000000", width=8)

    form2_frame = ctk.CTkFrame(main_frame, fg_color="#fff", width=window_width)
    form2_frame.pack(side="top", fill="x", padx=2, pady=(1, 2))

    customer_id_label = ttk.Label(form2_frame, text="Customer ID:", font=("Arial", 14), background='#fff')
    customer_id_label.grid(row=0, column=0, padx=(10,5), pady=(3,10), sticky="w")  # Align to the left

    customer_id_value = ttk.Label(form2_frame, font=("Arial", 14), text=customer_id, background='#fff')
    customer_id_value.grid(row=0, column=1, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right
    

    # Add label and entry for Name
    name_label = ttk.Label(form2_frame, text="Name:", font=("Arial", 14), background='#fff')
    name_label.grid(row=0, column=2, padx=(270,5), pady=(3,10), sticky="w")  # Align to the left

    name_value = ttk.Label(form2_frame, font=("Arial", 14), text=name, background='#fff')
    name_value.grid(row=0, column=3, padx=(5,3), pady=(3,10), sticky="e")  # Align to the right

    # Create a Canvas widget
    canvas = ttk.Canvas(main_frame, bg="#fff", width=720, height=5)
    canvas.pack()
    # Draw a horizontal line
    canvas.create_line(1, 0, 730, 0, fill="#000000", width=8)

    form3_frame = ctk.CTkFrame(main_frame, fg_color="#fff", width=window_width)
    form3_frame.pack(side="top", fill="x", padx=2, pady=(1, 2))


    # Add label and entry for Quantity
    fat_label = ttk.Label(form3_frame, text="Fat:", font=("Arial", 14), background='#fff')
    fat_label.grid(row=1, column=0, padx=(150,5), pady=(3,10), sticky="w")  # Align to the left

    fat_value = ttk.Label(form3_frame, font=("Arial", 14), text=fat, background='#fff')
    fat_value.grid(row=1, column=1, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right

    # Add label and entry for Fat
    snf_label = ttk.Label(form3_frame, text="Snf:", font=("Arial", 14), background='#fff')
    snf_label.grid(row=1, column=2, padx=(80,5), pady=(3,10), sticky="w")  # Align to the left

    snf_value = ttk.Label(form3_frame, font=("Arial", 14), text=snf, background='#fff')
    snf_value.grid(row=1, column=3, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right

    # Add label and entry for SNF
    per_liter_rate_label = ttk.Label(form3_frame, text="Per Liter Rate:", font=("Arial", 14), background='#fff')
    per_liter_rate_label.grid(row=2, column=0, padx=(150,5), pady=(3,10), sticky="w")  # Align to the left

    per_liter_rate_value = ttk.Label(form3_frame, font=("Arial", 14), text=per_liter_rate, background='#fff')
    per_liter_rate_value.grid(row=2, column=1, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right

    # Add label and entry for Per Liter Rate
    quantity_label = ttk.Label(form3_frame, text="Quantity:", font=("Arial", 14), background='#fff')
    quantity_label.grid(row=2, column=2, padx=(80,5), pady=(3,10), sticky="w")  # Align to the left

    quantity_value = ttk.Label(form3_frame, font=("Arial", 14), text=quantity, background='#fff')
    quantity_value.grid(row=2, column=3, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right

    bonus_label = ttk.Label(form3_frame, text="Bonus:", font=("Arial", 14), background='#fff')
    bonus_label.grid(row=3, column=0, padx=(150,5), pady=(3,10), sticky="w")  # Align to the left

    bonus_value = ttk.Label(form3_frame, font=("Arial", 14), text=bonus, background='#fff')
    bonus_value.grid(row=3, column=1, padx=(5,10), pady=(3,10), sticky="e")  # Align to the right

    # Add label and entry for Total Amount
    total_amount_label = ttk.Label(form3_frame, text="Total Amount:", font=("Arial", 14), background='#fff')
    total_amount_label.grid(row=3, column=2, padx=(80,5), pady=(3,10), sticky="w")  # Align to the left

    total_amount_value = ttk.Label(form3_frame, font=("Arial", 14), text=total, background='#fff')
    total_amount_value.grid(row=3, column=3, padx=(5,10), pady=(3,10), sticky="e")

    # Create a Canvas widget
    canvas = ttk.Canvas(main_frame, bg="#fff", width=720, height=5)
    canvas.pack()
    # Draw a horizontal line
    canvas.create_line(1, 0, 730, 0, fill="#000000", width=8)

    form4_frame = ctk.CTkFrame(main_frame, fg_color="#fff", width=window_width, height=120)
    form4_frame.pack(side="top", fill="x", padx=2, pady=(1, 2))

    # Add label for stamp
    stamp_label = ttk.Label(form4_frame, text="Stamp or Signature", font=("Arial", 13), background='#fff')
    stamp_label.grid(row=3, column=2, padx=(570,5), pady=(95,1), sticky="e") 






    # Create a frame for the form
    btn_frame = ctk.CTkFrame(app, bg_color="#fff", fg_color="#fff", width=window_width, height=30, border_color='#fff', border_width=1)
    btn_frame.pack(side="bottom", fill="both", padx=10, pady=(2,1), expand=False) 

    def back():
        app.destroy()
        bill.bill()

    def print_main_frame():
        # Take a screenshot of the main frame
        x, y, width, height = main_frame.winfo_rootx(), main_frame.winfo_rooty(), main_frame.winfo_width(), \
                              main_frame.winfo_height()
        screenshot = ImageGrab.grab((x, y, x + width, y + height))

         # Define the path to the folder where you want to save the file
        folder_path = "bill_images"

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
    back_button = ctk.CTkButton(btn_frame, font=("Arial", 14), text="Back", bg_color="#fff", hover_color="#12580A", fg_color="#187A0D", width=100, command=lambda: back())
    back_button.grid(row=0, column=0, padx=(510,10), pady=(1,1), sticky="e")

    print_button = ctk.CTkButton(btn_frame, font=("Arial", 14), text="Print", bg_color="#fff", hover_color="#12580A", fg_color="#187A0D", width=100, command=print_main_frame)
    print_button.grid(row=0, column=1, padx=(10,1), pady=(1,1), sticky="e")

    

    app.mainloop()


#print_bill(date,shift,category,customer_id,name,fat,snf,per_liter_rate,bonus,total)
#print_bill()
