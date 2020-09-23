import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#init
Run = True

# to open your sutes in chrome
webbrowser.register('chrome',
	    None,
	     webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

#selecting voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1])

#speak function,it helps to speak with you
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#greeting funtion
def wishme():
    hours = datetime.datetime.now().hour
    if hours in range(12):
        print("Good Morning!,yogith")
        speak("Good Morning!,yogith")

    elif hours in range(12,19):
        print("Good Afternoon!,yogith")

        speak("Good Afternoon!,yogith")

    else:
        print("Good Evening!,yogith")

        speak("Good Evening!,yogith")
    print("It's Thor,how may i help you ?")

    speak("It's Thor,  how may i help you ?")


#helps to convert your audio or voice to string
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say that again")
        speak("please say that again")
        return "None"
    return query

#Sends email
#Before this you need to allow less secure apps acessin your gmail
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourEmail@gmail.com","password")
    server.sendmail("yourEmail@gmail.com",to,content)
    server.close()


#main function
if __name__ == "__main__":
    wishme()
    while Run:
        query = takecommand().lower()

        #collects information from wikipedia
        if 'wikipedia' in query:
            speak("searching in wikipedia...")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)#increase the value of sentences to get more number of lines
            speak("According to wikipedia")
            print("According to wikipedia")
            print(results)
            speak(results)

        
        elif ("open youtube" in query):
            webbrowser.get('chrome').open_new("youtube.com")
            Run = False
        
        elif ("open google" in query):
            webbrowser.get('chrome').open_new("Google.com")
            Run = False

        elif ("open mail" in query):
            webbrowser.get('chrome').open_new("gmail.com")
            Run = False



        elif ("play music" in query):
            music_dir = "C:\\Users\\yogit\\OneDrive\\Desktop\\MyFavSongs\\music"
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[8]))
            Run = False
        
        elif("play my favourite music" in query):
            fmusic_dir = "C:\\Users\\yogit\\OneDrive\\Desktop\\MyFavSongs"
            fsongs = os.listdir(fmusic_dir)

            os.startfile(os.path.join(fmusic_dir,fsongs[6]))

        elif ('the time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Yogith, the time is {strTime}")
            Run = False
        

        elif('open code' in query):
            codepath = "C:\\Users\\yogit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif('send email' in query):
            try:
                speak("what should i send ?")
                content = takecommand()
                to = "toemail@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry my friend .i'm not able to send this email")


        elif("bye" in query):
            Run = False