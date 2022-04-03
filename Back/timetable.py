from datetime import datetime
from Back.speak import speak,speak_only

FourTO5 = '''
In This Time , You Have To Ready For School/Meeting .
4:00 to 5:00
Thanks.
'''

FiveTo7 = '''
In This Time , You Have To Complete The Notes OF School And Tution .
5:00 to 7:00
Thanks.
'''

eighto15= '''
In This Time , You Have To Go TO School
7:00 to 3:00
Thanks.
'''

sixteento19 = '''
In This Time , You Have To Go To Tution
4:00 TO 7:00
Thanks.
'''

nito20 = '''
In This Time , 
You Have To DO Dinner
7:00 TO 8:00
Thanks.
'''

eto00= '''
In This Time , 
You Have To Study
8:00 TO 12:00
Thanks.
'''

def time():
    hour = int(datetime.now().strftime("%H"))
    if hour>=4 and hour<5:
        speak_only(FourTO5)
        return FourTO5
    elif hour>=5 and hour<7:
        speak_only(FiveTo7)
        return FiveTo7
    elif hour>=8 and hour<15:
        speak_only(eighto15)
        return eighto15
    elif hour>=16 and hour<19:
        speak_only(sixteento19)
        return sixteento19
    elif hour>=19 and hour<20:
        speak_only(nito20)
        return nito20
    elif hour>=19 and hour<00:
        speak_only(eto00)
        return eto00
    else:
        speak_only('''In This Time , You Have To Sleep''')
        return '''In This Time , You Have To Sleep'''

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13 : 1
# 14 : 2 
# 15 : 3
# 16 : 4
# 17 : 5 
# 18 : 6 
# 19 : 7 
# 20 : 8
# 21 : 9
# 22 : 10
# 23 : 11
# 00 : 12
# 
# 
#  
