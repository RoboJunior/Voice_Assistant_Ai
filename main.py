import openai
import pyttsx3
import pywhatkit
import speech_recognition as sr
from openai.api_resources import Completion
import pywhatkit as py
import time
import datetime
import webbrowser
import os
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

openai.api_key = "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"

engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("I cant understand what are you trying to say!!.Can you please repeat??")


def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    running = True
    wish_me()
    sentiment()
    while running:
        speak_text('Say hello to start or goodbye to quit or to access special features say special')
        print('Say hello to start or goodbye to quit!!')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if 'special' in transcription:
                speak_text('Accessing special features')
                print('Accessing special features')
                special_features(transcription)
                running = False
            elif transcription.lower() == 'goodbye':
                speak_text('Bye have a good day')
                print('Bye have a good day!!')
                running = False
            elif transcription.lower() == 'hello':
                filename = "input.wav"
                speak_text('How can i help you')
                print('How can i help you??')
                with sr.Microphone() as source:
                    source.pause_threshold = 1
                    audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                    with open(filename, 'wb') as f:
                        f.write(audio.get_wav_data())
                text = transcribe_audio_to_text(filename)
                if text:
                    print(f"You said : {text}")

                    response = generate_response(text)
                    print(f"Junior : {response}")

                    speak_text(response)
        except Exception as e:
            print("An error occurred : {}".format(e))


def special_features(features):
    special = True
    while special:
        wish_me()
        speak_text('What do you want to access?? for example Say play to play a song')
        print('What do you want to access.Example Say play to play a song')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if 'play' in transcription:
                song = transcription.replace('play', '')
                speak_text('Playing' + song)
                print('Playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in transcription:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak_text('Current time' + time)
                print('Current time is ' + time)
            elif transcription.lower() == 'open youtube':
                speak_text('Opening youtube')
                webbrowser.open('https://www.youtube.com/')
            elif 'stack' in transcription:
                speak_text('Opening stackoverflow')
                webbrowser.open('https://stackoverflow.com/')
            elif 'open mail' in transcription:
                speak_text('Opening mail')
                webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
            elif transcription.lower() == 'open steam':
                codePath = r"C:\Program Files (x86)\Steam/steam.exe"
                speak_text('Opening steam')
                os.startfile(codePath)
            elif 'legends' in transcription:
                apex_legends = r"D:\SteamLibrary\steamapps\common\Apex Legends\r5apex"
                speak_text('Opening Apex legends')
                os.startfile(apex_legends)
            elif 'bye' in transcription:
                speak_text('Bye have a good day')
                special = False
            elif 'back' in transcription:
                main()
                special = False
        except Exception as e:
            print("An error occurred : {}".format(e))


def wish_me():
    current_time = datetime.now()
    hour = current_time.hour
    if hour >= 0 and hour < 12:
        speak_text('Good morning Sir')
    elif hour >= 12 and hour < 18:
        speak_text('Good afternoon Sir')
    else:
        speak_text('Good evening Sir')


def sentiment():
    sentiment_ = True
    while sentiment_:
        speak_text("How are you sir ")
        print("How are you sir?")

        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            senti = SentimentIntensityAnalyzer()
            analyzer = senti.polarity_scores(transcription)
            if analyzer['compound'] >= 0.05:
                speak_text('Hope you are doing great sir!')
                happy()
                sentiment_ = False
            elif analyzer['compound'] <= -0.05:
                speak_text('What is bothering you sir')
                sad()
                sentiment_ = False
            else:
                print('netural')
                sentiment_ = False

        except Exception as e:
            print("An error occurred : {}".format(e))


def happy():
    happy = True
    while happy:
        speak_text('Do you want to play a song to match your vibe')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if 'yes' in transcription:
                happy_song()
                happy = False   
            elif 'no' in transcription:
                speak_text('Sorry sir if i cant match your vibeg')
                print('Sorry sir that i cant make you feel ok ')
                happy = False
            else:
                speak_text("I cant understand can you please repeat again sir")
                print("I cant understand can you please repeat again sir")

        except Exception as e:
            print("An error occurred : {}".format(e))

def happy_song():
    speak_text("What song you want me to play sir!")
    print("What song you want me to play sir!")
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if 'play' in transcription:
                song = transcription.replace('play', '')
                speak_text('Playing' + song)
                print('Playing' + song)
                pywhatkit.playonyt(song)
            else:
                pass
        except Exception as e:
            print("An error occurred : {}".format(e))


def sad():
    sad = True
    while sad:
        speak_text("Do you want to play a game to be ok sir??")
        print("Do you want to play a game to be ok sir??")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'yes' in transcription:
                    speak_text("Here are the list of games installed in your pc sir Apex legends Fifa 2023 Battlefield 1 Hogwarts legacy The last of us Part 1 Combat Master Veiled experts")
                    print("""1 .Apex legends 
                             2. Fifa 2023 
                             3. Battlefield 1 
                             4. Hogwarts legacy 
                             5. The last of us Part 1
                             6. Combat Master
                             7. Veiled experts""")
                    games()
                    sad = False 
                elif 'no' in transcription:
                    speak_text('Do you want to text someone and get a call back sir ?')
                    print('Do you want to text someone and get a call back sir ?')
                    sad = False
                    no()
                else:
                    speak_text("I cant understand can you please repeat again sir")
                    print("I cant understand can you please repeat again sir")
            except Exception as e:
                print("An error occurred : {}".format(e))
            

def games():
    games = True
    while games:
        speak_text("What game you want to play sir ??")
        print("What game you want to play sir??")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'legends' in transcription:
                    apex_legends = r"D:\SteamLibrary\steamapps\common\Apex Legends\r5apex"
                    speak_text('Opening Apex legends')
                    os.startfile(apex_legends)
                    games = False
                

            except Exception as e:
                print("An error occurred : {}".format(e))
    
def sent_msg():
    message = True
    while message:
        speak_text("List of numbers avaiable to sent text message through whatsapp Appa Amma Minnie Myself")
        print("""List of numbers avaiable to sent text message through whatsapp
        1.Appa
        2.Amma
        3.Minnie
        4.Myself
        """)
        currentDateAndTime = datetime.now()
        current_hour = currentDateAndTime.hour
        current_minute = currentDateAndTime.minute + 1
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'myself' in transcription:
                    pywhatkit.sendwhatmsg("+916381315228","I need to talk i am not feeling well if your free give me a call or call me when you are free",current_hour,current_minute)
                    speak_text("message sent successfully")
                    message = False
            except Exception as e:
                print("An error occurred : {}".format(e))


def no():
    no = True
    while no:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'yes' in transcription:
                    sent_msg()
                    no = False
                elif 'no' in transcription:
                    speak_text("Sorry sir if i couldnt help you")
                    print("Sorry sir if i couldnt help you")
                    no = False
                else:
                    speak_text("Sorry sir i couldnt understand you")
                    print("Sorry sir i couldnt understand you")
            except Exception as e:
                print("An error occurred : {}".format(e))



if __name__ == "__main__":
    main()
