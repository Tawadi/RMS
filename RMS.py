#!/usr/bin/env python
# coding: utf-8

# In[2]:


#RMS
class rms:

    def __init__(self,resturant_name,resturant_menu):
        self.user_bill=0
        self.name=resturant_name
        self.menu=resturant_menu
        self.user_order=''
        self.user_pay=0
        self.user_rep=''
        

    def welcome_user(self):
        #Welcome User
        print('Welcome to ',self.name)

    def display_menu(self):
        #Display Menu
        print('Menu:')
        for i in self.menu:
            print(i.title(),self.menu[i])

    def take_order(self):
        #Take Order
        self.user_order=input('Please place your order here:')

    def preparing_order(self):
        #Prepare Order
        print('Preparing your',self.user_order)
        import time
        time.sleep(1)
        self.user_bill=self.user_bill+self.menu[self.user_order.lower()]

    def serve_order(self):
        #Serve Order
        print('Your order is ready')
        print('Please enjoy your',self.user_order)

    def display_bill(self):
        #Display Bill

        print('Total Bill:',self.user_bill)

    def verify_payment(self):
        self.user_pay=int(input("please pay your bill here:"))
        while self.user_pay<self.user_bill:
            print("unsuccessfull payment")
            self.user_bill=self.user_bill-self.user_pay
            print("please pay your remaining payment:",self.user_bill)
            self.user_pay=int(input("Please pay your bill here"))
        if self.user_pay>self.user_bill:
            print("Payment successfull")
            print("take your remaining change:",self.user_pay-self.user_bill)
        else:
            print("payment Successfull!")


    def thank_user(self):
        #Thank User
        print('Thank you for visiting',self.name)


    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.user_rep=input('Do you want to order anything else?')
            while self.user_rep.lower()=='yes':
                self.repeat_order()
                self.user_rep=input('Do you want to order anything else?')
            self.display_bill()
            self.verify_payment()
            self.thank_user()
        else:
            print('Invalid Order')
            self.order_process()

    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid Order')
            self.repeat_order()


# In[ ]:


if __name__ == "__main__":
    hot_rm={'cold coffee':200,'latte':190,'drip coffee':180,'cappuccino':190,'frappe':200}
    hot_rn="HOT CAFE"

    hot_rest=rms(hot_rn,hot_rm)

    #hot_rest.welcome_user()
    #hot_rest.order_process()
    import tkinter as tk

    window=tk.Tk()

    tk.Label(window,text="HOT CAFE",font=("helvetica",18)).place(x=40,y=50)

    tk.Button(window,text="START",command=hot_rest.order_process).place(x=80,y=115)

    window.mainloop()


# In[ ]:





# In[ ]:




