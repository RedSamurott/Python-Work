import csv
import scipy
import os

import matplotlib.pyplot as plt
import numpy as np


data = []

directory = "C:/Users/redsa/Downloads/CSCI 347 Music/Instrumental"
count = 0
for file in os.listdir(directory):
    print(count)
    path = directory + "/"
    filename = os.fsdecode(file)
    path += filename
    filename[:-4] #print(filename)
    sampleRate, songData = scipy.io.wavfile.read(path, mmap=True)
    
    peaksLeft = [0.1]
    peaksRight = [0.1]
    valleyLeft = [0.1]
    valleyRight = [0.1]
    for x in range(0, songData.shape[0]):
        if x !=0:
            if x != songData.shape[0]-1:
                if (songData[x-1][0] < songData[x][0]) and (songData[x][0] > songData[x+1][0]):
                    peaksLeft.append(songData[x][0])

    for x in range(0, songData.shape[0]):
        if x !=0:
            if x != songData.shape[0]-1:
                if (songData[x-1][0] > songData[x][0]) and (songData[x][0] < songData[x+1][0]):
                    valleyLeft.append(songData[x][0])

    for x in range(0, songData.shape[0]):
        if x !=0:
            if x != songData.shape[0]-1:
                if (songData[x-1][1] < songData[x][1]) and (songData[x][1] > songData[x+1][1]):
                    peaksRight.append(songData[x][1])

    for x in range(0, songData.shape[0]):
        if x !=0:
            if x != songData.shape[0]-1:
                if (songData[x-1][1] > songData[x][1]) and (songData[x][1] < songData[x+1][1]):
                    valleyRight.append(songData[x][1])

    averageLeftPeak = abs((sum(peaksLeft)-.1)/len(peaksLeft))
    averageLeftValley = abs((sum(valleyLeft)-.1)/len(valleyLeft))
    averageRightPeak = abs((sum(peaksRight)-.1)/len(peaksRight))
    averageRightValley = abs((sum(valleyRight)-.1)/len(valleyRight))

    averageLeftOscilations = (len(peaksLeft)+len(valleyLeft))/2
    averageRightOscilations = (len(peaksRight)+len(valleyRight))/2
    length = songData.shape[0] / sampleRate

    newDict = {'Name': filename[:-4], 'Sample Rate': sampleRate, 'Left Ear Average Amplitude': (averageLeftPeak+averageLeftValley)/2, 'Left Ear Average Frequency': averageLeftOscilations/length, 'Right Ear Average Amplitude': (averageRightPeak+averageRightValley)/2, 'Right Ear Average Frequency': averageRightOscilations/length, 'Length': songData.shape[0]/sampleRate, 'Label': 'Instrumental'}
    data.append(newDict)
    count+=1

with open('CSCI347_Final_Project_DataI_2.csv', 'w', encoding="utf-8", newline='') as csvfile:
    fieldnames = ['Name', 'Sample Rate', 'Left Ear Average Amplitude', 'Left Ear Average Frequency', 'Right Ear Average Amplitude', 'Right Ear Average Frequency', 'Length', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

'''def recursiveReducer(listPeaks):
    if len(listPeaks) < 500:
        return listPeaks
    newListPeaks = []
    for x in range(0, len(listPeaks)):
        if (x != 0):
            if x != len(listPeaks)-1:
                if (listPeaks[x-1] < listPeaks[x]) and (listPeaks[x] > listPeaks[x+1]):
                    newListPeaks.append(listPeaks[x])
    a = recursiveReducer(newListPeaks)
    return(a)

peaks = recursiveReducer(songData[:, 0])
tails = recursiveReducer(songData[:, 1])

print(sum(tails)/len(tails))'''

            
'''
time1 = np.linspace(0., length, len(peaksLeft))
time2 = np.linspace(0., length, len(peaksRight))
plt.plot(time1, peaksLeft, label="Left channel")
plt.plot(time2, peaksRight, label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()'''