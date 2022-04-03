from instabot import Bot
from Back.speak import speak,speak_only
bot = Bot()
bot.login(username="telavane_00007", password="Harsh@2007")
speak("Please Tell ME What Should I Do Press 1 For send Message Press 2 For Get AnyOne Followers List ")
inpu = input("Enter Here : ")
if "1" in inpu:
    speak_only("Enter The UserName : ")
    username = input ("\nEnter The UserName : ")
    speak_only("Enter The Message :")
    msg = input("\nEnter The Message : ")
    bot.send_message(msg, [username])
elif "2" in inpu:
    foll = input("Enter The User Name : ")
    bot.get_user_followers(foll)