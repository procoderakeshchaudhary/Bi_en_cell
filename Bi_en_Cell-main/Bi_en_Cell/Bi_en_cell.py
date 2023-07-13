def REGISTRATION():
    '''
    The first step to enroll in the Bi en Cell system of IIT ROPAR. We ask the name, entry number, and the password to set up the user's account.
    '''
    import pwinput                                                  # A module for typing secretly (passwords!)
    
    print("REGISTRATION in BI en Cell network IIT ROPAR \n") 
    print("Register to start selling & buying coupons!! \n") 

    
    global entry                                                    # The entry no. is the most important identity of a student 
                                                                    # and hence it is defined GLOBALLY.    
                                                                    
    storage=open('DATAMINE.txt','a')                                # CREATING a Storage file for All the registring users.
    storage.close()
    
    storage=open('DATAMINE.txt','r')                                

    sss = storage.read()
    
    name=input("Name: ")                                            # Asking the Name of the user.
    if name=='':                                                    # ...eliminating invalid names.
        REGISTRATION()

    match_point_1 = sss.find(name)                                  # THESE 
                                                                    #       LINES
    if match_point_1!=-1:                                           #            OF
        print('\n'+ str(name) +" already exists in the DATABASE")   #               CODE checks whether the DATABASE contains this name or not.
        LOGIN()
    
    entry=input("Entry number:  ")                                  # Input of the entry number.
    
    match_point_2 = sss.find(entry)                                 # THESE     
                                                                    #       LINES
                                                                    #           OF
    if match_point_2!=-1:                                           #             CODE checks whether the DATABASE contains this entry id or not.
        print('\n'+ str(entry) +" already exists in the DATABASE")  #
        print('\nPlease try again')                                 #
        REGISTRATION()                                              #
    
    if entry=='':                                                   # eliminating invalid entry numbers.
        REGISTRATION()                                              
    if len(entry)!=11:                                              # eliminating invalid entry numbers.
        print("\nPlease enter a correct entry no.")
        REGISTRATION()
       
    

    CONFIRMATION()

    

    passkey= pwinput.pwinput(prompt="Password: ",mask='*')          # masking the PASSWORD using PWINPUT module.
    
    if passkey=='':                                                 # eliminating invalid passwords 
        REGISTRATION()

    re_passkey= pwinput.pwinput(prompt="Re-enter password: ",mask='*')      # re-entering the password 
    

    if passkey==re_passkey:                                         # Confirming the Re-enter password matches with the original password.
           
        storage=open('DATAMINE.txt','a')                            # ...if it does we can stire the (name+entry+password) into the DATABASE
                                                                    # ...i.e. DATAMINE.txt
        storage.write(name+'-'+entry+'_'+passkey+'\n')          
      
        storage.close()

        print('\n'+25*" "+'Registration Successfull!! \n')
    else:
        print('\nPasswords do not match, Please try again! \n')
        LOGIN()                                               # if the password doesn't match with re-entered password, the program returns
                                                                    # ...to step one: REGISTRATION()



def generate_otp():
    '''
    To generate a 6 Digit OTP.
    '''
    import random                 # One_Time_Password is a random 6 digit code used to verify a user's authenticity.

    s=str()                       # this is empty string which we add otp  
    for i in range(6):              #this loop will generate otp
        x=random.randint(0,9)       #  provide 0 to  9 number as otp in 6 digit
        s=s+str(x)              #  append continues manner
    return s            #return  otp as string


def msg():                                                                          # this function will generate message to client in email
    l=[]                                                                            #  this  will empty list
    global z                                                                        # it defines variable
    z=generate_otp()                                                                #   store in z of calling function  
    l.append(z)                                                                     #  this converts list
    y=str()                                                                         # y is string  for message  
    y="!!!  THANKS FOR REGISTRING IN THE Bi en cell NETWORK IIT ROPAR !!! \n"+"\n OTP -> "+z+"\n Enter OTP for completing registration "
    return y                                                                        # this return as message



def send_otp():                                                                 
    import smtplib
    from email.message import EmailMessage

    messg = EmailMessage()
    messg.set_content(msg())

    messg['Subject'] = "|| Confirmation OTP --  BI en CELL || "
    messg['From'] = "bi.en.cell.iit.ropar@gmail.com"
    messg['To'] = entry+"@iitrpr.ac.in"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('bi.en.cell.iit.ropar@gmail.com','bwzatcbjycabeoqh')
    server.send_message(messg)
    print("OTP sent to "+entry+'@iitropar.ac.in')
    server.quit()

def CONFIRMATION():
    '''
    THIS FUNCTIONS LETS US TO ROCEED IFF we have entered the correct OTP 
    '''
    send_otp()                                          # Calls the send_otp function for sending OTP at the iit ropar email id.
    re_OTP = input('\nENTER OTP: ')                       
    
    if re_OTP != z:                                     # Condition for entering the wrong OTP.
        print("\nOTP does not match ")  
        PP=input("(R)e-send OTP/ (C)ancel")             # option for RE-SENDING the OTP.            
            
        if PP == 'R':
            CONFIRMATION()  
        if PP == 'C':
            REGISTRATION()
   
    if re_OTP == z:
        print("\nOTP VERIFIED\n")


def LOGIN():
    '''
    Logs in the registered users into the platform.
    '''
    import pwinput                                      # Secret password module!

    print('\n\n'+20*" "+'|| Bi en Cell network IIT ROPAR -- LOGIN || \n')
   
    creation=open("DATAMINE.txt",'a')                   # Creating the DATABASE.
    creation.close()

    global entry

    entry=input(str("\nENTRY NO: "))                    # asks for your registered Entry number.
    
    if len(entry)!=11:                                              # eliminating invalid entry numbers.
        print("\nPlease enter a correct entry no.")
        LOGIN()
    
    passkey= pwinput.pwinput(prompt="Password: ",mask='*')  # ... and corresponding Password.
    
    storage=open('DATAMINE.txt','r')                    # Verification steps for the entry id and its password.

    L=storage.readlines()                               # creates a list L whose each element is the user's credentials.
    
    storage.close()
    
    count=0
   
                                                         # the CODE below verifies the given entry number is in the registered users list!

    for i in range(len(L)):
    
        if entry in L[i]:
            count+=1
            
            a=L[i]
            b = a.find(entry)  # find() method returns the lowest index of the substring 
                               # ...i.e. username if it is found in a given string. If it is not found #then it returns -1.
            
            username = a[:b-1]              # Username is stored in such a way such that this slicing gives us the username. 
            matchh = a[b+12:-1]             # Password match is obtained via this slicing of L[i]'s for desired user. 
    
                                                        # Unregistered Users are asked for doing the REGISTRATION, by calling the REGISTARTION
                                                        # ...function.
    if count!=1:                                        
        print('\n You are not registered, kindly Register on the network.\n')
        REGISTRATION()


    # the below code checks if the password is matching for the registered user!
    if count==1:
        if passkey == matchh :                          # if password matches the user is welcomed!
            print('\n'+30*" "+'Welcome '+str(username)+'!')
            print('\n'+25*" "+'to the Bi en Cell network, IIT ROPAR \n')
       
        else:                                           # if not, the Login process is forced to repeat.
            print("\n Incorrect password \n")
            LOGIN()


def NAME_THIS(entry_no):
	'''
	GIVES OUT THE NAME CORRESPONDING TO A REGISTERED USER'S ENTRY NUMBER.
	'''
	storage = open('DATAMINE.txt','r')                  # Scans the DATAMINE for all registerd users and...
                                    	
	LIST_USERS = storage.readlines()                    # ... stores them in a LIST.
     
	for k in range(len(LIST_USERS)):                    # The following nest of loops, searches the DATAMINE for the corresponding name of... 
                                                        # ...the given entry number. 
		if LIST_USERS[k].find(entry_no)!=-1:
			indecx = LIST_USERS[k].find(entry_no)
			NAME = LIST_USERS[k][:indecx-1]
 
	storage.close()
 
	return NAME

        
def MATCHMAKING():
	
    '''
    Matches customer with the seller, works on the principle of first come first serve, no discrimination gauranteed!

    '''
    import time                                                     # time displaying for updation of the MATCH-list
    buy=open('BUYMINE.txt','r')                                     # A list of Buyers.
    sell=open('SELLMINE.txt','r')                                   # A list of Sellers.

    B = buy.readlines()
    S = sell.readlines()
    X=[]
    for i in range(len(S)):                                         # Checks the Seller's list for names of sellers.
        for j in range(len(B)):                                     # Checks the Buyer's list for names of buyers.
            if S[i][-1]!='x' and B[j][-1]!='x':                     # Condition for checking whether or not, the buyer and seller are matched
                                                                    # ...and if they are matched 'x' is concatenated in them to annhilate'em.
                if S[i][15]==B[j][15]:
                    tt=time.asctime()
                    buyer = NAME_THIS(B[j][3:14])                   # recalls the NAME_THIS() function, on the entry number of the BUYER.
                    seller = NAME_THIS(S[i][3:14])                  # recalls the NAME_THIS() function, on the entry number ot the SELLER.
                    X.append(buyer+'_'+str(B[j][15])+'_'+seller)
                    S[i]+='x'                                       # marks this SELLER as Mathced (by adding 'x') hence annhillation occurs.
                    B[j]+='x'                                       # marks this Buyer as Matched (by adding 'x') hence annhilation occurs.
                    buy.close()
                    sell.close()

    print('\n'+32*" "+'MATCHLIST:-')
    print(32*' '+'Buyers_OPT_Sellers\n')
    
    tt=time.asctime()
    for i in range(len(X)):                                         # gives the MATCH-LIST
        time.sleep(0.1);print(23*' '+str(i+1)+') '+X[i])
	
    print('\n'+23*" "+"Last Updated "+tt[4:-4])                     # gives the list recent most updation time


def MAIN():
    '''
    The main pallet for selecting different options incl. (B)reakfast, (L)unch, (D)inner, (S)nacks. For selling and buying from this sale.
    '''
    import time

    print('\n\n'+22*" "+'|| Bi en Cell network IIT ROPAR || \n')
    
    START=0 
    while START!='L':                                               # Giving options for Registration, Login and Matchlist.
        START=input('\n'+"(R)egistration / (L)ogin / (M)atchlist"+'\n')
        if START=='M':
            MATCHMAKING()
        if START=='R':
            REGISTRATION()
            
    LOGIN()

    z=input('(B)uy or (S)ell?\n ')                                  # option for Buying or Selling.
     
    sell = open("SELLMINE.txt", "a")
    buy = open("BUYMINE.txt", "a")
   
    if z=='B':                                                      # if the option of Buying is selected, further options of...
                                                                    # Breakfast, Lunch, Dinner and Snacks are given.
    
        x=input('(B)reakfast, (L)unch, (D)inner, (S)nacks\n ')
       
        '''
        The following conditionals saves the buyer's entry number and time of quering for the coupon.
        '''

        if x=='B':
            
            t=time.asctime()
            
            entry_time_stamp_new ='_B_'+str(entry)+'_B_'+str(t)+'\n' 
            
            buy.write(entry_time_stamp_new) 

        if x=='L':
      
            t=time.asctime()
            
            entry_time_stamp_new =('_B_'+str(entry)+'_L_'+str(t)+'\n') 
            
            buy.write(entry_time_stamp_new) 


        if x=='D':
       
            t=time.asctime()
           
            entry_time_stamp_new =('_B_'+str(entry)+'_D_'+str(t)+'\n') 
            
            buy.write(entry_time_stamp_new) 
       
        if x=='S':
       
            t=time.asctime()
            
            entry_time_stamp_new =('_B_'+str(entry)+'_S_'+str(t)+'\n') 
            
            buy.write(entry_time_stamp_new) 

        buy.close()

    
    if z=='S':
        
        x=input('(B)reakfast, (L)unch, (D)inner, (S)nacks \n')
        
        '''
        The following conditionals saves the Seller's entry number and time of quering for selling the coupon.
        '''
    
        if x == 'B' :
       
            t=time.asctime()
            
            entry_time_stamp_new =('_S_'+str(entry)+'_B_'+str(t)+'\n') 
            
            sell.write(entry_time_stamp_new) 

        
        if x=='L':
            
            t=time.asctime()
            
            entry_time_stamp_new =('_S_'+str(entry)+'_L_'+str(t)+'\n') 
            
            sell.write(entry_time_stamp_new) 
      
        if x=='D':
            
            t=time.asctime()
            
            entry_time_stamp_new =('_S_'+str(entry)+'_D_'+str(t)+'\n') 
            
            sell.write(entry_time_stamp_new) 

        if x=='S':
            
            t=time.asctime()
            
            entry_time_stamp_new =('_S_'+str(entry)+'_S_'+str(t)+'\n') 
            
            sell.write(entry_time_stamp_new) 

        sell.close()

    '''
    CHECKING OF THE BUYERS AND SELLERS LIST
    
    buy  = open("BUYMINE.txt", "r")

    output_1_new = buy.read()
    
    #print('\n')
    #print(output_1_new)  
  
    buy.close()
    
    sell  = open("SELLMINE.txt", "r")
    
    output_2_new = sell.read()
    
    #print('\n')
    #print(output_2_new)

    sell.close()
    
    '''
    
                    
    MATCHMAKING()                           # Recalls the MATCHMAKING FUNCTION for Updating the Matching list. 
         
    # Code FINAL
MAIN()







