from calendar import month
from pandas import read_csv,DataFrame
import datetime
from Back.speak import speak, speak_only
df = read_csv("bd.csv",sep=',')
df = DataFrame(df,columns=['Name','Mon','Date'])

day = datetime.datetime.now().day
month = datetime.datetime.now().month
list12 =[]

for i in range(6):
    try :
        if df['Mon'][i] == month:
            if day == df['Date'][i]:
                list12.append(df['Name'][i])
    except:
        break
for Name in list12:
    speak(f"\nAnd Today's The Birthday OF : {Name}")
