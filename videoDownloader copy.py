import csv
import scipy
import os
import wave

import matplotlib.pyplot as plt
import numpy as np


data = []

directory = wave.open("C:/Users/redsa/Downloads/CSCI 347 Music/Instrumental/Adele - Hello (Official Music Video).wav", mode='rb')

print(directory.getparams())


'''for file in os.listdir(directory):
    leftEar = 0
    rightEar = 0
    path = directory + "/"
    filename = os.fsdecode(file)
    path += filename
    #filename[:-4] #print(filename)
    sampleRate, songData = scipy.io.wavfile.read(path, mmap=True)
    #sampleRate#print(sampleRate)
    #print(songData)
    for x in songData:
        leftEar += x[0]
        leftEar += x[1]

    newDict = {'Name': filename[:-4], 'Sample Rate': sampleRate, 'Left Ear Average Amplitude': leftEar/songData.shape[0], 'Right Ear Average Amplitude': rightEar/songData.shape[0], 'Length': songData.shape[0]/sampleRate, 'Label': 'Instrumental'}
    data.append(newDict)

with open('CSCI347_Final_Project_DataA.csv', 'w', encoding="utf-8", newline='') as csvfile:
    fieldnames = ['Name', 'Sample Rate', 'Left Ear Average Amplitude', 'Right Ear Average Amplitude', 'Length', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)'''

'''length = songData.shape[0] / sampleRate
time = np.linspace(0., length, songData.shape[0])
plt.plot(time, songData[:, 0], label="Left channel")
plt.plot(time, songData[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()'''