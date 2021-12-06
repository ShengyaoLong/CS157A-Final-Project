from tkinter import *
import tkinter
import backend1
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
        e7.delete(0,END)
        e7.insert(END,selected_tuple[7])
    except IndexError:
        pass
def manufacturer_command():
    def get_selected_row4(event):
        try:
            global selected_tuple4
            index=list14.curselection()[0]
            selected_tuple4=list14.get(index)
            e14.delete(0,END)
            e14.insert(END,selected_tuple4[1])
            e24.delete(0,END)
            e24.insert(END,selected_tuple4[2])
            e34.delete(0,END)
            e34.insert(END,selected_tuple4[3])
            e44.delete(0,END)
            e44.insert(END,selected_tuple4[4])
            e54.delete(0,END)
            e54.insert(END,selected_tuple4[5])
        except IndexError:
            pass
    def view4_command():
        list14.delete(0,END)
        for row in backend1.view5():
            list14.insert(END,row)
    def search4_command():
        list14.delete(0,END)
        for row in backend1.search4(manufacturerName_text.get(),streetAddress_text.get(),city_text.get(),state_text.get(),zipCode_text.get()):
            list14.insert(END,row)

    def add4_command():
        backend1.insert4(manufacturerName_text.get(),streetAddress_text.get(),city_text.get(),state_text.get(),zipCode_text.get())
        list14.delete(0,END)
        list14.insert(END,manufacturerName_text.get(),streetAddress_text.get(),city_text.get(),state_text.get(),zipCode_text.get())

    def delete4_command():
        backend1.delete4(selected_tuple4[0])

    def update4_command():
        backend1.update4(selected_tuple4[0],manufacturerName_text.get(),streetAddress_text.get(),city_text.get(),state_text.get(),zipCode_text.get())
    window4=tkinter.Toplevel(window)
    window4.wm_title("Manufacturers")

    l14 = Label(window4,text="manufacturerName")
    l14.grid(row=0,column=0)

    l24 = Label(window4,text="streetAddress")
    l24.grid(row=0,column=2)

    l34 = Label(window4,text="city")
    l34.grid(row=1,column=0)

    l44 = Label(window4,text="state")
    l44.grid(row=1,column=2)

    l54 = Label(window4,text="zipCode")
    l54.grid(row=2,column=0)

    manufacturerName_text=StringVar()
    e14=Entry(window4,textvariable=manufacturerName_text)
    e14.grid(row=0,column=1)

    streetAddress_text=StringVar()
    e24=Entry(window4,textvariable=streetAddress_text)
    e24.grid(row=0,column=3)

    city_text=StringVar()
    e34=Entry(window4,textvariable=city_text)
    e34.grid(row=1,column=1)

    state_text=StringVar()
    e44=Entry(window4,textvariable=state_text)
    e44.grid(row=1,column=3)

    zipCode_text=StringVar()
    e54=Entry(window4,textvariable=zipCode_text)
    e54.grid(row=2,column=1)

    list14=Listbox(window4,height=6,width=35)
    list14.grid(row=4,column=0,rowspan=6,columnspan=2)

    sb14=Scrollbar(window4)
    sb14.grid(row=4,column=2)

    list14.configure(yscrollcommand=sb14.set)
    sb14.configure(command=list14.yview)

    list14.bind('<<ListboxSelect>>',get_selected_row4)

    b13=Button(window4,text="View all", width=13,command=view4_command)
    b13.grid(row=4,column=3)

    b23=Button(window4,text="Search entry", width=13,command=search4_command)
    b23.grid(row=5,column=3)

    b33=Button(window4,text="Add entry", width=13,command=add4_command)
    b33.grid(row=6,column=3)

    b43=Button(window4,text="Update selected", width=13,command=update4_command)
    b43.grid(row=7,column=3)

    b53=Button(window4,text="Delete selected", width=13,command=delete4_command)
    b53.grid(row=8,column=3)

    b63=Button(window4,text="Close", width=13, command=window4.destroy)
    b63.grid(row=9,column=3)
def order_command():
    def get_selected_row3(event):
        try:
            global selected_tuple3
            index=list13.curselection()[0]
            selected_tuple3=list13.get(index)
            e13.delete(0,END)
            e13.insert(END,selected_tuple3[1])
            e23.delete(0,END)
            e23.insert(END,selected_tuple3[2])
            e33.delete(0,END)
            e33.insert(END,selected_tuple3[3])
            e43.delete(0,END)
            e43.insert(END,selected_tuple3[4])
        except IndexError:
            pass
    def view3_command():
        list13.delete(0,END)
        for row in backend1.view4():
            list13.insert(END,row)
    def search3_command():
        list13.delete(0,END)
        for row in backend1.search3(orderNumber_text.get(),customerID_text.get(),totalPrice_text.get(),orderDate_text.get()):
            list13.insert(END,row)

    def add3_command():
        backend1.insert3(orderNumber_text.get(),customerID_text.get(),totalPrice_text.get(),orderDate_text.get())
        list13.delete(0,END)
        list13.insert(END,orderNumber_text.get(),customerID_text.get(),totalPrice_text.get(),orderDate_text.get())

    def delete3_command():
        backend1.delete3(selected_tuple3[0])

    def update3_command():
        backend1.update3(selected_tuple3[0],orderNumber_text.get(),customerID_text.get(),totalPrice_text.get(),orderDate_text.get())
    window3=tkinter.Toplevel(window)
    window3.wm_title("Orders")
    l13 = Label(window3,text="orderNumber")
    l13.grid(row=0,column=0)

    l23 = Label(window3,text="customerID")
    l23.grid(row=0,column=2)

    l33 = Label(window3,text="totalPrice")
    l33.grid(row=1,column=0)

    l43 = Label(window3,text="orderDate")
    l43.grid(row=1,column=2)

    orderNumber_text=StringVar()
    e13=Entry(window3,textvariable=orderNumber_text)
    e13.grid(row=0,column=1)

    customerID_text=StringVar()
    e23=Entry(window3,textvariable=customerID_text)
    e23.grid(row=0,column=3)

    totalPrice_text=StringVar()
    e33=Entry(window3,textvariable=totalPrice_text)
    e33.grid(row=1,column=1)

    orderDate_text=StringVar()
    e43=Entry(window3,textvariable=orderDate_text)
    e43.grid(row=1,column=3)

    list13=Listbox(window3,height=6,width=35)
    list13.grid(row=4,column=0,rowspan=6,columnspan=2)

    sb13=Scrollbar(window3)
    sb13.grid(row=4,column=2)

    list13.configure(yscrollcommand=sb13.set)
    sb13.configure(command=list13.yview)

    list13.bind('<<ListboxSelect>>',get_selected_row3)

    b13=Button(window3,text="View all", width=13,command=view3_command)
    b13.grid(row=4,column=3)

    b23=Button(window3,text="Search entry", width=13,command=search3_command)
    b23.grid(row=5,column=3)

    b33=Button(window3,text="Add entry", width=13,command=add3_command)
    b33.grid(row=6,column=3)

    b43=Button(window3,text="Update selected", width=13,command=update3_command)
    b43.grid(row=7,column=3)

    b53=Button(window3,text="Delete selected", width=13,command=delete3_command)
    b53.grid(row=8,column=3)

    b63=Button(window3,text="Close", width=13, command=window3.destroy)
    b63.grid(row=9,column=3)

def customer_command():
    def get_selected_row2(event):
        try:
            global selected_tuple2
            index=list12.curselection()[0]
            selected_tuple2=list12.get(index)
            e12.delete(0,END)
            e12.insert(END,selected_tuple2[1])
            e22.delete(0,END)
            e22.insert(END,selected_tuple2[2])
            e32.delete(0,END)
            e32.insert(END,selected_tuple2[3])
            e42.delete(0,END)
            e42.insert(END,selected_tuple2[4])
            e52.delete(0,END)
            e52.insert(END,selected_tuple2[5])
        except IndexError:
            pass
    def view2_command():
        list12.delete(0,END)
        for row in backend1.view3():
            list12.insert(END,row)
    def search2_command():
        list12.delete(0,END)
        for row in backend1.search2(customerName_text.get(),streetAddress_text.get(),city_text.get(),state_text.get(),zipCode_text.get()):
            list12.insert(END,row)

    def add2_command():
        backend1.insert2(customerName_text.get(),streetAddress_text.get(),city_text.get(), state_text.get(),zipCode_text.get())
        list12.delete(0,END)
        list12.insert(END,customerName_text.get(),streetAddress_text.get(),city_text.get(), state_text.get(),zipCode_text.get())

    def delete2_command():
        backend1.delete2(selected_tuple2[0])

    def update2_command():
        backend1.update2(selected_tuple2[0],customerName_text.get(),streetAddress_text.get(),city_text.get(), state_text.get(),zipCode_text.get())
    window2=tkinter.Toplevel(window)
    window2.wm_title("Customers")
    l12 = Label(window2,text="customerName")
    l12.grid(row=0,column=0)

    l22 = Label(window2,text="streetAddress")
    l22.grid(row=0,column=2)

    l32 = Label(window2,text="city")
    l32.grid(row=1,column=0)

    l42 = Label(window2,text="state")
    l42.grid(row=1,column=2)

    l52 = Label(window2,text="zipCode")
    l52.grid(row=2,column=0)

    customerName_text=StringVar()
    e12=Entry(window2,textvariable=customerName_text)
    e12.grid(row=0,column=1)

    streetAddress_text=StringVar()
    e22=Entry(window2,textvariable=streetAddress_text)
    e22.grid(row=0,column=3)

    city_text=StringVar()
    e32=Entry(window2,textvariable=city_text)
    e32.grid(row=1,column=1)

    state_text=StringVar()
    e42=Entry(window2,textvariable=state_text)
    e42.grid(row=1,column=3)

    zipCode_text=StringVar()
    e52=Entry(window2,textvariable=zipCode_text)
    e52.grid(row=2,column=1)

    list12=Listbox(window2,height=6,width=35)
    list12.grid(row=4,column=0,rowspan=6,columnspan=2)

    sb12=Scrollbar(window2)
    sb12.grid(row=4,column=2)

    list12.configure(yscrollcommand=sb12.set)
    sb12.configure(command=list12.yview)

    list12.bind('<<ListboxSelect>>',get_selected_row2)

    b12=Button(window2,text="View all", width=13,command=view2_command)
    b12.grid(row=4,column=3)

    b22=Button(window2,text="Search entry", width=13,command=search2_command)
    b22.grid(row=5,column=3)

    b32=Button(window2,text="Add entry", width=13,command=add2_command)
    b32.grid(row=6,column=3)

    b42=Button(window2,text="Update selected", width=13,command=update2_command)
    b42.grid(row=7,column=3)

    b52=Button(window2,text="Delete selected", width=13,command=delete2_command)
    b52.grid(row=8,column=3)

    b62=Button(window2,text="Close", width=13, command=window2.destroy)
    b62.grid(row=9,column=3)
    b7=Button(window2,text="Add orders", width=13, command=order_command)
    b7.grid(row=9,column=1)
    
def view_command():
    list1.delete(0,END)
    for row in backend1.view():
        list1.insert(END,row)
def view_command2():
    list1.delete(0,END)
    for row in backend1.view2():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend1.search(carVIN_text.get(),editionCode_text.get(),carMake_text.get(), carModel_text.get(),
                                manufacturerID_text.get(),carPrice_text.get(),quantityOnHand_text.get()):
        list1.insert(END,row)

def add_command():
    backend1.insert(carVIN_text.get(),editionCode_text.get(),carMake_text.get(), carModel_text.get(),
                                manufacturerID_text.get(),carPrice_text.get(),quantityOnHand_text.get())
    list1.delete(0,END)
    list1.insert(END,carVIN_text.get(),editionCode_text.get(),carMake_text.get(), carModel_text.get(),
                                manufacturerID_text.get(),carPrice_text.get(),quantityOnHand_text.get())

def delete_command():
    backend1.delete(selected_tuple[0])

def update_command():
    backend1.update(selected_tuple[0],carVIN_text.get(),editionCode_text.get(),carMake_text.get(), carModel_text.get(),
                                manufacturerID_text.get(),carPrice_text.get(),quantityOnHand_text.get())
    
window=Tk()
window.wm_title("Cars")
l1 = Label(window,text="carVIN")
l1.grid(row=0,column=0)

l2 = Label(window,text="editionCode")
l2.grid(row=0,column=2)

l3 = Label(window,text="carMake")
l3.grid(row=1,column=0)

l4 = Label(window,text="carModel")
l4.grid(row=1,column=2)

l5 = Label(window,text="manufacturerID")
l5.grid(row=2,column=0)

l6 = Label(window,text="carPrice")
l6.grid(row=2,column=2)

l7 = Label(window,text="quantityOnHand")
l7.grid(row=3,column=0)

carVIN_text=StringVar()
e1=Entry(window,textvariable=carVIN_text)
e1.grid(row=0,column=1)

editionCode_text=StringVar()
e2=Entry(window,textvariable=editionCode_text)
e2.grid(row=0,column=3)

carMake_text=StringVar()
e3=Entry(window,textvariable=carMake_text)
e3.grid(row=1,column=1)

carModel_text=StringVar()
e4=Entry(window,textvariable=carModel_text)
e4.grid(row=1,column=3)

manufacturerID_text=StringVar()
e5=Entry(window,textvariable=manufacturerID_text)
e5.grid(row=2,column=1)

carPrice_text=StringVar()
e6=Entry(window,textvariable=carPrice_text)
e6.grid(row=2,column=3)

quantityOnHand_text=StringVar()
e7=Entry(window,textvariable=quantityOnHand_text)
e7.grid(row=3,column=1)

list1=Listbox(window,height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=13,command=view_command)
b1.grid(row=4,column=3)

b2=Button(window,text="Search entry", width=13,command=search_command)
b2.grid(row=5,column=3)

b3=Button(window,text="Add entry", width=13,command=add_command)
b3.grid(row=6,column=3)

b4=Button(window,text="Update selected", width=13,command=update_command)
b4.grid(row=7,column=3)

b5=Button(window,text="Delete selected", width=13,command=delete_command)
b5.grid(row=8,column=3)

b6=Button(window,text="Close", width=13, command=window.destroy)
b6.grid(row=9,column=3)

b7=Button(window,text="View Selled Cars", width=13, command=view_command2)
b7.grid(row=9,column=0)
b8=Button(window,text="Add customers", width=13, command=customer_command)
b8.grid(row=9,column=1)
b9=Button(window,text="Add manufacturers", width=15, command=manufacturer_command)
b9.grid(row=9,column=2)
window.mainloop()
