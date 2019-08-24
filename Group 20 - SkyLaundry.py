######################################
#        Author, Group 20            #
#       Nishat, Jordan Dunn          #
#   Amine Bahlouli, Jonathon Hunte   #
######################################

from tkinter import *
from tkinter import messagebox

class Welcome:
    def __init__(self,master):

        self.master=master
        self.master.geometry('300x270')
        self.master.title('WELCOME')

        print("")
        print("---------------SERVICE CHARGES------------------")
        print("      DELIVERY     LOCKER     RIDERS      BAGS")
        print(" MON   £10.00      £15.00     £4.20     £5.00/Kg")
        print(" TUE   £10.00      £15.00     £4.20     £5.00/Kg")
        print(" WED   £10.00      £15.00     £4.20     £5.00/Kg")
        print(" THRS  £10.00      £15.00     £4.20     £5.00/Kg")
        print(" FRI   £12.00      £17.00     £6.20     £5.00/Kg")
        print(" SAT   £15.00      £20.00     £7.40     £7.00/Kg")
        print(" SUN   £15.00      £20.00     £7.40     £7.00/Kg")
        print("------------------------------------------------")
        print("")
        print("please note: minimum number of bags are accepted 2!")
        print("please note: minimum number of bags per Kg are accepted 10kg!")
        print("")
              
        self.label1=Label(self.master,text='**WELCOME TO SKYLAUNDRY**',fg='blue')
        self.label1.pack()
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button1=Button(self.master,text='LOG-IN CUSTOMER',command=self.gotoCustomer)
        self.button1.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button2=Button(self.master,text='LOG-IN DELIVERY',command=self.gotoDelivery)
        self.button2.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button3=Button(self.master,text=' LOG-IN LOCKER ',command=self.gotoLocker)
        self.button3.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button4=Button(self.master,text=' LOG-IN ADMIN  ',command=self.gotoAdmin)
        self.button4.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button5=Button(self.master,text=' LOG-IN PAYROLL/BILLING',command=self.gotoPayment)
        self.button5.pack(side=TOP)
        

    def gotoCustomer(self):

        stringVar = StringVar()
        text = Text()
        text2 = Text()
        root2=Toplevel(self.master)
        myGUI=Customer(root2,stringVar, text, text2)

    def gotoDelivery(self):

        stringVar = StringVar()
        root2=Toplevel(self.master)
        myGUI=Delivery(root2,stringVar)

    def gotoLocker(self):

        stringVar = StringVar()
        text = Text()
        text2 = Text()
        root2=Toplevel(self.master)
        myGUI=Locker(root2,stringVar,text, text2)

    def gotoAdmin(self):

        stringVar = StringVar()
        root2=Toplevel(self.master)
        myGUI=Admin(root2,stringVar)

    def gotoPayment(self):

        stringVar = StringVar()
        root2=Toplevel(self.master)
        myGUI=Payment(root2,stringVar)


class Customer:
    def __init__(self,master, stringVar, text, text2):

        self.master=master
        self.master.geometry('300x270')

        self.stringVar1 = StringVar()
        self.stringVar2 = StringVar()
        self.stringVar3 = StringVar()
        self.stringVar4 = StringVar()
        self.stringVar5 = StringVar()
    
        self.label1=Label(self.master,text='SKYLAUNDRY CUSTOMER MENU',fg='blue')
        self.label1.pack()
        self.label1=Label(self.master,text='Full Name: ',fg='black')
        self.label1.pack(side=TOP)
        self.entry1=Entry(self.master,textvariable=self.stringVar1,width=21)
        self.entry1.pack(side=TOP)
        self.label2=Label(self.master,text='Last Name: ',fg='black')
        self.label2.pack(side=TOP)
        self.entry2=Entry(self.master,textvariable=self.stringVar2,width=21)
        self.entry2.pack(side=TOP)
        self.label3=Label(self.master,text='Address: ',fg='black')
        self.label3.pack(side=TOP)
        self.entry3=Entry(self.master,textvariable=self.stringVar3,width=21)
        self.entry3.pack(side=TOP)
        self.label4=Label(self.master,text='Number of bags: ',fg='black')
        self.label4.pack(side=TOP)
        self.vcmd =(self.master.register(self.validate_entry), "%P")
        self.entry4=Entry(self.master,validate = "key",textvariable=self.stringVar4, validatecommand=self.vcmd,width=21)
        self.entry4.pack(side=TOP)
        self.label5=Label(self.master,text='Number of bags per Kg: ',fg='black')
        self.label5.pack(side=TOP)
        self.vcmd2 =(self.master.register(self.validate_entry2), '%P')
        self.entry5=Entry(self.master,validate = "key",textvariable=self.stringVar5, validatecommand=self.vcmd2,width=21)
        self.entry5.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button1=Button(self.master,text='NEW ORDER',command=self.save)
        self.button1.pack(side=RIGHT)
        self.button2=Button(self.master,text='VIEW MY ORDER',command=self.myorder)
        self.button2.pack(side=RIGHT)


    def save(self):

        file = open('New_HomeDelivery_Customer.txt','w')
        file.write('Customer First Name: '+self.stringVar1.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar2.get()+'\n')
        file.write('Customer Address: '+self.stringVar3.get()+'\n')
        file.write('Number of bags: '+self.stringVar4.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar5.get()+'\n')
        messagebox.showinfo("Successfully submited","Thanks for your order. We will now process your order in 24 hours.")      

    def myorder(self):

        file = open('Delivery Customer Number.txt','r')
        print(file.read())

    def validate_entry(self,text):
        if text =="": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 2 <= value <= 5

    def validate_entry2(self,text2):
        if text2 =="": return True
        try:
            value = int(text2)
        except ValueError:
            return False
        return 1 < value < 60

class Delivery:
    def __init__(self,master,stringVar):

        self.master=master
        self.master.geometry('300x295')

        self.stringVar11 = StringVar()
        self.stringVar12 = StringVar()
        self.stringVar13 = StringVar()
        self.stringVar14 = StringVar()
        self.stringVar15 = StringVar()
        
        self.label1=Label(self.master,text='SKYLAUNDRY DELIVERY MENU',fg='blue')
        self.label1.pack()
        self.label4=Label(self.master,text='Order Number: ',fg='black')
        self.label4.pack(side=TOP)
        self.entry4=Entry(self.master,textvariable=self.stringVar11,width=30)
        self.entry4.pack(side=TOP)
        self.label9=Label(self.master,text='Locker Number: ',fg='black')
        self.label9.pack(side=TOP)
        self.entry9=Entry(self.master,textvariable=self.stringVar14,width=30)
        self.entry9.pack(side=TOP)
        self.label5=Label(self.master,text='Delivered: ',fg='black')
        self.label5.pack(side=TOP)
        self.entry5=Entry(self.master,textvariable=self.stringVar12,width=30)
        self.entry5.pack(side=TOP)
        self.label6=Label(self.master,text='Dispatched: ',fg='black')
        self.label6.pack(side=TOP)
        self.entry6=Entry(self.master,textvariable=self.stringVar13,width=30)
        self.entry6.pack(side=TOP)
        self.label8=Label(self.master,text='Driver Number: ',fg='black')
        self.label8.pack(side=TOP)
        self.entry8=Entry(self.master,textvariable=self.stringVar15,width=30)
        self.entry8.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button2=Button(self.master,text='VIEW DELIVERY',command=self.viewdelivery)
        self.button2.pack(side=RIGHT)
        self.button3=Button(self.master,text='DISPATCH',command=self.dispatch)
        self.button3.pack(side=RIGHT)
        self.button4=Button(self.master,text='DELIVER',command=self.deliver)
        self.button4.pack(side=RIGHT)

    def viewdelivery(self):

        file = open ('Delivery Order Number.txt','r')
        print (file.read())

        file = open ('Locker Order Number.txt','r')
        print (file.read())  

    def dispatch(self):

        file = open ('Order Dispatch.txt','a')
        file.write('Driver Number: '+self.stringVar15.get()+'\n')
        file.write('Order Number: '+self.stringVar11.get()+'\n')
        file.write('Locker Number: '+self.stringVar14.get()+'\n')
        file.write('Order Dispatch: '+self.stringVar13.get()+'\n')
        file.write('----------------------'+'\n')
        messagebox.showinfo("Successfully submited","Done!")

    def deliver(self):

        file = open ('Order Delivered.txt','a')
        file.write('Driver Number: '+self.stringVar15.get()+'\n')
        file.write('Order Number: '+self.stringVar11.get()+'\n')
        file.write('Locker Number: '+self.stringVar14.get()+'\n')
        file.write('Order Delivered: '+self.stringVar12.get()+'\n')
        file.write('----------------------'+'\n')
        messagebox.showinfo("Successfully submited","Done!")
        

class Locker:
    def __init__(self,master,stringVar, text, text2):

        self.master=master
        self.master.geometry('300x310')

        self.stringVar80 = StringVar()
        self.stringVar81 = StringVar()
        self.stringVar82 = StringVar()
        self.stringVar83 = StringVar()
        self.stringVar84 = StringVar()
        self.stringVar85 = StringVar()

        self.label1=Label(self.master,text='SKYLAUNDRY LOCKER MENU',fg='blue')
        self.label1.pack()
        self.label1=Label(self.master,text='First Name: ',fg='black')
        self.label1.pack(side=TOP)
        self.entry1=Entry(self.master,textvariable=self.stringVar80,width=21)
        self.entry1.pack(side=TOP)
        self.label2=Label(self.master,text='Last Name: ',fg='black')
        self.label2.pack(side=TOP)
        self.entry2=Entry(self.master,textvariable=self.stringVar81,width=21)
        self.entry2.pack(side=TOP)
        self.label6=Label(self.master,text='Customer Address: ',fg='black')
        self.label6.pack(side=TOP)
        self.entry7=Entry(self.master,textvariable=self.stringVar82,width=21)
        self.entry7.pack(side=TOP)
        self.label4=Label(self.master,text='Number of bags: ',fg='black')
        self.label4.pack(side=TOP)
        self.vcmd =(self.master.register(self.validate_entry), "%P")
        self.entry4=Entry(self.master,validate = "key", textvariable=self.stringVar83,validatecommand=self.vcmd,width=21)
        self.entry4.pack(side=TOP)
        self.label6=Label(self.master,text='Number of bags per Kg: ',fg='black')
        self.label6.pack(side=TOP)
        self.vcmd2 =(self.master.register(self.validate_entry2), '%P')
        self.entry6=Entry(self.master,validate = "key",textvariable=self.stringVar85,validatecommand=self.vcmd2,width=21)
        self.entry6.pack(side=TOP)
        self.label5=Label(self.master,text='Locker Number: ',fg='black')
        self.label5.pack(side=TOP)
        self.entry5=Entry(self.master,textvariable=self.stringVar84,width=21)
        self.entry5.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button1=Button(self.master,text='NEW ORDER',command=self.savelocker)
        self.button1.pack(side=RIGHT)
        self.button2=Button(self.master,text='VIEW ORDER',command=self.myorder)
        self.button2.pack(side=RIGHT)

    def savelocker(self):
        file = open('New_Locker_Customer.txt','w')
        file.write('Customer First Name: '+self.stringVar80.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar81.get()+'\n')
        file.write('Customer Address: '+self.stringVar82.get()+'\n')
        file.write('Number of bags: '+self.stringVar83.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar85.get()+'\n')
        file.write('Locker Number: '+self.stringVar84.get()+'\n')
        messagebox.showinfo("Successfully submited","Thanks for you order. We will now process your order in 24 hours.")

    def myorder(self):
        file = open ('Locker Customer Number.txt','r')
        print (file.read())

    def validate_entry(self,text):
        if text =="": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 2 <= value <= 5

    def validate_entry2(self,text2):
        if text2 =="": return True
        try:
            value = int(text2)
        except ValueError:
            return False
        return 1 < value < 60

class Admin:
    def __init__(self,master,stringVar):

        self.master=master
        self.master.geometry('540x450')
        
        self.stringVar5 = StringVar()
        self.stringVar6 = StringVar()
        self.stringVar7 = StringVar()
        self.stringVar8 = StringVar()
        self.stringVar9 = StringVar()
        self.stringVar10 = StringVar()
        self.stringVar24 = StringVar()
        self.stringVar26 = StringVar()
        self.stringVar27 = StringVar()

        self.label1=Label(self.master,text='SKYLAUNDRY ADMIN MENU',fg='blue')
        self.label1.pack()
        self.label1=Label(self.master,text='Full Name: ',fg='black')
        self.label1.pack(side=TOP)
        self.entry1=Entry(self.master,textvariable=self.stringVar7,width=30)
        self.entry1.pack(side=TOP)
        self.label2=Label(self.master,text='Last Name: ',fg='black')
        self.label2.pack(side=TOP)
        self.entry2=Entry(self.master,textvariable=self.stringVar8,width=30)
        self.entry2.pack(side=TOP)
        self.label3=Label(self.master,text='Address: ',fg='black')
        self.label3.pack(side=TOP)
        self.entry3=Entry(self.master,textvariable=self.stringVar9,width=30)
        self.entry3.pack(side=TOP)
        self.label4=Label(self.master,text='Number of bags: ',fg='black')
        self.label4.pack(side=TOP)
        self.entry4=Entry(self.master,textvariable=self.stringVar10,width=30)
        self.entry4.pack(side=TOP)
        self.label34=Label(self.master,text='Number of bags per Kg: ',fg='black')
        self.label34.pack(side=TOP)
        self.entry34=Entry(self.master,textvariable=self.stringVar27,width=30)
        self.entry34.pack(side=TOP)
        self.label5=Label(self.master,text='Customer Number: ',fg='black')
        self.label5.pack(side=TOP)
        self.entry5=Entry(self.master,textvariable=self.stringVar5,width=30)
        self.entry5.pack(side=TOP)
        self.label9=Label(self.master,text='Locker Number: ',fg='black')
        self.label9.pack(side=TOP)
        self.entry9=Entry(self.master,textvariable=self.stringVar24,width=30)
        self.entry9.pack(side=TOP)
        self.label6=Label(self.master,text='Order Number: ',fg='black')
        self.label6.pack(side=TOP)
        self.entry6=Entry(self.master,textvariable=self.stringVar6,width=30)
        self.entry6.pack(side=TOP)
        self.label8=Label(self.master,text='Order Date: ',fg='black')
        self.label8.pack(side=TOP)
        self.entry8=Entry(self.master,textvariable=self.stringVar26,width=30)
        self.entry8.pack(side=TOP)
        self.label1=Label(self.master,text='')
        self.label1.pack()
        self.button1=Button(self.master,text='VIEW CUSTOMER',command=self.viewcustomer)
        self.button1.pack(side=LEFT)
        self.button2=Button(self.master,text='VIEW DELIVERY',command=self.viewdelivery)
        self.button2.pack(side=RIGHT)
        self.button3=Button(self.master,text='VIEW DISPATCH',command=self.viewdispatch)
        self.button3.pack(side=RIGHT)
        self.button4=Button(self.master,text='NEW DELIVERY ORDER',command=self.neworder)
        self.button4.pack(side=LEFT)
        self.button5=Button(self.master,text='NEW LOCKER ORDER',command=self.newlockerorder)
        self.button5.pack(side=LEFT)

    def viewcustomer(self):

        file = open('New_HomeDelivery_Customer.txt','r')
        print(file.read())

        file = open('New_Locker_Customer.txt','r')
        print(file.read())

    def viewdelivery(self):

        file = open('Order Delivered.txt','r')
        print(file.read())

    def viewdispatch(self):

        file = open('Order Dispatch.txt','r')
        print(file.read())

    def neworder(self):
        file = open('Delivery Customer Number.txt','w')
        file.write('Customer Number: '+self.stringVar5.get()+'\n')
        file.write('Customer First Name: '+self.stringVar7.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar8.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar27.get()+'\n')
        file.write('Order Date: '+self.stringVar26.get()+'\n')
        file.write('----------------'+'\n')

        file = open('Delivery Customer Info.txt','a')
        file.write('Customer Number: '+self.stringVar5.get()+'\n')
        file.write('Customer First Name: '+self.stringVar7.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar8.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar27.get()+'\n')
        file.write('Order Date: '+self.stringVar26.get()+'\n')
        file.write('----------------'+'\n')

        file = open('Delivery Order Number.txt','w')
        file.write('Order Number: '+self.stringVar6.get()+'\n')
        file.write('Locker Number: '+self.stringVar24.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        messagebox.showinfo("Successfully submited","New Order has now been successfully created!")

    def newlockerorder(self):
        file = open('Locker Customer Number.txt','w')
        file.write('Customer Number: '+self.stringVar5.get()+'\n')
        file.write('Locker Number: '+self.stringVar24.get()+'\n')
        file.write('Customer First Name: '+self.stringVar7.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar8.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar27.get()+'\n')
        file.write('Order Date: '+self.stringVar26.get()+'\n')
        file.write('----------------'+'\n')

        file = open('Locker Customer Info.txt','a')
        file.write('Customer Number: '+self.stringVar5.get()+'\n')
        file.write('Locker Number: '+self.stringVar24.get()+'\n')
        file.write('Customer First Name: '+self.stringVar7.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar8.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        file.write('Number of bags per Kg: '+self.stringVar27.get()+'\n')
        file.write('Order Date: '+self.stringVar26.get()+'\n')
        file.write('----------------'+'\n')

        file = open('Locker Order Number.txt','w')
        file.write('Order Number: '+self.stringVar6.get()+'\n')
        file.write('Locker Number: '+self.stringVar24.get()+'\n')
        file.write('Customer Address: '+self.stringVar9.get()+'\n')
        file.write('Number of bags: '+self.stringVar10.get()+'\n')
        messagebox.showinfo("Successfully submited","New Order has now been successfully created!")


class Payment:
    def __init__(self,master,stringVar):

        self.stringVar55 = StringVar()
        self.stringVar66 = StringVar()
        self.stringVar77 = StringVar()
        self.stringVar88 = StringVar()
        self.stringVar99= StringVar()
        self.stringVar100 = StringVar()
        self.stringVar200 = StringVar()
        self.stringVar300 = StringVar()
        self.stringVar400 = StringVar()
        self.textinput = StringVar()
       
    
        self.master=master
        self.master.geometry('368x455')

        self.label1=Label(self.master,text='SKYLAUNDRY PAYROLL/BILLING MENU',fg='blue')
        self.label1.pack()
        self.label1=Label(self.master,text='Customer Number:')
        self.label1.pack()
        self.entry1=Entry(self.master,textvariable=self.stringVar55,width=30)
        self.entry1.pack(side=TOP)
        self.label2=Label(self.master,text='Order Number:')
        self.label2.pack()
        self.entry2=Entry(self.master,textvariable=self.stringVar66,width=30)
        self.entry2.pack(side=TOP)
        self.label3=Label(self.master,text='Customer Name:')
        self.label3.pack()
        self.entry3=Entry(self.master,textvariable=self.stringVar77,width=30)
        self.entry3.pack(side=TOP)
        self.label4=Label(self.master,text='Customer Address:')
        self.label4.pack()
        self.entry4=Entry(self.master,textvariable=self.stringVar88,width=30)
        self.entry4.pack(side=TOP)
        self.label5=Label(self.master,text='Number of bags:')
        self.label5.pack()
        self.entry5=Entry(self.master,textvariable=self.stringVar99,width=30)
        self.entry5.pack(side=TOP)
        self.label6=Label(self.master,text='Number of bags per Kg:')
        self.label6.pack()
        self.entry6=Entry(self.master,textvariable=self.stringVar100,width=30)
        self.entry6.pack(side=TOP)
        self.label7=Label(self.master,text='Price per bags:')
        self.label7.pack()
        self.entry7=Entry(self.master,textvariable=self.stringVar400,width=30)
        self.entry7.pack(side=TOP)
        self.label9=Label(self.master,text='Cost per trip:')
        self.label9.pack()
        self.entry9=Entry(self.master,textvariable=self.stringVar200,width=30)
        self.entry9.pack(side=TOP)
        self.label10=Label(self.master,text='Number of trips:')
        self.label10.pack()
        self.entry10=Entry(self.master,textvariable=self.stringVar300,width=30)
        self.entry10.pack(side=TOP)
        self.label8=Label(self.master,text='Total Price:')
        self.label8.pack()
        self.entry8=Entry(self.master,textvariable=self.textinput,width=30)
        self.entry8.pack(side=TOP)
        self.button1=Button(self.master,text='VIEW DELIVERY',command=self.viewdelivery2)
        self.button1.pack(side=RIGHT)
        self.button2=Button(self.master,text='CREATE BILL',command=self.bill)
        self.button2.pack(side=RIGHT)
        self.button3=Button(self.master,text='PAY DRIVER',command=self.paydriver)
        self.button3.pack(side=RIGHT)


    def viewdelivery2(self):

        file = open('Locker Customer Info.txt','r')
        print(file.read())

        file = open('Delivery Customer Info.txt','r')
        print(file.read())

        file = open('Order Delivered.txt','r')
        print(file.read())

        file = open('Order Dispatch.txt','r')
        print(file.read())

    def bill(self):

        result = float(self.entry5.get()) * float(self.entry7.get())
        results = str(result)
        self.textinput.set(results)

        file = open('Customer Billing.txt','a')
        file.write('Customer Number: '+self.stringVar55.get()+'\n')
        file.write('Locker Number: '+self.stringVar66.get()+'\n')
        file.write('Customer First Name: '+self.stringVar77.get()+'\n')
        file.write('Customer Last Name: '+self.stringVar88.get()+'\n')
        file.write('Customer Address: '+self.stringVar99.get()+'\n')
        file.write('Number of bags: '+self.stringVar100.get()+'\n')
        file.write('Total Price: £'+self.textinput.get()+'\n')
        file.write("-----------------"+"\n")
        messagebox.showinfo("Message","New bill has been geerated and sent to customer!")

    def paydriver(self):

        result = float(self.entry9.get()) * float(self.entry10.get())
        results = str(result)
        self.textinput.set(results)
        
        file = open('Driver Paymets.txt','a')
        file.write('Driver Number: '+self.stringVar55.get()+'\n')
        file.write('Cost per trip: '+self.stringVar99.get()+'\n')
        file.write('Number of trips: '+self.stringVar100.get()+'\n')
        file.write('Net Pay: £'+self.textinput.get()+'\n')
        file.write("-----------------"+"\n")
        messagebox.showinfo("Message","New paysleep has been generate and sent to driver!")
        

def main():

    root=Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

if __name__== '__main__':
    main()
