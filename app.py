import pyttsx3

#open and read the file
with open('AND.txt', encoding='UTF8') as f:
    content = f.read()

#initialize the engine
speaker = pyttsx3.init()

#iterate through the file and speak each line
for line in content.splitlines():
    speaker.say(line)
    speaker.runAndWait()
    