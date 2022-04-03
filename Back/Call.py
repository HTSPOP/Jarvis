#To Download ADB Tool :- https://developer.android.com/studio/releases/platform-tools



#importing all modules -----------------------------------
                                                        #|
import os                                               #|
import time    
import speak                                         #|
                                                        #|
#---------------------------------------------------------

def call(person):
    from phone_book import contacts
    call_book=contacts  #------------- List of phone number
    if person in call_book:   #------------------------------ Searching the call book
        ph_no=call_book[person]     #------------------------ Phone no. of the person

        command1='adb shell am start -a android.intent.action.CALL -d tel:+91'+ph_no  #----cmd. to make call
        command2='adb shell input tap 210 2183'  #--------------- cmd. to tap the speaker button
        speak.speak('calling.. '+person)
        os.system(command1)  #----------------------- executing the cmd
        time.sleep(2)
        os.system(command2)
    else:
        speak.speak('no saved contact')


# person='swapnil'
# call(person)
          