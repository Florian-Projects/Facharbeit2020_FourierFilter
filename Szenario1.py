import createimages
import numpy as np
from PIL import Image
import numpy.fft as fft
import filters as f
import steganography as stg

"""Entfernt Texturmuster aus dem Bild fingerabdruch.png um den Fingerabdruck leserlicher zu machen"""

x = Image.open("bilder/fingerabdruck.png").convert("L") #öffne fingerabdruck.png als Luminanzbild
x = np.array(x) #konvertiere das Bild in eine Matrix
createimages.createImage(x) #zeige das original Bild

spectrum = fft.fft2(x) #DFT
spectrum = fft.fftshift(spectrum) #Zentraliesierung des Spektrums

mask = Image.open("maske/fingerabdruckMaske.png").convert("L") #öffne fingerabdruckMaske.png als Luminanzbild
spectrum2 = Image.open("spektrum/fingerabdruckSpektrum.png").convert("L") #öffne das Referenzspektrum
stg.overlay(mask, spectrum2, spectrum) #wende die Maske auf das Spektrum an (spektrum2 dient als referenz Spektrum)

f.highpass(spectrum, 5) #wende den Highpass Filter mit Filterfrequenz 3 an

createimages.plotFrequencySpectrum(np.abs(spectrum)) #zeige das neue Amplitudenspektrum

imgData = fft.ifft2(fft.fftshift(spectrum)) #Rücktransformation

createimages.createImage(imgData.real) #zeige das neue Bild
