#!/usr/bin/env python
# coding: utf-8

# ## Product Details
# 1. Product Id
# 2. Product Name
# 3. Product Price
# 4. Product Quantity

# In[ ]:


#for current date time
import time as ts

# read the data from inventery
fd=open ("D:\\Python_Data_Analysis\\GFG_Course\\User_Inventery_Project\\Inventery.txt",'r')
products=fd.read().split('\n')
fd.close()

# User defined data

ui_name=input("Enter your Name :")
ui_phone=input("Enter Your Phone No :")
ui_mail=input("Enter Your mail Id :")
ui_prod_id=input("Enter the Product Id :")
ui_prod_qn=input("Enter the Quantity :")

product_update=[]

for product in products :
        
        product_details = product.split(',')
        
        if(product_details[0] ==ui_prod_id):
        # check with user defined id
            if(int(product_details[3])>= int(ui_prod_qn)):
            # check quantity it's available or not as per user given quantity
              print("==========================")
              print("Product Name :",product_details[1])
              print("Price :",product_details[2])
              print("Quantity :",ui_prod_qn)
              print("===========================")
              print("Amount Billing :",int(ui_prod_qn)*int(product_details[2]))
              print("===========================")
                
              product_details[3]=str(int(product_details[3])-int(ui_prod_qn))
              # update inventery
              fs=open("D:\\Python_Data_Analysis\\GFG_Course\\User_Inventery_Project\\Sales.txt",'a')
              details= ui_name+","+ui_phone+","+ui_mail+","+product_details[1]+","+ui_prod_id+","+ui_prod_qn+","+str(int(ui_prod_qn)*int(product_details[2]))+","+ts.ctime()+"\n"
              fs.write(details)
              # write sales data
              fs.close()
            else:
            # if user given quanity not present 
                print("Sorry, we're not having enough quentity.")
                print("We're having only ",product_details[3]," Quentity.")
                print("Would you like to purchase it ?")
                ch=input("Press Y/N :")

                if(ch=='Y' or ch=='y'):
                # if user wants to purchase remaining products
                  print("==========================")
                  print("Product Name :",product_details[1])
                  print("Price :",product_details[2])
                  print("Quantity :",product_details[3])
                  print("===========================")
                  print("Amount Billing :",int(product_details[3])*int(product_details[2]))
                  print("===========================")
    
                  fs=open("D:\\Python_Data_Analysis\\GFG_Course\\User_Inventery_Project\\Sales.txt",'a')
                  details= ui_name+","+ui_phone+","+ui_mail+","+product_details[1]+","+ui_prod_id+","+product_details[3]+","+str(int(product_details[3])*int(product_details[2]))+","+ts.ctime()+"\n"
                  fs.write(details)
                  fs.close()
                  
                  product_details[3]="0"
                  # update inventery
                else:
                    print("Thanks")
                    
        product_update.append(product_details)
        #update my inventery
        
lst=[]
for pu in product_update :
    pr= pu[0]+","+pu[1]+","+pu[2]+","+pu[3]+"\n"
    lst.append(pr)
lst[-1]=lst[-1][:-1]

fw= open ("D:\\Python_Data_Analysis\\GFG_Course\\User_Inventery_Project\\Inventery.txt",'w')

for i in lst :
    fw.write(i)
fw.close()
print("Inventery Update")        


# In[ ]:




