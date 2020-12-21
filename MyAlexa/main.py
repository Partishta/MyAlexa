import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # for female voice
engine.setProperty('voice', voices[1].id)  # for female voice


def talk(text):
    engine.say(text)
    engine.runAndWait()


# engine.say('I Am Your Alexa')
# engine.say('What Can I Do For You')
# engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
            return command
    except:
        pass


def run_alexa():
    command = take_command()
    print(command)
    if command == None:
        talk('Please say something')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('Current time is ', time)
    elif 'Who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif'date' in command:
        talk('sorry,I have a headache')
    elif'are you single' in command:
        talk('I Am in a relationship with wifi')
    elif'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()



