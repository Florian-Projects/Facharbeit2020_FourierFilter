import cmath
import numpy as np
from numpy import pi as pi

def dft2d(image):
	"""
	Diese Methode berechnet die Diskrete-Fouriertransformation eines Bildes
	sollte nicht für Bilder größer als 10x10 Pixel verwendet werden da die Laufzeit O(n**4) beträgt.
	"""
	imageArr = np.array(image)
	N, M = imageArr.shape #height(y), width(x) M = x N = y
	output = np.zeros((N,M), dtype="complex")
	for k in range(int(M)):
		for l in range(int(N)):
			sum = 0 + 0j
			for m in range(M):
				for n in range(N):
					pixelValue = imageArr[n][m] #[y][x]
					power = cmath.exp(-1j * 2 * pi * (float(k * m) / M + float(l * n) / N))#exp = e^x
					sum += pixelValue * power
			output[l][k] = sum
	return output
	
def fdft2d(image):
	"""
	Diese Methode soll die Fouriertransformation, durch Symmetrie eigenschaften effizienter berechnen.
	TO DO: Die Symmetrie eigenschaften sind nicht so wie in den Büchern beschrieben. Warum?
		  Funktionsfähig machen.
	"""
	imageArr = np.array(image)
	N, M = imageArr.shape #height(y), width(x) M = x N = y
	output = np.zeros((N,M), dtype="complex")
	for k in range(int(M/2)):
		#print("K="+ str(k))
		for l in range(int(N/2)):
			sum = 0 + 0j
			for m in range(M):
				#print("M=" + str(m))
				for n in range(N):
					pixelValue = imageArr[n][m] #[y][x]
					power = cmath.exp(-1j * 2 * pi * (float(k * m) / M + float(l * n) / N))#exp = e^x
					sum += pixelValue * power
			output[l][k] = sum
		matrix1 = np.fliplr(output)
		output = output + matrix1
		matrix2 = np.flipud(matrix1)
		output = output + matrix2

		#for k in range(M//2):
			#for l in range(N//2):	
				#output[l + (N//2)][k + (M//2)] = output[N - l - 1][M - k - 1].real - output[l][k].imag
	return output


def idft2d(coefficient):
	"""
	Diese Methode berechnet die Rücktransformation
	Sollte nicht für Bilder größer als 10x10 verwendet werden, da die Laufzeit O(n**4) beträgt.
	"""
	N,M = coefficient.shape #N = heigth M = width
	output = np.zeros((N,M), dtype="int")
	for m in range(M): #m = width = x
		for n in range(N): #n=height = y
			sum = 0.0
			for k in range(M):
				for l in range(N):
					value = coefficient[l][k]
					exponent = cmath.exp(1j*2*pi*(float(k * m) / M + float(l * n) / N))
					sum += value * exponent
			output[n][m] = int(sum.real + 0.5) #+0.5 wegen rundungsfe
	return output	

