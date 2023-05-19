
import pyttsx3
# pip install pyttsx3
converter = pyttsx3.init()

converter.setProperty('rate', 150)

converter.setProperty('volume', 0.7)

converter.say("Hello GeeksforGeeks")
converter.say("I'm also a geek")
ab=['car','bus']
converter.say(ab)
converter.runAndWait()