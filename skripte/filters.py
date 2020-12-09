import numpy as np
from numpy import pi

def lowpass(coefficient, radius):
	"""
	Wendet den Lowpass-Filter auf ein zentralisiertes Spektrum an
	coefficient ist dabei ein numpy 2d Array von komplexen Zahlen
	"""
	N,M = coefficient.shape
	for m in range(M):
		for n in range(N):
			if (np.sqrt(((m-(M/2))**2)+((n-(N/2))**2)) > radius): #relativ zu M/2,N/2. Der Linke teil des vergleichs bestimmt den abstand des eintrages n,m von der "mitte" der Matrix.
				coefficient[n][m] = 0.1+0.1j #da 0.1 der kleinste Farbwert in dem Spektrum ist und 0 sonst als weiß dargestellt wird
	return coefficient
	
def highpass(coefficient, radius):
	"""
	Wendet den Highpass-Filter auf ein zentralisiertes Spektrum an
	"""
	N,M = coefficient.shape
	for m in range(M):
		for n in range(N):
			if (np.sqrt(((m-(M/2))**2)+((n-(N/2))**2)) < radius): #relativ zu M/2,N/2
				coefficient[n][m] = 0.1+0.1j
	return coefficient

def gaussianLowpass(coefficient, cutOfFrequency):
	"""
	Wendet den Gaußschen Lowpass-Filter auf ein zentralisiertes Spektrum an
	cutOfFrequenzy ist dabei die Streung der Gauss/ Glockenkurve
	"""
	N, M = coefficient.shape
	gaussValues = np.zeros((N,M))
	for m in range(M):
		for n in range(N):
			gaussValue = np.exp(-(((m - (M/2))**2 + (n - (N/2))**2) / ((2 * cutOfFrequency) ** 2)))
			gaussValues[n][m] = gaussValue
			coefficient[n][m] = coefficient[n][m] * gaussValue
	return coefficient
	
def gaussianHighpass(coefficient, cutOfFrequency):
	"""
	Wendet den Gaußschen Highpass-Filter auf ein zentralisiertes Spektrum an
	"""
	N, M = coefficient.shape
	gaussValues = np.zeros((N, M))
	for m in range(M):
		for n in range(N):
			gaussValue = np.exp(-(((m - (M / 2)) ** 2 + (n - (N / 2)) ** 2) / ((2 * cutOfFrequency) ** 2))) #berechne den Gaußkoeffizienten
			gaussValues[n][m] = gaussValue
			coefficient[n][m] = coefficient[n][m] * (1 - gaussValue)
	return coefficient
