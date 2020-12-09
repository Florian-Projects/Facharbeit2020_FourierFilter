import numpy as np
from createimages import *

def overlay(mask, spectrumImage, coefficient):
	"""
	Wendet eine Spektrummaske auf ein Fourierspektrum an, indem es die differenz der einer und des zu maskierenden Spektrums bildet,
	um so geziehlte Fourierkoeffizeinten auf 0 zu setzen.
	Die maske ist dabei eine bearbeitete version eins Bildes des Spektrum!
	Zu "löschende" koeffizienten sind dabei durch schwarze Pixel repräsentiert.
	mask = Maske
	spectrumImage = Bild des Fourierspektrums
	coefficient = MAtrix in der die FOurierkoeffizienten gespeichert sind

	mask, spectrumImage müssen array_like datenstrukturen sein (siehe numpy.array dokumentation) und müssen die selbe größe haben.
	coefficient ist ein 2d numpy array des komplexen datentyps.
	"""
	maskArr = np.array(mask)
	spectrumArr = np.array(spectrumImage)
	difference = maskArr - spectrumArr #die differenze von mask und spectrumImage gibt an welche koeffizienten auf 0 gesetzt werden sollen.
	difference = np.fliplr(difference)
	N,M = maskArr.shape
	for m in range(M): #für jeden Pixel wiederhole
		for n in range(N):
			if not(difference[n][m] == 0): #falls die differenz ungleich 0 ist, bedeutet dies, dass mask von spectrumImage abweicht und der koeffizient auf 0 gesetzt werden soll
				coefficient[n][m] = 0.1+0.1j #der koeffizient wird nicht auf exakt 0 gesetzt, da dies zu grafik Fehlern in createimages.createImage() führt
	return(coefficient)

def overlay2(mask, coeffcient):
	"""
	Wendet eine Maske auf ein Fourierspektrum an. Die Maske ist hier anders als bei overlay ein schwarzweiß bild.
	Weiße Pixel stehen dabei für koeffizienten die auf 0 gesetzt werden sollen. Schwarz dafür das sie unverändert bleiben sollen.
	"""
	maskArr = np.array(mask)
	maskArr = np.fliplr(maskArr)
	N,M = coeffcient.shape
	for m in range(M):
		for n in range(N):
				if n > int(N/2) - 1:
					nc = N - n - 1
				else:
					nc = n
				if m > int(M / 2) - 1:
					mc = M - m - 1
				else:
					mc = m
				if maskArr[nc][mc] > 0:
					coeffcient[n][m] = 0.1+0.1j

	return(coeffcient)

def mixMagnitudePhase(spectrum1, spectrum2):
	"""
	Berechnet Fourierkoeffizienten aus der Amplituden des ersten Spektrum und der Phase des zweiten Spektrum
	"""
	magnitude = np.abs(spectrum1)
	phase = np.angle(spectrum2)
	N, M = spectrum1.shape
	coeffiecient = np.zeros((N,M), dtype=complex)
	for m in range(M):
		for n in range(N):
			coeffiecient[n][m] = magnitude[n][m] * np.exp(1j*phase[n][m])
	return coeffiecient

def mixImage(spectrum1, spectrum2, threshold):
	"""
	Vermixt 2 zentralisierte Spektra, indem bis zu einer bestimmte Frequenz die Fourierkoeffizienten des einen Soeltrum und nach der Frequenz des 2ten Spektrum
	"""
	N, M = spectrum1.shape
	coeffiecient = np.zeros((N, M), dtype=complex)
	for m in range(M):
		for n in range(N):
			if np.sqrt(((m-(M/2))**2)+((n-(N/2))**2)) > threshold: #der linke Teil des Vergeleichs berechnet den Abstand des Eintrages von der Mitte.
																	# Es Gillt je weiter von der Mitte entfernt desto höher die Frequenz
				coeffiecient[n][m] = spectrum2[n][m]
			else:
				coeffiecient[n][m] = spectrum1[n][m]

	return coeffiecient
