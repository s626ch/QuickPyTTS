import tkinter as tk
import pyttsx3
from time import sleep

# window definitions
window = tk.Tk()
window.title('QuickTTSPy')

# voice variable, 0 = male, 1 = female
voice = tk.IntVar() # this will be changed by a checkbox--tk int variable 0/1
engine = pyttsx3.init() # create voice object
vol = tk.DoubleVar() # double var for volume control

# code snippets
def voice_toggle():
    if(voice.get() == 1):
        voices = engine.getProperty('voices')       #getting details of current voice
        engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    else:
        voices = engine.getProperty('voices')       #getting details of current voice
        engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male

def playVoice():
    engine.say(textInput.get())
    engine.runAndWait() # talk!!

def stopVoice():
    engine.stop() # shut up!!!

def saveFile():
    engine.save_to_file(textInput.get(), f"{fileInput.get()}.wav") # save tts to an wav file
    engine.runAndWait() # talk!!

# lol this doesn't even work
#def volumeController():
#    engine.setProperty('volume',volumeScale.get())

# frames, each one is its own line
textVoice = tk.Frame(master=window)
playPause = tk.Frame(master=window)
#volumeContainer = tk.Frame(master=window)
saveToFile = tk.Frame(master=window)

# easy packing?
#frames = [textVoice, playPause, volumeContainer, saveToFile]
frames = [textVoice, playPause, saveToFile]

# the shit in the window
# main -- input and voice toggle
mainLabel = tk.Label(text="Simple TTS applet, put your text in the textbox below.") # info label
textInput = tk.Entry(master=textVoice)
voiceToggle = tk.Checkbutton(master=textVoice,text="Toggle Female voice",variable=voice,onvalue=1,offvalue=0, command=voice_toggle)
# play and pause controls
#playButton = tk.Button(master=playPause,text="Play TTS",command=playVoice)
playButton = tk.Button(master=playPause,text="Play TTS",command=playVoice)
stopButton = tk.Button(master=playPause,text="Stop TTS",command=stopVoice)
# volume slider
#volumeScale = tk.Scale(master=volumeContainer,from_=0.0,to=1.0,tickinterval=0.1,command=volumeController,orient='horizontal')
# file saving
saveLabel = tk.Label(text="Want to save the TTS to a wav? Put the file-name above.") # file save help label
fileInput = tk.Entry(master=saveToFile)
saveButton = tk.Button(master=saveToFile,text="Save WAV",command=saveFile)

#packing
mainLabel.pack(fill=tk.BOTH,expand=True)
for i in frames:
    i.pack(fill=tk.BOTH,expand=True)
# i can't really do that easy method for the rest because it'd need to be interrupted by the "save label"
textInput.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
voiceToggle.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
playButton.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
#stopButton.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True) # can't even make use of this due to the window freezing up
# i love tkinter.
#volumeScale.pack(fill=tk.BOTH,expand=True)
saveLabel.pack(fill=tk.BOTH,expand=True)
fileInput.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
saveButton.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)

# initialize window
window.mainloop()