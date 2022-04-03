import speedtest
def SpeedTest():
    from Back.speak import speak_only,speak
    speak_only("Hecking Speed............")
    speak_only('Please Wait For While')
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctupload = int(uploading/800000) 
    print('   ')
    speak(f"The Uploading Speed Is {correctupload} Mbp s And Downloading Speed Is {correctDown} Mbp s")