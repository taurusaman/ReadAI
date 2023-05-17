import pyttsx3
friend = pyttsx3.init()

print('This is a ReadAI very basic Application in which you can red aloud the text')

text = input('Enter the text you want to read it aloud:')

friend.say(text)
friend.runAndWait()