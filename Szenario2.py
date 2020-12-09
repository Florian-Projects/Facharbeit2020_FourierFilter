from transforms import *
import createimages
from PIL import Image
import numpy as np
import numpy.fft as fft
import steganography as stg

""" Entfernt Shutterartefakte aus dem Bild mondlandung.png"""

x = Image.open("bilder/mondlandung.png").convert("L") #öffne mondlandung.png als Luminanzbild
x = np.array(x) #konvertiere bild in eine Matrix
createimages.createImage(x) #zeige das original Bild

spectrum = fft.fft2(x) #Wende die Fouriertransformation an
spectrum = fft.fftshift(spectrum) #Zentralisierung des Spektrum

mask = Image.open("maske/mondlandungMaske.png").convert("L") #öffne die Spektrummaske
spectrum2 = Image.open("spektrum/mondlandungSpektrum.png").convert("L") #öffne das Referenzspektrum
stg.overlay(mask,spectrum2,spectrum) #wende die Maske an

createimages.plotFrequencySpectrum(spectrum) #zeige das neue Amplitudenspektrum

img = fft.ifft2(fft.ifftshift(spectrum)) #Rücktransformation

createimages.createImage(img.real) #zeige das Ergebniss

