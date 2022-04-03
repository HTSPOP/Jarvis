#To Download ADB Tool :- https://developer.android.com/studio/releases/platform-tools



#importing all modules -----------------------------------
                                                        #|
import os                                               #|
import time                                             #|
                                                        #|
#---------------------------------------------------------


def get_my_IP(my_mac=''):
    check=os.popen('arp -a').readlines()  #--------------- geting all device ip list
    #print(check)
    for i in check:
        #print(i)
        i=i.split()   #----------------------------- reducing the line to needed information
        #print(i)

        if len(i)==3:  #---------------------------- if it is the line with ip and mac
            ip=i[0]    #---------------------------- extracting ip
            mac=i[1]   #---------------------------- extracting mac

            #print(ip,'\t\t',mac,)
            
            if my_mac!='':     #-------------------- seeing if any mac is given to find
                if my_mac==mac:         #----------- checking for match
                    return ip    #------------------ returning ip of specified device 
            else:
                print(mac,' --> ',ip)    #---------- printing all mac and ip if not specified
                pass   

ip=get_my_IP('')
print(ip)