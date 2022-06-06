######################################################################################
###This program is so we know what the customer hired from Julie's party hire store###
######################################################################################

#import tkinter to make a GUI
from tkinter import *

#quit function for the quit button

def quit():
    main_window.destroy()

#printing the entry details

def print_details():
    #variables used
    global details, total_entries, info
    info=0
    #making column headings
    Label(main_window,text='Costumer Name').grid(column=0,row=7)
    Label(main_window,text='Receipt Number').grid(column=1,row=7)
    Label(main_window,text='Item Held').grid(column=2,row=7)
    Label(main_window,text='Number Hired').grid(column=3,row=7)
    

    #adding each item in the list into their own row
    while info < total_entries:
        Label(main_window,text=info).grid(column=0,row=info+8)
        Label(main_window,text=(details[info][0])).grid(column=0,row=info+8)
        Label(main_window,text=(details[info][1])).grid(column=1,row=info+8)
        Label(main_window,text=(details[info][2])).grid(column=2,row=info+8)
        Label(main_window,text=(details[info][3])).grid(column=3,row=info+8)
        Label(main_window,text=(details[info][4])).grid(column=4,row=info+8)
        info+= 1

#checking if the inputs are all valid
def check():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    entry_check=0
 
    
    #checking that costumer name is not blank, set error text if blank
    if len(entry_customer_name.get())==0:
        Label(main_window,fg='red',text='Please enter your name').grid(column=2,row=0)
        entry_check=1
        
    #checking that receipt is not blank and sending error if its blank
    if len(entry_receipt_number.get())==0:
        Label(main_window,fg='red',text='Please enter your receipt number').grid(column=2,row=1)
        entry_check=1

    #checking that item held is not blank and sending error if its blank
    if len(entry_item_held.get()) == 0:
        Label(main_window,fg='red',text='Please choose your item').grid(column=2,row=2)

    #checking that number hired is not blank and sending error if its blank
    if (entry_number_hired.get().isdigit()):
        if int(entry_number_hired.get()) < 1 or int(entry_number_hired.get()) > 500:
            Label(main_window,fg='red',text='1 to 500 only').grid(column=2,row=3)
            entry_check=1
    else:
        Label(main_window,fg='red',text='1 to 500 only').grid(column=2,row=3)
        entry_check=1
    if entry_check ==0:
        append_details()

#appending the customer details

def append_details():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    #append each deteails to its own area of list
    details.append([entry_customer_name.get(),
                    entry_receipt_number.get(),
                    entry_item_held.get(),
                    entry_number_hired.get(),
                    delete_item.get()])
    #clearing the boxes
    entry_customer_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_item_held.delete(0,'end')
    entry_number_hired.delete(0,'end')
    delete_item.delete(0,'end')
    total_entries +=1

#deleting row from the list
def delete_row():
    #variables used
    global details,delete_item,total_entries,info
    #find which row to be deleted
    del details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    #clearing the last detail displayed on the GUI
    Label(main_window, text="                                 ").grid(column=0, row=info+7)
    Label(main_window, text="                                 ").grid(column=1, row=info+7)
    Label(main_window, text="                                 ").grid(column=2, row=info+7)
    Label(main_window, text="                                 ").grid(column=3, row=info+7)
    Label(main_window, text="                                 ").grid(column=4, row=info+7)
    #print every item in the list
    print_details()

#creating buttons and labels
def buttons():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,delete_item,total_entries
    #creating buttons
    Button(main_window,text='Quit', command=quit, width=10).grid(column=4,row=0,sticky=E)
    Button(main_window,text='Append Details',command=check).grid(column=3,row=1)
    Button(main_window,text='Print Details',command=print_details,width=10).grid(column=4,row=1,sticky=E)

    #creating empty entry boxes and putting labels
    Label(main_window,text='Customer Name').grid(column=0,row=0,sticky=E)
    entry_customer_name=Entry(main_window)
    entry_customer_name.grid(column=1,row=0)
    Label(main_window,text='Receipt Number').grid(column=0,row=1,sticky=E)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1,row=1)
    Label(main_window,text='Item Held').grid(column=0,row=2,sticky=E)
    entry_item_held=Entry(main_window)
    entry_item_held.grid(column=1,row=2)
    Label(main_window,text='Number Hired').grid(column=0,row=3,sticky=E)
    entry_number_hired=Entry(main_window)
    entry_number_hired.grid(column=1,row=3)
    #row deleting
    Label(main_window,text='Delete Row #').grid(column=3,row=2,sticky=E)
    delete_item=Entry(main_window)
    delete_item.grid(column=4,row=2)
    Button(main_window,text='Delete Row',command=delete_row,width=10).grid(column=5,row=2)
    

#to start the program
def main():
    #variables used
    global main_window
    global details,entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    #creating an empty list for the details
    details=[]
    total_entries=0
    #creating the GUI to start it
    main_window=Tk()
    buttons()
    main_window.mainloop()

main()


    
