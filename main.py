import tempfile
from tkinter import *
from tkinter import messagebox
import random
import os
import smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')

####################################################-Functions-#######################################
def clear():

    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    bill_entry.delete(0,END)

    prod1EntryD.delete(0,END)
    prod2EntryD.delete(0, END)
    prod3EntryD.delete(0, END)
    prod4EntryD.delete(0, END)
    prod5EntryD.delete(0, END)
    prod6EntryD.delete(0,END)

    prod1EntryF.delete(0,END)
    prod2EntryF.delete(0, END)
    prod3EntryF.delete(0, END)
    prod4EntryF.delete(0, END)
    prod5EntryF.delete(0, END)
    prod6EntryF.delete(0,END)

    prod1EntryS.delete(0,END)
    prod2EntryS.delete(0, END)
    prod3EntryS.delete(0, END)
    prod4EntryS.delete(0, END)
    prod5EntryS.delete(0, END)
    prod6EntryS.delete(0,END)

    prod1EntryD.insert(0,0)
    prod2EntryD.insert(0,0)
    prod3EntryD.insert(0,0)
    prod4EntryD.insert(0,0)
    prod5EntryD.insert(0,0)
    prod6EntryD.insert(0,0)

    prod1EntryF.insert(0,0)
    prod2EntryF.insert(0,0)
    prod3EntryF.insert(0,0)
    prod4EntryF.insert(0,0)
    prod5EntryF.insert(0,0)
    prod6EntryF.insert(0,0)

    prod1EntryS.insert(0,0)
    prod2EntryS.insert(0,0)
    prod3EntryS.insert(0,0)
    prod4EntryS.insert(0,0)
    prod5EntryS.insert(0,0)
    prod6EntryS.insert(0,0)

    textArea.delete(1.0, END)

    taxEntry.delete(0,END)
    totalPriceEntry.delete(0,END)

def send_email():

    def send_gmail():

        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(sender_entry.get(), password_entry.get())
            message = email_textarea.get(1.0, END)
            receiver_address = recipient_entry.get()
            ob.quit()
            ob.sendmail(sender_entry.get(), receiver_address, message)
            messagebox.showinfo('Success', 'Email was sent')

        except:
            messagebox.showerror('Error', 'Something went wrong')

    if textArea.get(1.0, END) == "\n":
        messagebox.showerror('Error', 'Bill is empty')

    else:
        root1 = Toplevel()
        root1.title('Send Email')
        root1.config(bg='red')
        root1.resizable(0,0)

        sender_frame = LabelFrame(root1, text='Sender', font=('arial', 16, 'bold'))
        sender_frame.grid(row=0, column=0, padx=10, pady=8)

        sender_label = Label(sender_frame, text="Sender's Email", font=('arial', 14, 'bold'), bg='white')
        sender_label.grid(row=0, column=0)

        sender_entry = Entry(sender_frame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        sender_entry.grid(row=0, column=1)

        password_label = Label(sender_frame, text="Password", font=('arial', 14, 'bold'), bg='white')
        password_label.grid(row=1, column=0)

        password_entry = Entry(sender_frame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,
                               show="*")
        password_entry.grid(row=1, column=1)

        recipient_frame = LabelFrame(root1, text="Customer", font=('arial', 14, 'bold'), bg='white')
        recipient_frame.grid(row=1, column=0, padx=40, pady=20)

        recipient_label = Label(recipient_frame, text="Email address", font=('arial', 14, 'bold'), bg='white')
        recipient_label.grid(row=0, column=0, padx=10, pady=8)

        recipient_entry = Entry(recipient_frame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recipient_entry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipient_frame, text="Message", font=('arial', 14, 'bold'), bg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipient_frame, font=('arial', 14, 'bold'), bg='white', width=43, height=11)
        email_textarea.grid(row=2, column=1,columnspan=2)
        email_textarea.grid(row=2, column=0, rowspan=2)
        email_textarea.delete(1.0, END)


        send_button = Button(root1, text='SEND', font=('arial', 14, 'bold'), width=15,
                              command=send_gmail)
        send_button.grid(row=2, column=0, pady=20)

        root1.mainloop()
def print_bill():

    if textArea.get(1.0, END) == "\n": #when there is an empty text area
        messagebox.showerror('Error', 'Bill is Empty')

    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textArea.get(1.0, END))
        os.startfile(file, 'print')
def search_bills():

    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_entry.get():
            f = open(f'bills/{i}', 'r')
            textArea.delete(1.0, END)
            for data in f:
                textArea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Bill does not exist')
def save_bill():

    global bill_number
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
         bill_content = textArea.get(1.0,END)
         file = open(f'bills/{bill_number}.txt', 'w')
         file.write(bill_content)
         file.close()
         messagebox.showinfo('Success', f'Bill Number {bill_number} has been saved successfully')
         bill_number = random.randint(10000, 100000000)

bill_number = random.randint(10000, 100000000)
def total():

    global pd1, pd2, pd3,pd4, pd5, pd6,pf1, pf2, pf3, pf4, pf5, pf6,ps1, ps2, ps3, ps4, ps5, ps6

    pd1 = int(prod1EntryD.get())*2.49
    pd2 = int(prod2EntryD.get())*4.29
    pd3 = int(prod3EntryD.get()) * 2.59
    pd4 = int(prod4EntryD.get()) * 3.49
    pd5 = int(prod5EntryD.get()) * 2.49
    pd6 = int(prod6EntryD.get()) * 2.79

    drinksTotal = pd1+pd2+pd3+pd4+pd5+pd6

    pf1 = int(prod1EntryF.get()) * 5.29
    pf2 = int(prod2EntryF.get()) * 5.39
    pf3 = int(prod3EntryF.get()) * 5.29
    pf4 = int(prod4EntryF.get()) * 8.79
    pf5 = int(prod5EntryF.get()) * 6.79
    pf6 = int(prod6EntryF.get()) * 2.49

    foodsTotal = pf1+pf2+pf3+pf4+pf5+pf6

    ps1 = int(prod1EntryS.get()) * 7.79
    ps2 = int(prod2EntryS.get()) * 4.49
    ps3 = int(prod3EntryS.get()) * 1.49
    ps4 = int(prod4EntryS.get()) * 2.49
    ps5 = int(prod5EntryS.get()) * 2.29
    ps6 = int(prod6EntryS.get()) * 2.29

    sweetsTotal = ps1+ps2+ps3+ps4+ps5+ps6

    global  payable_amt
    payable_amt = sweetsTotal + drinksTotal + foodsTotal + ((sweetsTotal + drinksTotal + foodsTotal) * 0.13)
    payable_amt = round(payable_amt, 2)

    totalAmt = drinksTotal + foodsTotal + sweetsTotal
    totalAmt = round(totalAmt,2)
    totalPriceEntry.delete(0,END)

    tax = totalAmt * 0.13
    tax = round(tax, 2)
    taxEntry.delete(0,END)

    taxEntry.insert(0,'$'f'{tax}')
    totalPriceEntry.insert(0, '$'f'{totalAmt}')

def bill_area():

    if name_entry.get() == '' or phone_entry.get() == '':
        messagebox.showerror('Error', 'Customer Details are required')

    elif totalPriceEntry.grid() == '':
        messagebox.showerror('Error', 'No products are selected')

    elif totalPriceEntry.grid() == '$0.0':
        messagebox.showerror('Error', 'No products are selected')

    else:
        textArea.delete(0.0, END)
        textArea.insert(END, '\t\t*** Tim Hortons ***')
        textArea.insert(END, f'\n\nBill Number: {bill_number}')
        textArea.insert(END, f'\n\nCustomer Name: {name_entry.get()}')
        textArea.insert(END, f'\n\nTelephone: {phone_entry.get()}')
        textArea.insert(END, '\n****************************************************')
        textArea.insert(END, '\nProduct\t\t\tQuantity\t\t\tCost')
        textArea.insert(END, '\n****************************************************')

        if prod1EntryD.get()!=0:
            textArea.insert(END, f'\nIced Coffee\t\t\t{prod1EntryD.get()}\t\t\t{pd1}')

        if prod2EntryD.get()!=0:
            textArea.insert(END, f'\nMocha Iced Cap\t\t\t{prod2EntryD.get()}\t\t\t{pd2}')

        if prod3EntryD.get()!=0:
            textArea.insert(END, f'\nMilk\t\t\t{prod3EntryD.get()}\t\t\t{pd3}')

        if prod4EntryD.get()!=0:
            textArea.insert(END, f'\nCappuccino\t\t\t{prod4EntryD.get()}\t\t\t{pd4}')

        if prod5EntryD.get()!=0:
            textArea.insert(END, f'\nHot Chocolate\t\t\t{prod5EntryD.get()}\t\t\t{pd5}')

        if prod6EntryD.get()!=0:
            textArea.insert(END, f'\nFrench Vanilla\t\t\t{prod6EntryD.get()}\t\t\t{pd6}')

        if prod1EntryF.get()!=0:
            textArea.insert(END, f'\nFarmer\'s Sandwich\t\t\t{prod1EntryF.get()}\t\t\t{pf1}')

        if prod2EntryF.get()!=0:
            textArea.insert(END, f'\nBacon Sandwich\t\t\t{prod2EntryF.get()}\t\t\t{pf2}')

        if prod3EntryF.get()!=0:
            textArea.insert(END, f'\nBagel Belt\t\t\t{prod3EntryF.get()}\t\t\t{pf3}')

        if prod4EntryF.get()!=0:
            textArea.insert(END, f'\nBBQ Chicken Wrap\t\t\t{prod4EntryF.get()}\t\t\t{pf4}')

        if prod5EntryF.get()!=0:
            textArea.insert(END, f'\nVeggie Wrap\t\t\t{prod5EntryF.get()}\t\t\t{pf5}')

        if prod6EntryF.get()!=0:
            textArea.insert(END, f'\nPotato Wedges\t\t\t{prod6EntryF.get()}\t\t\t{pf6}')

        if prod1EntryS.get()!=0:
            textArea.insert(END, f'\n6 Assorted Donuts\t\t\t{prod1EntryS.get()}\t\t\t{ps1}')

        if prod2EntryS.get()!=0:
            textArea.insert(END, f'\n20 Assorted Timbits\t\t\t{prod2EntryS.get()}\t\t\t{ps2}')

        if prod3EntryS.get()!=0:
            textArea.insert(END, f'\nChocolate Chunk Cookie\t\t\t{prod3EntryS.get()}\t\t\t{ps3}')

        if prod4EntryS.get()!=0:
            textArea.insert(END, f'\nChocolate Croissants\t\t\t{prod4EntryS.get()}\t\t\t{ps4}')

        if prod5EntryS.get()!=0:
            textArea.insert(END, f'\nEverything Twist\t\t\t{prod5EntryS.get()}\t\t\t{ps5}')

        if prod6EntryS.get()!=0:
            textArea.insert(END, f'\nSavoury Pastry\t\t\t{prod1EntryS.get()}\t\t\t{ps6}')

        textArea.insert(END, f'\n\nCost: {totalPriceEntry.get()}')
        textArea.insert(END, f'\n\nTax: {taxEntry.get()}')
        textArea.insert(END, f'\n\nTotal Payable Amount: ${payable_amt}')
        save_bill()

####################################################-GUI-#############################################
#---------------------------Main Window Setup--------------------------------
root = Tk()
root.title("Tim Hortons Billing System")
root.geometry('1270x685')
root.configure(bg="red")

#-----------------------Heading------------------------------------------

headingLabel = Label(root, text= "Tim Hortons Billing System", font=('times new roman', 30, 'bold'),
                     bg="white", fg="red", bd=10, relief=FLAT)
headingLabel.pack(fill=X)

#----------------------------Customer Details Frame-----------------------

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'),
                                    fg="red", bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X, pady=10)


name_label = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'),
                                    fg="red", bd=8, relief=GROOVE, width=8)

name_label.grid(row=0, column=0, padx=20, pady=2)
name_entry = Entry(customer_details_frame)
name_entry.grid(row=0, column=1, padx=8)

phone_label = Label(customer_details_frame, text='Telephone Number', font=('times new roman', 15, 'bold'),
                                    fg="red", bd=8, relief=GROOVE, width=18)


phone_label.grid(row=0, column=2, padx=20, pady=2)
phone_entry = Entry(customer_details_frame)
phone_entry.grid(row=0, column=3, padx=8)


bill_label = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'),
                                    fg="red", bd=8, relief=GROOVE, width=12)

bill_label.grid(row=0, column=4, padx=20, pady=2)
bill_entry = Entry(customer_details_frame)
bill_entry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='SEARCH', font=('arial', 12, 'bold'), command=search_bills)
searchButton.grid(row=0, column=6, padx=20, pady=8)

#---------------------------Products---------------------------
productsFrame=Frame(root)
productsFrame.pack()

#Drinks Frame
drinksFrame = LabelFrame(productsFrame, text='Beverages', font=('times new roman', 15, 'bold'),
                         fg='red', bd=8, relief=GROOVE)

drinksFrame.grid(row=0, column=0)


#Drink Products
prod1LabelD = Label(drinksFrame, text='Iced Coffee', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.49

prod1LabelD.grid(row=0, column=0, pady=9)

prod1EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod1EntryD.grid(row=0, column=1, pady=9)
prod1EntryD.insert(0,0)


prod2LabelD = Label(drinksFrame, text='Mocha Iced Cap', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8) #4.29
prod2LabelD.grid(row=1, column=0, pady=9)
prod2EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod2EntryD.grid(row=1, column=1, pady=9)
prod2EntryD.insert(0,0)


prod3LabelD = Label(drinksFrame, text='Milk', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.59
prod3LabelD.grid(row=2, column=0, pady=9)
prod3EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod3EntryD.grid(row=2, column=1, pady=9)
prod3EntryD.insert(0,0)


prod4LabelD = Label(drinksFrame, text='Cappuccino', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#3.49
prod4LabelD.grid(row=3, column=0, pady=9)

prod4EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod4EntryD.grid(row=3, column=1, pady=9)
prod4EntryD.insert(0,0)


prod5LabelD = Label(drinksFrame, text='Hot Chocolate', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.49
prod5LabelD.grid(row=4, column=0, pady=9)

prod5EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod5EntryD.grid(row=4, column=1, pady=9)
prod5EntryD.insert(0,0)


prod6LabelD = Label(drinksFrame, text='French Vanilla', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.79
prod6LabelD.grid(row=5, column=0, pady=9)

prod6EntryD = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod6EntryD.grid(row=5, column=1, pady=9)
prod6EntryD.insert(0,0)


#Food frame
foodFrame = LabelFrame(productsFrame, text='Food', font=('times new roman', 15, 'bold'),
                         fg='red', bd=8, relief=GROOVE)

foodFrame.grid(row=0, column=1)

#Food products
prod1LabelF = Label(foodFrame, text='Farmer\'s Sandwich', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#5.29

prod1LabelF.grid(row=0, column=0, pady=9)

prod1EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod1EntryF.grid(row=0, column=1, pady=9)
prod1EntryF.insert(0,0)

prod2LabelF = Label(foodFrame, text='Bacon Sandwich', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#5.39

prod2LabelF.grid(row=1, column=0, pady=9)

prod2EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod2EntryF.grid(row=1, column=1, pady=9)
prod2EntryF.insert(0,0)

prod3LabelF = Label(foodFrame, text='Bagel Belt', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#5.29

prod3LabelF.grid(row=2, column=0, pady=9)

prod3EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod3EntryF.grid(row=2, column=1, pady=9)
prod3EntryF.insert(0,0)


prod4LabelF = Label(foodFrame, text='BBQ Chicken Wrap', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#8.79

prod4LabelF.grid(row=3, column=0, pady=9)

prod4EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod4EntryF.grid(row=3, column=1, pady=9)
prod4EntryF.insert(0,0)


prod5LabelF = Label(foodFrame, text='Veggie Wrap', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#6.79

prod5LabelF.grid(row=4, column=0, pady=9)

prod5EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod5EntryF.grid(row=4, column=1, pady=9)
prod5EntryF.insert(0,0)


prod6LabelF = Label(foodFrame, text='Potato Wedges', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.49

prod6LabelF.grid(row=5, column=0, pady=9)

prod6EntryF = Entry(foodFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod6EntryF.grid(row=5, column=1, pady=9)
prod6EntryF.insert(0,0)


#Sweets frame
sweetsFrame = LabelFrame(productsFrame, text='Sweets', font=('times new roman', 15, 'bold'),
                         fg='red', bd=8, relief=GROOVE)

sweetsFrame.grid(row=0, column=2)

#Sweets products
prod1LabelS = Label(sweetsFrame, text='6 Assorted Donuts', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#7.79

prod1LabelS.grid(row=0, column=0, pady=9)

prod1EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod1EntryS.grid(row=0, column=1, pady=9)
prod1EntryS.insert(0,0)

prod2LabelS = Label(sweetsFrame, text='20 Assorted Timbits', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#4.49
prod2LabelS.grid(row=1, column=0, pady=9)

prod2EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod2EntryS.grid(row=1, column=1, pady=9)
prod2EntryS.insert(0,0)


prod3LabelS = Label(sweetsFrame, text='Chocolate Chunk Cookie', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#1.49
prod3LabelS.grid(row=2, column=0, pady=9)

prod3EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod3EntryS.grid(row=2, column=1, pady=9)
prod3EntryS.insert(0,0)


prod4LabelS = Label(sweetsFrame, text='Chocolate Croissants', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.49
prod4LabelS.grid(row=3, column=0, pady=9)

prod4EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod4EntryS.grid(row=3, column=1, pady=9)
prod4EntryS.insert(0,0)


prod5LabelS = Label(sweetsFrame, text='Everything Twist', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.29
prod5LabelS.grid(row=4, column=0, pady=9)

prod5EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod5EntryS.grid(row=4, column=1, pady=9)
prod5EntryS.insert(0,0)

prod6LabelS = Label(sweetsFrame, text='Savoury Pastry', font=('times new roman', 15, 'bold'),
                   fg='red', bd=8)#2.29

prod6LabelS.grid(row=5, column=0, pady=9)

prod6EntryS = Entry(sweetsFrame, font=('times new roman', 15, 'bold'), width=5, bd=5)
prod6EntryS.grid(row=5, column=1, pady=9)
prod6EntryS.insert(0,0)


#Bill area frame
billFrame = Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billAreaLabel = Label(billFrame, text='Bill Area',font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billAreaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textArea = Text(billFrame, height=18, width=52, yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

#----------------------------------------Bill Menu Frame--------------------

billMenuFrame = LabelFrame(root, text="Bill Menu", font=('times new roman', 15, 'bold'), width=5, bd=5, pady=10)
billMenuFrame.pack(fill=X)

totalPriceLabel = Label(billMenuFrame, text='Total Cost',font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE, width=10)
totalPriceLabel.grid(row=0, column=0)
totalPriceEntry = Entry(billMenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
totalPriceEntry.grid(row=0, column=1, pady=6, padx=10)

taxLabel = Label(billMenuFrame, text='Tax',font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE, width=5)
taxLabel.grid(row=0, column=2)
taxEntry = Entry(billMenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
taxEntry.grid(row=0, column=3, pady=6, padx=10)


#---------------------------Button Frame---------------------------------------------

buttonFrame = Frame(billMenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=1)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bd=5, width=8
                     , command=total)
totalButton.grid(row=0, column=0, padx=15)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bd=5, width=8, command= bill_area)
billButton.grid(row=0, column=1, padx=15)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bd=5, width=8, command = send_email)
emailButton.grid(row=0, column=2, padx=15)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bd=5, width=8, command=print_bill)
printButton.grid(row=0, column=3, padx=15)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bd=5, width=8, command=clear)
clearButton.grid(row=0, column=4, padx=15)

root.mainloop()