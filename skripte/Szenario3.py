import createimages
from PIL import Image
import numpy.fft as fft
import numpy as np
import steganography as stg

"""Versteckt eine Geheimbotschaft in einem Bild, durch anwendung einer Maske auf das Fourierspektrum"""

x = Image.open("bilder/kameraman.png").convert("L") #öffne kameraman.png als Luminanzbild
x = np.array(x) #konvertiere Bild zu Matrix/ numpy 2d Array
createimages.createImage(x) #zeige das original Bild

mask = Image.open("maske/smileyMaske.png").convert("L") #öffne die Bildmaske als Luminanzbild
spectrum = fft.fft2(x) #Wende die Fouriertransformation an
createimages.plotFrequencySpectrum(spectrum) #zeige das Spektrum

spectrum = stg.overlay2(mask, spectrum) #wende die Maske an
stg.plotFrequencySpectrum(spectrum) #zeige das neue Spektrum

img = fft.ifft2(spectrum) #Rücktransformation
createimages.createImage(img.real) #zeige das neue Bild
createimages.exportImage(img.real) #speicher das neue Bild

x = Image.open("export.png").convert("L") #importiere das neue Bild
x = np.array(x) #konvertiere Bild zu Matrix
spectrum = fft.fft2(x) #Wende die Fouriertransformation an
createimages.plotFrequencySpectrum(spectrum) #zeige das Spektrum des neuen Bild
