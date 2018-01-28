from flask import *
import speech_recognition as sr
import os
import pyaudio
app=Flask(__name__)
@app.route("/")
def call():
        return "helloworld"
@app.route("/camera")
def hello():
        while(True):
            print("Try")
            r=sr.Recognizer()
            print(r)
            with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print(r.energy_threshold)
                    audio=r.listen(source)
                    text1="default"
            print(audio)
            try:
                        text1 = r.recognize_google(audio)
                        print(text1)
            except sr.UnknownValueError:
                            print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                            print("Could not request results from Google  Speech Recognition service; {0}".format(e))
            print("Gand MARA")
            print(text1)
            f=open("IntroSpeech.vbs","w+")
            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+text1+'"'
            f.write(k)
            f.close()
            os.system("IntroSpeech.vbs")

    


if __name__=="__main__":
    app.run(debug = True)
    
