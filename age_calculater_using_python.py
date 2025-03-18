# AGE CALCUTAOR USING PYTHON GUI (TKINTER)


import tkinter as tk # Importing tkinter for GUI
from tkinter import messagebox # Importing message box from tkinter module for the output message box
from datetime import date # Import the "date" class from the "datetime" module to work with dates and all


def calculating_the_age() :
    try:
        # Getting the birth date information from the user
        year=int(year_entry.get()) # User Input for Year 
        month=int(month_entry.get()) # User Input for Month
        day=int(day_entry.get()) # User Input for Day
        Date=date(year,month,day) # Date of Birth
        
        # Confirmation Window
        confirmation=messagebox.askyesno("Confirming Date",f"You entered {Date} Format (YYYY-MM-DD) . Is this correct ?")
        if not confirmation :
            messagebox.showinfo("Error","Please Enter the correct birth date again .")
            return False  
        
        # Calculating the difference between the birth date and the current date
        today=date.today()  # Estimating the current date
        age_days=(today-Date).days  # Days between dates
        years=age_days//365  # Estimating years
        remaining_days=age_days%365  # Remaining days after calculating years
        months=remaining_days//30  # Estimating months
        days=remaining_days%30  # Calculating remaining days

        # Showing the calculated age in a message box
        messagebox.showinfo("Your Age" , f"You are {years} years , {months} months , and {days} days old.")
        return True

    except ValueError :
        # Error message for invalid input by user
        messagebox.showerror("Error","Please enter valid numbers.")


# MAIN GUI WINDOW


window=tk.Tk() # Creating a window
window.title("Age Calculator")  

# Entry Field 1 (Birth Date ?)
tk.Label(window,text="Enter Birth Day (1-31) --> ").grid(padx=12,pady=10,row=0,column=0)
day_entry=tk.Entry(window)
day_entry.grid(row=0,column=1,padx=15,pady=10) # Indentation

print()
# Entry Field 2 (Birth Month ?)
tk.Label(window,text="Enter Birth Month (1-12) --> ").grid(padx=12,pady=10,row=1,column=0)
month_entry=tk.Entry(window)
month_entry.grid(row=1,column=1,padx=15,pady=10)  # Indentation

print()
# Entry Field 3 (Birth Year ?)
tk.Label(window,text="Enter Birth Year --> ").grid(padx=12,pady=10,row=2,column=0)
year_entry=tk.Entry(window)
year_entry.grid(row=2,column=1,padx=15,pady=10)  # Indentation

print()
# Adding Buttons to calculate age in year,month,days
calculate_button=tk.Button(window,text=" Calculate The Age ! ",command=calculating_the_age)  
calculate_button.grid(row=3,column=0,columnspan=2,pady=20)  # Button Indentation

# Running the GUI window
window.mainloop()
