#functions for extracting features from audio signals
from scipy import *
import numpy as np
from rect import halfWave

def hfc(x):
    raise NotImplementedError()

def RMS(x):
    raise NotImplementedError()

def threeBandRMS(x):
    raise NotImplementedError()

def crestFactor(x):
    raise NotImplementedError()

def temporalCentroid():
    raise NotImplementedError()

def spectralTemproid():
    raise NotImplementedError()

def spectralKurtosis():
    raise NotImplementedError()

def spectralSkewness():
    raise NotImplementedError()

def spectralRolloff():
    raise NotImplementedError()

def spectralFlux(x, hop=None):

    """
    A function for detecting the amount of relitive energy change in a signal
    -------------------
    Variables :
    ----------------------
    x     :   the input array of data
    hop   :   the number of samples to analyze at once
    ----------------------
    Returns
    ----------------------
    flux  :   the spectral flux of the signal
    ----------------------
    """
    if (hop == None):
        hop = 100
    flux = envelope(x, hop)

    x = halfWave(x)
    aver = flux[0]
    for i in range (hop, len(x) - hop, hop):
        flux[i:i+hop] = np.abs(flux[i] - flux[i+hop])
    return flux

def complexNovelty(x):
    """
    -------------------
    Variables :
    ----------------------
    ----------------------
    Returns
    ----------------------
    """
    raise NotImplementedError()

def zeroCrossingRate(x, srate = 44100):
    crossingCount = 0

    crossings = np.zeros(len(x))
    for i in range (1, len(x)):
        if ((x[i] > 0) & (x[i-1] <= 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1
        if ((x[i] < 0) & (x[i-1] > 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1

    print(crossingCount*len(x)/srate/2)
    return crossings

def envelope(x, binSize=None):
    """
    function for determining the overall amplitude envelope of a signal
    -------------------
    Variables :
    ----------------------
    x         :  incoming array of audio data (or data in general
    binSize   :  the amount of samples processed at a time
    ----------------------
    Returns
    ----------------------
    x         :  an array containing the envelope data
    """
    if (binSize == None):
        binSize = 2200
    for i in range(0,len(x)-binSize,binSize):
        maxi = 0.0
        for j in range (i,i+binSize):
            if (x[j] > maxi):
                maxi = x[j]
        for i in range(i,i+binSize):
            x[i] = maxi
    return x

def flatness(x):
    256, 128, 64, 32, 16, 8, 4, 2
    X1 = x[:128,:]
    X2 = x[128:256,:]
    X3 = x[256:,:]

    K1 = X1.shape[0]
    GeoMean = np.prod(np.abs(X1), axis=0)**(1/K1)
    arithMean = np.sum(np.abs(X1), axis=0)/K1

    flat1 = geoMean/arithMean#the flatness for the first bin
