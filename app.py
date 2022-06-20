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

#to save the audio file
speaker.save_to_file('AND.mp3')
speaker.runAndWait()
speaker.stop()

