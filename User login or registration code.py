# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:23:57 2022
@author: mogith
"""
import os
import pandas as pd
import openpyxl

def registration(email_ID): #function to register user details
    accept_email=True
    emailheader=(email_ID[0:(email_ID.index('@'))]) #checks condition 1 
    if email_ID[0]=='@' :
        accept_email=False
    elif (email_ID.index('.')-email_ID.index('@'))<2: #checks that @ and . is not next to each other
        accept_email=False
    elif (accept_email==True):
        for i in range(len(emailheader)):
            if emailheader[i] in '1234567890':   #checks that email header doesn't contain any numeric values
               accept_email=False
               break
            elif emailheader[i] in '[@_!#$%^&*()<>?/\|}{~:]' : #checks that email header doesn't contain any special characters
                accept_email=False
                break
    if accept_email!=True:  #if all above contions fail 
        print("Enter valid Email address")
    else:
        password=input("enter password:") #getting password input from user once email is verfiied
        accept_pwd=0     #password pointer 
    if (len(password)>=5 or len(password)<=16): #condition 1 checking length of passwd
        accept_pwd+=1
    else:
        print('password length must be min 5 and max 16')
    if (any(map(str.isdigit,password))==True): # checking condition whether passed consists of one integer
        accept_pwd+=1
    else:
        print("Password must have atleast one integer")
    if accept_pwd>1: #condition 3 password consists of atleast one upper case and lowercase letter
        uppercount=0 #counter for caps letter 
        lowercount=0 #counter for small letter
        for i in password: #checks whether password has atleast one capital letter
            if i.isupper():
                uppercount+=1
                break
        else:
              print("Password must have one capital letter")
        for i in password: #checks whether password has atleast one small letter
            if i.islower():
                lowercount+=1
                break
        else:
              print("Password must have one small letter")      
        if uppercount>=1 and lowercount>=1: 
          accept_pwd+=1
    if accept_pwd>2: # condition 4 executes only when above conditions met
        for i in range(len(password)):
            if password[i] in '[@_!#$%^&*()<>?/\|}{~:]':
                accept_pwd+=1
   
    if accept_pwd>3: #return value only when all 4 conditions met 
        return(email_ID,password) #returns as a tuple

log_or_reg=input("Login or Registration(press '1' for register '2' for login):") # Asking user whether login or registration
if log_or_reg =='1':  #validating user choice 
    email=input('enter email address to register:') #if user chooses reg it will trigger registration function
    details=(registration(email)) #store the value as a tuple
    wb = openpyxl.load_workbook("./Userdatabase.xlsx") #loading user database file stored in local system
    sh = wb['Sheet1']  #prompting to sheet1
    sh.append(details) #Append the details extracted from registration function into existing excel file
    wb.save("./Userdatabase.xlsx") #saves and updates the file
else:  # if user chooses other option - for login
     Emaillogin=input('enter email for logging in:')  
     passwdlogin=input('enter password for logging in:')
     Df=pd.read_excel('./Userdatabase.xlsx')        #reads the excel file as dataframe
     Df_to_dict = Df.set_index('email_ID').T.to_dict() #converts the each row value as a dictionary with index as email_ID
     if(( Df_to_dict[Emaillogin]['password'])==passwdlogin ): #If the user entered details is successful (password matches the emailid)
         print('login successful') 
     else:
         print('Email_id and password do not exists')
         nextattempt=input('For Registration: press 1/forget_password: press 2') #to prompt to registration again or to get the password from file
         if nextattempt==1:
             newreg=input("enter new email_id to register:") # registration process
             newdetails=registration(newreg)
             wb = openpyxl.load_workbook("./Userdatabase.xlsx")
             sh = wb['Sheet1']
             sh.append(details)
             wb.save("./Userdatabase.xlsx")
         elif nextattempt==2:    #else this will retrieve the password for corresponding email_id
             print("Password for your account is:" ,Df_to_dict[Emaillogin]['password'])
   
         
        
    
                
        
        

            
        
        
               

