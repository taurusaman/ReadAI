import pyttsx3
readmyapphehe = pyttsx3.init()

print('This is a ReadAI very basic Application in which you can red aloud the text')



text = input('Enter the text you want to read it aloud:')

readmyapphehe.say(text)
readmyapphehe.runAndWait()