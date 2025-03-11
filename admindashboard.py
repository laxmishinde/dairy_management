import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import manage_user
import milk_rate, bill, history
from history import show_history


def show_admin_dashboard():
    
    # Create main window
    root = ctk.CTk()
    root.title("Admin Dashboard")

    def manage():
        root.destroy()
        manage_user.show_manage_user()

    def milk():
        root.destroy()
        milk_rate.milk_price()

    def billing():
        root.destroy()
        bill.bill()

    def history():
        root.destroy()
        show_history()

    def logout():
        root.destroy()
        import Login_Signup
        Login_Signup

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
    project_heading = ttk.Label(heading_frame, text="Vyankteshwar Dairy Center", font=("Arial", 24), style="Heading.TLabel", padding=(47, 0))  # Added left and right padding
    project_heading.grid(row=0, column=1, padx=80, pady=10)  # Centered

    


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

    # Add label for Admin Dashboard with left alignment
    admin_dashboard_label = ttk.Label(admin_frame, text="Admin Dashboard", font=("Arial", 14), background='lightgray')
    admin_dashboard_label.grid(row=0, column=1, padx=(300,50), pady=10)  # Align to the left

    logout_button = ctk.CTkButton(admin_frame, font=("Arial", 16), text="Logout", fg_color="#1b2fa1", hover_color="#191D65", bg_color="#E3DBB7", width=50, command=lambda: logout())
    logout_button.grid(row=0, column=2, padx=(150,4), pady=10)

    # Create second horizontal frame for cards
    cards_frame = ctk.CTkFrame(root, fg_color="#D2D2D2")  # Adjusted height
    cards_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(5, 0))  # Reduced top padding

    #   Load images for each card
    card1_image = Image.open("image3.png")
    card1_image = card1_image.resize((80, 120), Image.LANCZOS)
    card1_image = ImageTk.PhotoImage(card1_image)

    card2_image = Image.open("image1.png")
    card2_image = card2_image.resize((80, 120), Image.LANCZOS)
    card2_image = ImageTk.PhotoImage(card2_image)

    card3_image = Image.open("image2.png")
    card3_image = card3_image.resize((80, 120), Image.LANCZOS)
    card3_image = ImageTk.PhotoImage(card3_image)

    card4_image = Image.open("image5.png")
    card4_image = card4_image.resize((80, 120), Image.LANCZOS)
    card4_image = ImageTk.PhotoImage(card4_image)

    # Create card frames manually
    card_frame1 = ctk.CTkFrame(cards_frame, fg_color="#26C3A7")
    card_frame1.grid(row=0, column=0, padx=25, pady=(70, 60), sticky="nsew")


    card_frame2 = ctk.CTkFrame(cards_frame, fg_color="#B1D02A")
    card_frame2.grid(row=0, column=1, padx=25, pady=(70, 60), sticky="nsew")

    card_frame3 = ctk.CTkFrame(cards_frame, fg_color="#2ACCD0")
    card_frame3.grid(row=0, column=2, padx=25, pady=(70, 60), sticky="nsew")

    card_frame4 = ctk.CTkFrame(cards_frame, fg_color="#D0902A")
    card_frame4.grid(row=0, column=3, padx=25, pady=(70, 60), sticky="nsew")

    # Add images to the card frames
    image_label1 = ttk.Label(card_frame1, image=card1_image, background="#26C3A7")
    image_label1.image = card1_image
    image_label1.bind("<Button-1>", lambda event: manage())
    image_label1.pack()

    image_label2 = ttk.Label(card_frame2, image=card2_image, background="#B1D02A")
    image_label2.image = card2_image
    image_label2.bind("<Button-1>", lambda event: billing())
    image_label2.pack()

    image_label3 = ttk.Label(card_frame3, image=card3_image, background="#2ACCD0")
    image_label3.image = card3_image
    image_label3.bind("<Button-1>", lambda event: history())
    image_label3.pack()

    image_label4 = ttk.Label(card_frame4, image=card4_image, background="#D0902A")
    image_label4.image = card4_image
    image_label4.bind("<Button-1>", lambda event: milk())
    image_label4.pack()

    #    Add text labels below the images
    text_label1 = ttk.Label(card_frame1, text="Manage Users", font=("Arial", 15), background='#A8A5A7')
    text_label1.pack()

    text_label2 = ttk.Label(card_frame2, text="Bill Generation", font=("Arial", 15), background='#A8A5A7')
    text_label2.pack()

    text_label3 = ttk.Label(card_frame3, text="Records History", font=("Arial", 15), background='#A8A5A7')
    text_label3.pack()

    text_label4 = ttk.Label(card_frame4, text="Set Milk Rate", font=("Arial", 15), background='#A8A5A7')
    text_label4.pack()



    # Run the application
    root.mainloop()

#show_admin_dashboard()
