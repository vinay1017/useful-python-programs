# A method for speech. You could adapt this to store what someone says.


import speech_recognition as sr


def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            print(text)  # this is the speech converted to string
        except:
            print("Sorry, could not recognize what you said.")
        return text


text = speech()
print(text)
