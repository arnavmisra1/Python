import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


#hear mic and return audio as text
def transform_audio_into_text():
    #store recognizer
    r = sr.Recognizer()

    #set mic
    with sr.Microphone() as source:

        #waiting time
        r.pause_threshold = 0.8

        print("You can now speak.")

        #report recording has begun
        audio = r.listen(source)

        try:

            request = r.recognize_google(audio, language='en-gb')

            #test in text
            print("You said: " + request)

            #return request
            return request

        except sr.UnknownValueError:
            print("Uh oh! I could not understand.")

            return "I am still waiting"

        except sr.RequestError:
            print("Uh oh! There is no service.")

            return "I am still waiting"

        except:

            print("Uh oh! Something went wrong")

            return "I am still waiting"


def speak(message):
    engine = pyttsx3.init()

    engine.say(message)
    engine.runAndWait()

def ask_day():
    day = datetime.date.today()
    print(day)

    week_day = day.weekday()
    print(week_day)

    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    speak(f'Today is {calendar[week_day]}')




def ask_time():

    time = datetime.datetime.now()
    time = f'Right now, it is {time.hour} hours and {time.minute} minutes'
    print(time)

    speak(time)


def greeting():

    speak("Hello i am David! How may i help you today?")



def my_assistant():


    greeting()

    go_on = True

    while go_on:
        my_request =transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak("Of course. Here is YouTube for you")
            webbrowser.open('https://www.youtube.com')
            continue
        if 'hello david' in my_request:
            speak("Hello! How may i help you today?")
            continue
        elif 'hello' in my_request:
            speak("Hello! How may i help you today?")
            continue
        elif 'open google' in my_request:
            speak("Of course. Here is google for you")
            webbrowser.open('https://www.google.com')
            continue
        elif 'open chatgpt' in my_request:
            speak("Of course. Here is chatgpt for you")
            webbrowser.open('https://chatgpt.com/')
            continue
        elif 'open spotify' in my_request:
            speak("Of course. Here is spotify for you")
            webbrowser.open('https://spotify.com/')
            continue
        elif 'what day it is' in my_request:
            ask_day()
            continue
        elif 'what day is it' in my_request:
            ask_day()
            continue
        elif 'what time is it' in my_request:
            ask_time()
            continue
        elif 'what time it is' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak("Of course, let me look for it")
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=5)
            speak("According to Wikipedia: ")
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak("Of course, why not!")
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('this is what i found on the internet')
            continue
        elif 'search google for' in my_request:
            speak("Of course, why not!")
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('this is what i found on the internet')
            continue
        elif 'play' in my_request:
            speak("Oh that is a lovely one. I will play it right now.")
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'google': 'GOOGL',
                         'amazon': 'AMZN',
                         'microsoft': 'MSFT',
                         'yahoo': 'YHOO'}

            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                speak('Sorry, I could not find that stock')
                continue

        elif 'goodbye' in my_request:
            speak('goodbye! I hope i was of help to you')
            continue
        elif 'bye' in my_request:
            speak('goodbye! I hope i was of help to you')
            break


my_assistant()














