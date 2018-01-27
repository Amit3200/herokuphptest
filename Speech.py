import os
import speech_recognition as sr
import pyaudio
import sys
from gtts import gTTS
import platform
import ctypes
import psutil
import cv2
k=str(psutil.virtual_memory())
ramdetails=(k[6:len(k)].split(','))
totalram=ramdetails[0]
totalram=int(totalram[6:])
totalram=round(totalram//(1024*1024*1000))
totalram=str(totalram)
while(True):
        
        t=0
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
        print(audio)


        #mathlist+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        
        try:
                mathslist=["calculation","calculate","solve","evaluate","maths","math"]
                talklist=["tell me about yourself","who are you","who r u","tell me something about yourself","introduce","introduce yourself","intro","give intro"]
                videolist=["capture and play","video capture","capture video","record video","record and capture","record and play","video"]
                text1 = r.recognize_google(audio)
                print("You said: " + text1)
                tts=gTTS(text=text1,lang='en')
                #tts.save("Record.mp3")
                #os.system("Record.mp3")
                speechsaid=text1.lower().split()
                print(speechsaid)
                try:
                        for i in mathslist:
                                if i in speechsaid:
                                    t=1
                                    print("Yes")
                                    break
                        if t==1:
                                mathmsg="Hi , I will help you with Maths Calculation"
                                f=open("MathSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+mathmsg+'"'
                                f.write(k)
                                f.close()
                                os.system("MathSpeech.vbs")
                                print("Give Expression : ")
                                r1=sr.Recognizer()
                                with sr.Microphone() as source:
                                    audio=r1.listen(source)
                                print(audio)
                                try:
                                    text2 = r1.recognize_google(audio)
                                    if "multiplied" in text2:
                                            text2=text2.replace("multiplied","*")
                                            print("Detected")
                                    if "multiplied by" in text2:
                                            text2=text2.replace("multiplied by","*")
                                    if "x" in text2:
                                            text2=text2.replace("x","*")
                                    if "Multiplied" in text2:
                                            text2=text2.replace("multiplied","*")
                                    if "Multiplied by" in text2:
                                            text2=text2.replace("multiplied by","*")
                                    if "multiply" in text2:
                                            text2=text2.replace("multiply","*")
                                    if "multiply by" in text2:
                                            text2=text2.replace("multiply by","*")
                                    print("Expression said : "+text2)
                                    f=open("MathResult.vbs","w+")
                                    result="Evaluated Result is : "+str(eval(text2))
                                    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+result+'"'
                                    f.write(k)
                                    f.close()
                                    print("Evaluated Result : "+str(eval(text2)))
                                    os.system("MathResult.vbs")
                                except sr.UnknownValueError:
                                        print("Google Speech Recognition could not understand audio")
                             
                                except sr.RequestError as e:
                                        print("Could not request results from Google  Speech Recognition service; {0}".format(e))
                                
                except:
                        pass


                #wordlist+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                
                try:
                        for i in talklist:
                                if i in text1:
                                    t=2
                                    print("Yes")
                                    break
                        if t==2:
                                wordmsg="I am ToughX version 1.0. I am a basic python build assistant. I can run on any machine which supports python 3.6."
                                wordmsg+="Currently My Platform Machine is "+platform.machine()+" . "
                                wordmsg+="My Platform System is "+platform.system()+" . "
                                wordmsg+="Platform Processor is "+platform.processor()+" . "
                                wordmsg+="Current RAM Memory  "+totalram+" GigaBytes . "
                                f=open("IntroSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+wordmsg+'"'
                                f.write(k)
                                f.close()
                                os.system("IntroSpeech.vbs")
                                print(z)
                except:
                        pass


                
                #VideoList+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


                
                try:
                        for i in videolist:
                                if i in text1:
                                    t=3
                                    print("Yes")
                                    break
                        if t==3:
                                print("YES")
                                videomsg="Okay! I get that. Opening Camera For You"
                                f=open("VideoSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+videomsg+'"'
                                f.write(k)
                                f.close()
                                os.system("VideoSpeech.vbs")
                                cv2.namedWindow("preview")
                                vc = cv2.VideoCapture(0)

                                if vc.isOpened(): # try to get the first frame
                                    rval, frame = vc.read()
                                else:
                                    rval = False

                                while rval:
                                    cv2.imshow("preview", frame)
                                    rval, frame = vc.read()
                                    key = cv2.waitKey(20)
                                    if key == 27: # exit on ESC
                                        break

                                cv2.destroyWindow("preview")
                                vc.release()
                except:
                        pass
                print("*************************************************************************")

                
            #error occurs when google could not understand what was said
                
             
        except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
             
        except sr.RequestError as e:
                print("Could not request results from Google  Speech Recognition service; {0}".format(e))


