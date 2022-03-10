from gtts import gTTS
import gtts
from playsound import playsound
import os
import pyttsx3

inp = list(input())

i = 0
count = 0
while(i < len(inp)):
    if (inp[i] == "a" or inp[i] == "e" or inp[i] == "i" or inp[i] == "o" or inp[i] == "u"):
        count = 1
        break
    i += 1

inp.append("m")
temp = inp[len(inp)-1]
for j in range (len(inp)-2, i, -1):
    inp[j+1] = inp[j]
inp[i+1] = temp

print("your funny transformation is : ", end='')
res = ""

engine = pyttsx3.init()
newvoice = 145
engine.setProperty('rate', newvoice)

for x in inp:
    res += x

lang = 'en'

#myobj = gtts.gTTS(res)

#myobj.save("bak.mp3")

#myobj.save("bak.mp3")

#os.system("mpg321 bak.mp3")
#playsound("bak.mp3")
engine.say(res)
engine.runAndWait()