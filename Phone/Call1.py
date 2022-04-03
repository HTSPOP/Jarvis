#To Download ADB Tool :- https://developer.android.com/studio/releases/platform-tools



#importing all modules -----------------------------------
                                                        #|
import os                                               #|
import time    
                                                        #|
#---------------------------------------------------------

def call(person):
    # from Back.speak import speak                              #|
    call_book={'swapnil':'9545147979','pappa':'8087140900','mummy':'9270346375',''}  #------------- List of phone number
    if person in call_book:   #------------------------------ Searching the call book
        ph_no=call_book[person]     #------------------------ Phone no. of the person

        command1='adb shell am start -a android.intent.action.CALL -d tel:+91'+ph_no  #----cmd. to make call
        command2='adb shell input tap 252 1811'  #--------------- cmd. to tap the speaker button
        print('calling.. '+person)
        os.system(command1)  #----------------------- executing the cmd
        time.sleep(2)
        os.system(command2)
    else:
        print('\nno saved contact')


# person='pappa'
# call(person)
          