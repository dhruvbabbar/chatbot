import speech_recognition as rc
import time
print("Say something!")
while True:
    rec = rc.Recognizer()
    with rc.Microphone() as source:
        print source
        audio = rec.listen(source)    

    try:
        print(rec.recognize_google(audio)) 
    except rc.UnknownValueError:
        print("I cannot understand what you said")
        time.sleep(0.5)
        print("Say again")
    except rc.RequestError as e:
        print("Error".format(e))

    word = rec.recognize_google(audio)

    if (word == 'goodbye'):
        break

