import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from csv import DictWriter
import os

window = tk.Tk()
window.title("Monthly Expenditure")
window.geometry("450x550")
window.resizable(width = False, height = False)

#create Items Name label
name_label = ttk.Label(window, text = "Purchased items name:")
name_label.grid(row=0, column=0,padx = 14, pady = 14, sticky = tk.W)

#create Name Entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width = 16, textvariable = name_var)
name_entrybox.grid(row = 0,  column = 1, padx = 14, pady = 14)
name_entrybox.focus()


#create Price Name label
price_label = ttk.Label(window, text = "Enter price:")
price_label.grid(row = 1, column = 0,padx = 14, pady = 14,sticky = tk.W)

#create Price Entry box
price_var = tk.DoubleVar()
price_entrybox = ttk.Entry(window, width = 16, textvariable = price_var)
price_entrybox.grid(row = 1,  column = 1, padx = 14, pady = 14)
price_entrybox.focus()

#create Shop Name label
shop_name = ttk.Label(window, text = "Select Shop name:")
shop_name.grid(row = 3, column = 0,padx = 14, pady = 14,sticky = tk.W)

#create Combobox
shop_var = tk.StringVar()
shop_combobox = ttk.Combobox(window, width = 14, textvariable = shop_var, state = 'readonly')
shop_combobox['values'] = ('Udaya Store', 'Woolworth', 'Big Apple', 'Sunrise Fresh')
shop_combobox.current(0)
shop_combobox.grid(row = 3, column = 1, padx = 14, pady = 14)

#create Calendar Label
calendar_label = ttk.Label(window, text = "Choose Date:")
calendar_label.grid(row = 4, column = 0,padx = 14, pady = 14,sticky = tk.W)

#Creating Calendar
cal = Calendar(window, selectmode = "day", year = 2020, month = 8, day = 27)
cal.grid(row = 5, column = 1)

def Exit():
    window.destroy()
    
def action():
    item_name = name_var.get()
    item_price = price_var.get()
    shop_details = shop_var.get()
    calc_date = cal.get_date()
        
    #write to csv, 
    with open("Monthly_details.csv", 'a', newline="") as f:
        dict_writer = DictWriter(f, fieldnames = ['Item Name', 'Item Price', 'Shop Name', 'Date'])
        
        if os.stat('Monthly_details.csv'). st_size == 0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'Item Name' : item_name,
            'Item Price' : item_price,
            'Shop Name': shop_details,
            'Date'      : calc_date,
           
            })
    
    name_entrybox.delete(0, tk.END)
    price_entrybox.delete(0, tk.END)



#creating Submit Button
submit_button = ttk.Button(window, text = 'Submit', command = action)
submit_button.grid(row = 7, column = 1, padx = 14, pady = 30)


exit_button = ttk.Button(window, text = 'EXIT', command = Exit)
exit_button.grid(row = 8, column = 1, padx = 14, pady = 10)

window.mainloop()


