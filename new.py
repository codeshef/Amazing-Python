import speech_recognition
import pyttsx

recognizer = speech_recognition.Recognizer()

def speak(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    with speech_recognition.Microphone() as source :
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        recognizer.energy_threshold = 2000
        recognizer.pause_threshold = .5
    try:
        print("You said {}".format(recognizer.recognize_google(audio)))
        return recognizer.recognize_google(audio)

    except:
        speech_recognition.UnknownValueError
        print "could not understand audio"
    return " "

speak("Say something!")
speak("I heard you say " + listen())

