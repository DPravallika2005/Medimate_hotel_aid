from tkinter import Tk, Frame, Label, Entry, Button, messagebox, ttk, Text, PhotoImage
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title('MEDIMATE HOSTEL AID')
        self.front_frame = Frame(self.root, width=1366, height=764, bg='white')
        self.front_frame.place(x=0, y=0)
        self.image = Image.open(r'C:\Users\admin\Desktop\wise_project\assets\WhatsApp Image 2024-02-26 at 9.55.00 AM.jpeg')
        self.image = self.image.resize((1366,765))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.front_frame,image=self.image)
        self.image_label.image = self.image
        self.image_label.place(x=0,y=0)
        title_label = Label(self.front_frame, text='MEDIMATE HOSTEL AID', font=('Courier New', 30, 'bold'), bg='white')
        title_label.place(relx=0.5, rely=0.4, anchor='center')
        next_button = Button(self.front_frame, text='NEXT', font=('Courier New', 12, 'bold'), command=self.show_next_page)
        next_button.place(relx=0.5, rely=0.7, anchor='center')

    def show_next_page(self):
        self.front_frame.destroy()
        second_page = SecondPage(self.root)

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.title('MOTTO')
        self.second_frame = Frame(self.root, width=1366, height=765, bg='white')
        self.second_frame.place(x=0, y=0)

        self.image = Image.open(r'C:\Users\admin\Desktop\wise_project\assets\WhatsApp Image 2024-02-26 at 12.31.35 PM.jpeg')
        self.image = self.image.resize((1366,765))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.second_frame,image=self.image)
        self.image_label.image = self.image
        self.image_label.place(x=0,y=0)

        heading_label = Label(self.second_frame, text='MOTTO', font=('Courier New', 25, 'bold'), bg='white')
        heading_label.place(relx=0.5, rely=0.2, anchor='center')
        description_label = Label(self.second_frame, text='Medimate Hostel Aid streamlines hostel life by managing medicine donations, ensuring availability for students. It promotes well-being through efficient medication distribution, fostering a healthier and more convenient living environment for hostelmates.', font=('Courier New', 12), bg='white', wraplength=600, justify='center')
        description_label.place(relx=0.5, rely=0.5, anchor='center')
        lets_go_button = Button(self.second_frame, text="LET'S GO", font=('Courier New', 12, 'bold'), command=self.show_third_page)
        lets_go_button.place(relx=0.5, rely=0.8,anchor='center')

    def show_third_page(self):
        self.second_frame.destroy()
        third_page = ThirdPage(self.root)

class ThirdPage:
    def __init__(self, root):
        self.root = root
        self.root.title('LOGIN / SIGNUP')
        self.third_frame = Frame(self.root, width=1366, height=765, bg='white')
        self.third_frame.place(x=0, y=0)

        self.image = Image.open(r'C:\Users\admin\Desktop\wise_project\assets\WhatsApp Image 2024-02-26 at 1.38.30 PM.jpeg')
        self.image = self.image.resize((1366,765))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.third_frame,image=self.image)
        self.image_label.image = self.image
        self.image_label.place(x=0,y=0)

        login_label = Label(self.third_frame, text='Login', font=('Courier New', 14, 'bold'), bg='white')
        login_label.place(relx=0.25, rely=0.2, anchor='center')

        name_label_login = Label(self.third_frame, text='Name:', font=('Courier New', 12), bg='white')
        name_label_login.place(relx=0.08, rely=0.35, anchor='center')
        self.name_entry_login = Entry(self.third_frame, font=('Courier New', 12), width=15)
        self.name_entry_login.place(relx=0.25, rely=0.35, anchor='center')

        password_label_login = Label(self.third_frame, text='Password:', font=('Courier New', 12), bg='white')
        password_label_login.place(relx=0.08, rely=0.5, anchor='center')
        self.password_entry_login = Entry(self.third_frame, show='*', font=('Courier New', 12), width=15)
        self.password_entry_login.place(relx=0.25, rely=0.5, anchor='center')

        login_button = Button(self.third_frame, text='Login', font=('Courier New', 12, 'bold'), command=self.validate_login)
        login_button.place(relx=0.25, rely=0.65, anchor='center')

        signup_label = Label(self.third_frame, text='Signup', font=('Courier New', 14, 'bold'), bg='white')
        signup_label.place(relx=0.75, rely=0.2, anchor='center')

        name_label_signup = Label(self.third_frame, text='Name:', font=('Courier New', 12), bg='white')
        name_label_signup.place(relx=0.58, rely=0.35, anchor='center')
        self.name_entry_signup = Entry(self.third_frame, font=('Courier New', 12), width=14)
        self.name_entry_signup.place(relx=0.75, rely=0.35, anchor='center')

        password_label_signup = Label(self.third_frame, text='Password:', font=('Courier New', 12), bg='white')
        password_label_signup.place(relx=0.58, rely=0.5, anchor='center')
        self.password_entry_signup = Entry(self.third_frame, show='*', font=('Courier New', 12), width=14)
        self.password_entry_signup.place(relx=0.75, rely=0.5, anchor='center')

        signup_button = Button(self.third_frame, text='Signup', font=('Courier New', 12, 'bold'), command=self.validate_signup)
        signup_button.place(relx=0.75, rely=0.65, anchor='center')

    def validate_login(self):
        name = self.name_entry_login.get().strip()
        password = self.password_entry_login.get().strip()

        if not name:
            messagebox.showerror('Error', 'Enter your name')
        elif len(password) < 6:
            messagebox.showerror('Error', 'Password must be at least 6 characters')
        else:
            if self.check_user_in_database(name, password):
                self.third_frame.destroy()
                self.show_fourth_page() 
            else:
                messagebox.showerror('Error', 'Account does not exist. Please signup.')

    def validate_signup(self):
        name = self.name_entry_signup.get().strip()
        password = self.password_entry_signup.get().strip()

        if not name:
            messagebox.showerror('Error', 'Enter your name')
        elif len(password) < 6:
            messagebox.showerror('Error', 'Password must be at least 6 characters')
        else:
            self.add_user_to_database(name, password)
            self.third_frame.destroy()
            self.show_fourth_page() 

    def check_user_in_database(self, name, password):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user_info WHERE name=? AND password=?', (name, password))
        result = c.fetchone()
        conn.close()
        return result is not None

    def add_user_to_database(self, name, password):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_info (name, password) VALUES (?, ?)', (name, password))
        conn.commit()
        conn.close()
    def show_fourth_page(self):
        self.third_frame.destroy()
        fourth_page = FourthPage()
class FourthPage:
    def __init__(self):
        def create_table():
            conn = sqlite3.connect('tablet.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS medicine_data
                        (medicine_name TEXT, medicine_count INTEGER, hostel_name TEXT, room_no INTEGER, contact_no INTEGER)''')
            conn.commit()
            conn.close()
        def save_data():
            if not donor_medicine_name.get():
                messagebox.showwarning("Warning", "Please enter Medicine Name for Donor.")
                return
            if not donor_medicine_count.get().isdigit():
                messagebox.showwarning("Warning", "Please enter a valid Medicine Count for Donor.")
                return
            if not donor_hostel_name.get().isalpha():
                messagebox.showwarning("Warning", "Please enter a valid Hostel Name for Donor.")
                return
            if not donor_room_no.get().isdigit():
                messagebox.showwarning("Warning", "Please enter a valid Room No for Donor.")
                return
            if not donor_contact_no.get().isdigit() or len(donor_contact_no.get()) != 10:
                messagebox.showwarning("Warning", "Please enter a valid Contact No (10 digits) for Donor.")
                return

            conn = sqlite3.connect('tablet.db')
            c = conn.cursor()
            c.execute('INSERT INTO medicine_data VALUES (?, ?, ?, ?, ?)',
                    (donor_medicine_name.get(), int(donor_medicine_count.get()), donor_hostel_name.get(), int(donor_room_no.get()), int(donor_contact_no.get())))
            conn.commit()
            conn.close()
            clear_donor_entries()
            messagebox.showinfo("Success", "Donor Data saved successfully!")
        def clear_donor_entries():
            donor_medicine_name_entry.delete(0, 'end')
            donor_medicine_count_entry.delete(0, 'end')
            donor_hostel_name_entry.delete(0, 'end')
            donor_room_no_entry.delete(0, 'end')
            donor_contact_no_entry.delete(0, 'end')
        def search_medicine():
            if not recipient_medicine_name.get():
                messagebox.showwarning("Warning", "Please enter Medicine Name for Recipient.")
                return
            if not recipient_medicine_count.get().isdigit():
                messagebox.showwarning("Warning", "Please enter a valid Medicine Count for Recipient.")
                return

            conn = sqlite3.connect('tablet.db')
            c = conn.cursor()
            c.execute('SELECT medicine_name, medicine_count, hostel_name, room_no, contact_no FROM medicine_data WHERE medicine_name=? OR medicine_name LIKE ?', (recipient_medicine_name.get(), '%' + recipient_medicine_name.get() + '%'))
            results = c.fetchall()
            conn.close()

            if results:
                display_window = tk.Tk()
                display_window.title("Medicine Details")
                table = ttk.Treeview(display_window)
                table['columns'] = ('Medicine Name', 'Availability Count', 'Hostel Name', 'Room Number', 'Contact Number')
                table.column('#0', width=0, stretch=tk.NO)
                table.column('Medicine Name', anchor=tk.W, width=100)
                table.column('Availability Count', anchor=tk.W, width=150)
                table.column('Hostel Name', anchor=tk.W, width=150)
                table.column('Room Number', anchor=tk.W, width=100)
                table.column('Contact Number', anchor=tk.W, width=150)

                table.heading('#0', text='', anchor=tk.W)
                table.heading('Medicine Name', text='Medicine Name', anchor=tk.W)
                table.heading('Availability Count', text='Availability Count', anchor=tk.W)
                table.heading('Hostel Name', text='Hostel Name', anchor=tk.W)
                table.heading('Room Number', text='Room Number', anchor=tk.W)
                table.heading('Contact Number', text='Contact Number', anchor=tk.W)

                for result in results:
                    table.insert('', 'end', text='', values=(result[0], result[1], result[2], result[3], result[4]))
                table.pack(expand=tk.YES, fill=tk.BOTH)

                def delete_medicine():
                    selected_item = table.selection()
                    if selected_item:
                        item = table.item(selected_item)
                        medicine_name = item['values'][0]

                        conn = sqlite3.connect('tablet.db')
                        c = conn.cursor()
                        c.execute('DELETE FROM medicine_data WHERE medicine_name=?', (medicine_name,))
                        conn.commit()
                        conn.close()
                        table.delete(selected_item)
                        messagebox.showinfo("Success", f"Medicine {medicine_name} deleted successfully!")
                    else:
                        messagebox.showwarning("Warning", "Please select a medicine to delete.")

                delete_button = tk.Button(display_window, text="Delete", command=delete_medicine)
                delete_button.pack()

                display_window.mainloop()

            else:
                messagebox.showinfo("Medicine Availability", f"No information found for {recipient_medicine_name.get()}.")

        root.title("Medicine Management System")
        root.config(bg='lightgreen')
        create_table()

        donor_frame = tk.Frame(root, padx=10, pady=10,bg = 'lightgreen')
        donor_frame.grid(row=0, column=0, sticky='n',padx=100,pady=10)

        donor_label = tk.Label(donor_frame, text="Donor")
        donor_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        donor_labels = ['Medicine Name', 'Medicine Count', 'Hostel Name', 'Room No', 'Contact No']
        for i, label_text in enumerate(donor_labels):
            label = tk.Label(donor_frame, text=label_text)
            label.grid(row=i+1, column=0, padx=40, pady=40, sticky='w')

        donor_medicine_name = tk.StringVar()
        donor_medicine_count = tk.StringVar()
        donor_hostel_name = tk.StringVar()
        donor_room_no = tk.StringVar()
        donor_contact_no = tk.StringVar()

        donor_medicine_name_entry = tk.Entry(donor_frame, textvariable=donor_medicine_name)
        donor_medicine_name_entry.grid(row=1, column=1, padx=10, pady=5)

        donor_medicine_count_entry = tk.Entry(donor_frame, textvariable=donor_medicine_count)
        donor_medicine_count_entry.grid(row=2, column=1, padx=10, pady=10)

        donor_hostel_name_entry = tk.Entry(donor_frame, textvariable=donor_hostel_name)
        donor_hostel_name_entry.grid(row=3, column=1,padx=10,pady=15)

        donor_room_no_entry = tk.Entry(donor_frame, textvariable=donor_room_no)
        donor_room_no_entry.grid(row=4, column=1,padx=10,pady=10)

        donor_contact_no_entry = tk.Entry(donor_frame, textvariable=donor_contact_no)
        donor_contact_no_entry.grid(row=5, column=1,padx=10,pady=10)

        donor_save_button = tk.Button(donor_frame, text="Save", command=save_data)
        donor_save_button.grid(row=6, column=0, columnspan=2, pady=25)

        recipient_frame = tk.Frame(root, padx=10, pady=10,bg='lightgreen')
        recipient_frame.grid(row=0, column=1, sticky='n',padx=250,pady=10)

        recipient_label = tk.Label(recipient_frame, text="Recipient")
        recipient_label.grid(row=0, column=2, columnspan=5, padx=10, pady=5)

        recipient_labels = ['Medicine Name', 'Count']
        for i, label_text in enumerate(recipient_labels):
            label = tk.Label(recipient_frame, text=label_text)
            label.grid(row=i+1, column=3, padx=40, pady=40, sticky='w')
        
        recipient_medicine_name = tk.StringVar()
        recipient_medicine_count = tk.StringVar()

        recipient_medicine_name_entry = tk.Entry(recipient_frame, textvariable=recipient_medicine_name)
        recipient_medicine_name_entry.grid(row=1, column=4, padx=15, pady=5,sticky='e')
        
        recipient_medicine_count_entry = tk.Entry(recipient_frame, textvariable=recipient_medicine_count)
        recipient_medicine_count_entry.grid(row=2, column=4, padx=15, pady=5,sticky='e')

        recipient_search_button = tk.Button(recipient_frame, text="Search", command=search_medicine)
        recipient_search_button.grid(row=3, column=2, columnspan=2, padx=10,pady=10,sticky='e')
        
        feedback_button = tk.Button(root, text="Give Feedback", font=('Courier New', 12, 'bold'), command=self.show_feedback_page, bg='lightblue')
        feedback_button.place(relx=0.5, rely=0.85, anchor='center')

    def show_feedback_page(self):
        feedback_page = FeedbackPage(root)
class FeedbackPage:
    def __init__(self, root):
        self.root = root
        self.root.title('FEEDBACK')
        self.feedback_frame = Frame(self.root, width=1366, height=765, bg='white')
        self.feedback_frame.place(x=0, y=0)

        bg_image = Image.open(r'C:\Users\admin\Desktop\wise_project\assets\WhatsApp Image 2024-03-03 at 10.51.39 AM.jpeg')
        bg_image = bg_image.resize((1366,765))
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.feedback_frame, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0)

        feedback_heading = Label(self.feedback_frame, text='Feedback', font=('Courier New', 20, 'bold'), bg='white')
        feedback_heading.place(relx=0.5, rely=0.2, anchor='center')

        self.feedback_textbox = Text(self.feedback_frame, font=('Courier New', 12), width=40, height=8)
        self.feedback_textbox.place(relx=0.5, rely=0.5, anchor='center')

        submit_feedback_button = Button(self.feedback_frame, text='Submit Feedback', font=('Courier New', 12, 'bold'), command=self.submit_feedback)
        submit_feedback_button.place(relx=0.5, rely=0.8, anchor='center')

        exit_button = Button(self.feedback_frame, text='Exit', font=('Courier New', 12, 'bold'), command=self.return_to_front_page)
        exit_button.place(relx=0.85, rely=0.2, anchor='ne')

    def submit_feedback(self):
        feedback = self.feedback_textbox.get("1.0", "end-1c")
        if not feedback:
            messagebox.showwarning('Error', 'Please enter your feedback')
            return

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, feedback TEXT)')
        c.execute('INSERT INTO feedback (feedback) VALUES (?)', (feedback,))
        conn.commit()
        conn.close()

        messagebox.showinfo('Feedback', 'Thank you for your feedback!')

    def return_to_front_page(self):
        self.feedback_frame.destroy()
        front_page = FrontPage(self.root)

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}+0+0')

conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL)''')
conn.commit()
conn.close()
front_page = FrontPage(root)
root.mainloop()