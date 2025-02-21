# Import package
import tkinter as tk
from tkinter import messagebox
import pickle
from PIL import Image, ImageTk

# login function
def login():
    
    #  Get the username and password from the input entrys
    entry_usr = v_usr.get()
    entry_pwd = v_pwd.get()
    
    # Create new dictionary if user information is not available
    try:
        try:
            # Read
            with open('user_info.pickle', 'rb') as f:
                user_info = pickle.load(f)
        except EOFError:       
            # Create empty dictionary
            user_info = {}
    except FileNotFoundError:
        # Create empty dictionary
        user_info = {}
    
    # Determine if the username exists
    if entry_usr in user_info:
        # Determine if the username and password match    
        if entry_pwd == user_info[entry_usr]:
            # Match
            tk.messagebox.showinfo(message = 'Login Success')
        else:
            # Do not match
            tk.messagebox.showerror(message = 'Error Password')
    
    # The username does not exist
    else:
        # Create an account or not (return true or false to sing_up)
        sign_up = tk.messagebox.askyesno(message = 'Do you want to create an account by your input?')
        # if true
        if sign_up:
            with open('user_info.pickle', 'wb') as f:
                # Add a new entry into dictionary
                user_info[entry_usr] = entry_pwd     
                # Write
                pickle.dump(user_info, f)

# sign function
def sign():
    
    # _sign function
    def _sign():
        #  Get the username, password and confirmed password from the input entrys
        entry2_usr = v2_usr.get()
        entry2_pwd = v2_pwd.get()
        entry2_cfm = v2_cfm.get()
        
        # Create new dictionary if user information is not available
        try:
            with open('user_info.pickle', 'rb') as f:
                user2_info = pickle.load(f)
        except FileNotFoundError:
            user2_info = {}
        
        # Determine if the username exists
        if entry2_usr in user2_info:
            tk.messagebox.showerror(message = 'This account has already existed')
        # Determine if the password and confirmed password match
        elif entry2_pwd != entry2_cfm:
            tk.messagebox.showerror(message = 'The password is inconsistent')
        # Sign up
        else:
            with open('user_info.pickle', 'wb') as f:
                # Add a new entry into dictionary
                user2_info[entry2_usr] = entry2_pwd
                # Write
                pickle.dump(user2_info, f)
                # Destroy window2
                window2.destroy()
                tk.messagebox.showinfo(message = 'Sign Up Success')
    # Create second wondow    
    window2 = tk.Toplevel(window)
    window2.title('Sign Up')
    window2.geometry('300x300')
    
    # String variable
    v2_usr = tk.StringVar()
    v2_pwd = tk.StringVar()
    v2_cfm = tk.StringVar()
    
    # Laebl 
    tk.Label(window2, text = 'User Name').place(x = 20, y = 20)
    tk.Label(window2, text = 'Password').place(x = 20, y = 50)
    tk.Label(window2, text = 'Confirm Password').place(x = 20, y = 80)
    
    # Entry
    tk.Entry(window2, textvariable = v2_usr).place(x = 130, y = 20)
    tk.Entry(window2, textvariable = v2_pwd, show = '*').place(x = 130, y = 50)
    tk.Entry(window2, textvariable = v2_cfm, show = '*').place(x = 130, y = 80)

    # Button
    tk.Button(window2, text = 'Sign Up', command = lambda: _sign()).place(x = 150, y = 130)


if __name__ == '__main__':
    
    # Create main window
    window = tk.Tk()
    window.title('Lab5')
    window.geometry('300x320')
    
    # Split the window into two sections
    f1 = tk.Frame(window)
    f2 = tk.Frame(window)
    f1.pack()
    f2.pack()
    
    # Insert and resize an image
    image1 = ImageTk.PhotoImage( Image.open('beagle.jpg').resize((300, 200)) )
    im = tk.Label(f1, image=image1)
    im.pack()

    # String variable
    v_usr = tk.StringVar()
    v_pwd = tk.StringVar()
    
    # Label 
    tk.Label(window, text = 'User:').place(x = 20, y = 220)
    tk.Label(window, text = 'Password:').place(x = 20, y = 240)
    
    # Entry
    tk.Entry(window, textvariable = v_usr).place(x = 100, y = 220)
    tk.Entry(window, textvariable = v_pwd, show = '*').place(x = 100, y = 240)

    # Button
    tk.Button(window, text = 'Log In', command = lambda: login()).place(x = 70, y = 275)
    tk.Button(window, text = 'Sign Up', command = lambda: sign()).place(x = 150, y = 275)
  
    # Repeat the loop to keep the computation ongoing
    window.mainloop()