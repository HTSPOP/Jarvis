from pytube import YouTube,Playlist
import scipy as sp
import speak as s
import os

def Finish():
    print('\n Done Download!')

def D():
    s.speak("\n Press 1 For Video Download | Press 2 For Playlist Download | Press 3 For Audio Download ")
    while True:

        E = input("\n Enter Here : ")

        if '1' in E:
            s.speak("\n You Have Selected Video ")
            s.speak ("\n Please Enter URL")
            URL1 = input("\n Enter URL Here : ")
            s.speak ("\n Now Please Enter Path")
            Path1 = input("\n Enter Path Here : ")
            s.speak ("\n Now Please Enter resolution")
            R1 = input("\n Enter Resolution Here : ")
            Video = YouTube(URL1)
            s.speak(f'\n Your Video Title Is : {Video.title}')
            s.speak("\n Downloading........Please Wait For While")
            video = Video.streams.get_by_resolution(R1)
            video.download(Path1)  
            s.speak(f"\n {Video.title} Has Being Downloaded IN {Path1}")
            s.speak("\n DO YOU WHANT TO OPEN VIDEO DOWNLOADED Folder IF YES WRITE OPEN OR NO FOR NOT TO DOwNLOADED FOLDER OK ")
            o = input("\n Enter Here : ")
            if 'Yes' or 'y' or 'yes' or 'Y' in o:
                os.startfile(Path1)
            else:
                exit()

        elif '2' in E:
            s.speak ("\n You Have Selected Playlist ")
            s.speak ("\n Please Enter URL")
            URL2 = input("\n Enter URL Here : ")
            s.speak ("\n Now Please Enter Path")
            Path2 = input("\n Enter Path Here : ")
            s.speak ("\n Now Please Enter resolution")
            R2 = input("\n Enter Resolution Here : ")
            Play = Playlist(URL2)
            s.speak("\n Now Please Wait For While...............")
            for video in Play.videos:
                video.streams.get_by_resolution(R2).download(Path2)
                video.register_on_complete_callback(Finish())
            s.speak("\n All Download Completed")

        elif '3' in E :
            s.speak ("\n You Have Selected Audio ")
            s.speak ("\n Please Enter URL")
            # url input from user
            yt = YouTube(str(input("\n Enter URL Here : ")))

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # check for destination to save file    
            s.speak ("\n Now Please Enter Path")
            destination = str(input("\n Enter Path Here : ")) or '.'

            # download the file
            out_file = video.download(output_path=destination)

            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # result of success
            print( '                     ')
            s.speak(yt.title + " has been successfully downloaded.")
        elif 'quit' in E:
            break
# D()