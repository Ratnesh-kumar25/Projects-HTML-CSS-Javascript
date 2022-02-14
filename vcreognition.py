import webbrowser   

# pyttsx3 is the librabry which converts the text to speech
import pyttsx3

# pyttsx3.init() is the function which is used to generate the sound and sapi5 consists the voices opf male and female
engine = pyttsx3.init('sapi5')

# this is use to take the property of voices 
vo = engine.getProperty('voices')

# setproperty is used to set the voice to male and female ie. 0 for male and 1 for female
engine.setProperty('voice',vo[1].id)

# This defines the rate ie the speed of the pronounciation
engine.setProperty('rate',190)

# functaion is created which takes the input manually from the user
def speak(text):
    # Here the manual command is taken by the user 
    engine.say(text)

    # This function take sthe command and calls the init() function
    engine.runAndWait()




# speech_recognition is the library which converts the speech to text
import speech_recognition as sr

import pywhatkit

def takecommand():
    # Recognizer helps to recognize the sound from the user to the computer
    r = sr.Recognizer()

    # This is used to take the input from the microphone as a source
    with sr.Microphone() as source:

        # It is printed to know that the microphone is perfectly working
        print("start speaking...")

        # It is used to generate the output after the given seconds 
        r.pause_threshold = 2

        # It is used to listen the users voice as a source
        audio = r.listen(source)


    # try and except is used sometimes sound is not properly reached to the microphone so, in that case computer should say something like please say again.. or if the it heared the voices proerly so, it should say that the user told to do.

    try:

        # It is used so that after listening user should know the it is working.. 
        print("recognizing")

        # It stores the sound in a variable as an audio which is in indian eng language
        statement = r.recognize_google(audio, language='eng-in')

        statement = statement.lower()

        if 'alexa' in statement:
            statement = statement.replace('alexa','')

            # It is used to pronounce the recognized statement
            engine.say(statement)

            # It is used to print the statements which is recognized by the computer
            print("You said: ", statement)

        else:

            # It is used to pronounce the recognized statement
            engine.say(statement)

            # It is used to print the statements which is recognized by the computer
            print("You said: ", statement)

        if 'hello' in statement:

            engine.say('hello sir i hope you are also fine..')
            print("hello sir i hope you are also fine..")

        elif 'play' in statement:

            song = statement.replace('play','')
            print("playing..." + song)
            engine.say('playing' + song)
            pywhatkit.playonyt(song)

        # It call ths say function
        engine.runAndWait()

    except Exception as e:

        # If the computer haven't listened the sound then it should be reflected and it calls the takecommand function again
        engine.say("Please say that again..")   
        print("Please say that again..")
        return takecommand()

    return statement


if __name__ == '__main__':

    # calling the speak function
    speak("hello there, how are you doing... do you have any task for me please say ? ")

    # calling  takecommand function
    takecommand()