"""
This python code will read a noisy
EKG signal from a already made wave file
reduce the noise using a notch filter center
50Hz
"""

import wave
import matplotlib.pyplot as plt
import numpy as np


def lowpassFFT(signal, rate, cutoff):
    """Lowpass a signal using FFT/iFFT"""

    """
    This function computes the one-dimensional n-point discrete
    Fourier Transform with the efficient FFT algorithm
    The output of the function is a complex ndArray of complex conjugates

    fft = np.fft.fft(signal)
    for f in fft:
        print(fft)
    """
    fft = np.fft.fft(signal)

    """ 
        This function returns the Discrete Fourier Transforms
        Sample Frequencies which contains the frequency bin center in cycler per unit
        of the sample spacing with zeros at the start
        This function takes the array length and its sample right in Hz
        Afterwards it returns the a array containing the sample frequnecys
        
        So if you design a filter with cutoff at 100Hz and 1kHz sampling rate, 
        then you are really designing for a normalized cutoff frequency f/fs of 1/10 and 
        whatever the processing rate (ie. the sampling rate of the processed signal), the cutoff will 
        always be 1/10 times the processing rate. If you design a similar filter with cutoff at 200Hz 
        and 2kHz sampling rate, then you will get the same filter.
        Now, if you want to filter a signal sampled at 1kHz and you want the cutoff to be 100Hz, then 
        you need to design a filter with a normalized cutoff frequency of 1/10. If you use the same filter on 
        a signal sampled at 2kHz, then the cutoff will be at 200Hz. If you want to keep the cutoff at 100Hz 
        for the 2kHz signal as well, then you need a different filter, this time for a (normalized) frequency 
        of 1/20 instead.

    The filter coefficients don't carry any information about the sampling rate, but rather everything is always 
    relative to the sampling rate of the signal you are filtering and this applies to all digital filters, 
    whatever the design method and whether FIR and IIR.
    
    """

    # This function gives me the x-asias of the Fourier transformation
    # Which then gets sampled into a four loop and if the fre

    fftfreq = np.fft.fftfreq(len(signal), 1 / rate, )
    fftfreq = np.abs(fftfreq)

    for i, freq in enumerate(fftfreq):
        if abs(freq) >= cutoff:
            fft[i] = 0

    signal = np.fft.ifft(fft)

    return signal


def highpassFFT(signal, rate, cutoff):
    """HighPass Filter a signal using FFT/iFFT"""

    """
    This function computes the one-dimensional n-point discrete
    Fourier Transform with the efficient FFT algorithm
    The output of the function is a complex ndArray of complex conjugates

    fft = np.fft.fft(signal)
    for f in fft:
        print(fft)
    """
    fft = np.fft.fft(signal)

    """ 
        This function returns the Discrete Fourier Transforms
        Sample Frequencies which contains the frequency bin center in cycler per unit
        of the sample spacing with zeros at the start
        This function takes the array length and its sample right in Hz
        Afterwards it returns the a array containing the sample frequnecys
        
        So if you design a filter with cutoff at 100Hz and 1kHz sampling rate, 
        then you are really designing for a normalized cutoff frequency f/fs of 1/10 and 
        whatever the processing rate (ie. the sampling rate of the processed signal), the cutoff will 
        always be 1/10 times the processing rate. If you design a similar filter with cutoff at 200Hz 
        and 2kHz sampling rate, then you will get the same filter.
        Now, if you want to filter a signal sampled at 1kHz and you want the cutoff to be 100Hz, then 
        you need to design a filter with a normalized cutoff frequency of 1/10. If you use the same filter on 
        a signal sampled at 2kHz, then the cutoff will be at 200Hz. If you want to keep the cutoff at 100Hz 
        for the 2kHz signal as well, then you need a different filter, this time for a (normalized) frequency 
        of 1/20 instead.

    The filter coefficients don't carry any information about the sampling rate, but rather everything is always 
    relative to the sampling rate of the signal you are filtering and this applies to all digital filters, 
    whatever the design method and whether FIR and IIR.
    
    """

    # This function gives me the x-asias of the Fourier transformation
    # Which then gets sampled into a four loop and if the fre

    fftfreq = np.fft.fftfreq(len(signal), 1 / rate)
    fftfreq = np.abs(fftfreq)
    for i, freq in enumerate(fftfreq):
        if abs(freq) <= cutoff:
            fft[i] = 0
    signal = np.fft.ifft(fft)
    return signal


def notchFFT(signal, rate, L_cutoff, H_cuttoff):
    """Notch Filter a signal using FFT/iFFT"""

    """
    This function computes the one-dimensional n-point discrete
    Fourier Transform with the efficient FFT algorithm
    The output of the function is a complex ndArray of complex conjugates

    fft = np.fft.fft(signal)
    for f in fft:
        print(fft)
    """
    fft = np.fft.fft(signal)

    """ 
        This function returns the Discrete Fourier Transforms
        Sample Frequencies which contains the frequency bin center in cycler per unit
        of the sample spacing with zeros at the start
        This function takes the array length and its sample right in Hz
        Afterwards it returns the a array containing the sample frequnecys
        
        So if you design a filter with cutoff at 100Hz and 1kHz sampling rate, 
        then you are really designing for a normalized cutoff frequency f/fs of 1/10 and 
        whatever the processing rate (ie. the sampling rate of the processed signal), the cutoff will 
        always be 1/10 times the processing rate. If you design a similar filter with cutoff at 200Hz 
        and 2kHz sampling rate, then you will get the same filter.
        Now, if you want to filter a signal sampled at 1kHz and you want the cutoff to be 100Hz, then 
        you need to design a filter with a normalized cutoff frequency of 1/10. If you use the same filter on 
        a signal sampled at 2kHz, then the cutoff will be at 200Hz. If you want to keep the cutoff at 100Hz 
        for the 2kHz signal as well, then you need a different filter, this time for a (normalized) frequency 
        of 1/20 instead.

    The filter coefficients don't carry any information about the sampling rate, but rather everything is always 
    relative to the sampling rate of the signal you are filtering and this applies to all digital filters, 
    whatever the design method and whether FIR and IIR.
    
    """

    # This function gives me the x-asias of the Fourier transformation
    # Which then gets sampled into a four loop and if the fre

    fftfreq = np.fft.fftfreq(len(signal), 1 / rate)
    fftfreq = np.abs(fftfreq)

    for i, freq in enumerate(fftfreq):
        if L_cutoff <= abs(freq) <= H_cuttoff:
            fft[i] = 0
    signal = np.fft.ifft(fft)

    return signal


def Power_FFT(data, rate):
    """given some data points and a rate, return [freq,power]"""
    data = data * np.hamming(len(data))

    # signal of complex value and data
    fft = 10 * np.log10(np.fft.fft(data))
    # convert the fft into the absolute maxiumum of the freuqnecys
    fft = np.abs(fft)

    fftfreq = np.fft.fftfreq(len(data), 1 / rate) * 10
    fftfreq = abs(fftfreq)

    return fftfreq, fft


def FFT(data, rate):
    data = data * np.hamming(len(data))

    # signal of complex value and data 
    fft = np.fft.fft(data)
    # convert the fft into the absolute maxiumum of the freuqnecys
    fft = np.abs(fft)

    fftfreq = np.fft.fftfreq(len(data), 1 / rate)
    fftfreq = np.abs(fftfreq)

    return fftfreq, fft


if __name__ == "__main__":
    # load ecg data from the WAV File
    wf = wave.open("Imports/data_ecg.wav")
    RATE = 24000
    assert wf.getnchannels != 2, "WAV must be mono"
    PCM = np.fromstring(wf.readframes(-1), np.int32)

    # invert waveform
    PCM *= -1

    # create a time series to match the PCM series
    Xs = (np.arange(len(PCM)))/RATE

    """ 
    According to the wave documentation, it explains "Reads and returns at most n frames of audio, as a bytes object."
    How does the number of frames affect the audio that is being played? What is then the best number to assign to n?
    Overall the data of the Wave file is stored within an two different arrays
    function: wf.readframes(-1)
    Quality is affected by the frame rate (sampling rate), 
    sample width and the number of channels. 
    These parameters affect the number of frames that comprise the data portion of the wav file.
    Each frame contains getsampwidth() * getnchannels() bytes. The duration of the audio file in seconds will be the 
    total number of frames divided by the frame rate and this is waveform then gets created into an array with 
    each index of the array being int32
    This array is called the Pulse-Code modulation 
    which is a digital method to represent sampled analog signals
    Where the amplitude of the analog signal is sampled at regulararly uniform interviews
    
    The Xs is the time series for each sampled PCM that was captured.
    """

    Ys = lowpassFFT(PCM, RATE, 900)
    YYs = highpassFFT(PCM, RATE, 950)

    Zs = highpassFFT(Ys, RATE, 20)
    Zs = notchFFT(Zs, RATE, 45, 65)

    notch = notchFFT(PCM, RATE, 800, 1000)

    """
    # plot the data
    plt.figure(figsize=(8, 3))
    plt.plot(Xs, Ys, lw=.5, color='r', label="LowPass Filter")
    plt.plot(Xs, PCM, lw=.5, color='y', label="orginal")
    plt.plot(Xs, YYs, lw=.5, color='g', label="HighPass Filter")
    plt.plot(Xs, notch, lw=.5, color='b', label="notch")
    plt.axis([5.3, 8.5, None, None])
    # style the plot
    plt.axis('on')
    plt.margins(0, .05)
    plt.tight_layout()
    plt.legend()
    plt.show()

    # plot the data
    plt.figure(figsize=(8, 3))
    plt.plot(Xs, PCM, lw=.5, color='b', label="original")
    plt.plot(Xs, Zs, lw=.5, color='r', label="Fill Filtered")
    plt.axis([5.3, 10.5, None, None])
    # style the plot
    plt.axis('on')
    plt.margins(0, .05)
    plt.tight_layout()
    plt.legend()
    plt.show()
    """

    plt.figure(figsize=(8, 3))
    plt.plot(Xs, PCM, lw=.5, color='r', label="orginal")
    plt.plot(Xs, Ys, lw=.5, color='b', label="Low Pass filter")
    plt.plot(Xs, YYs, lw=.5, color='y', label="High Pass filter")
    plt.plot(Xs, notch, lw=.5, color='g', label="Band Pass filter")
    plt.axis([0, 1, None, None])
    # style the plot
    plt.axis('on')
    plt.margins(0, .05)
    plt.tight_layout()
    plt.show()

    """Plotting the foueir transform of the signal using numpy"""
    x, y = FFT(PCM, RATE)

    # plot the data
    plt.figure(figsize=(8, 3))
    plt.plot(x, y, lw=.5, color='b', label="Fouer Transiform")
    plt.axis([0, 3000, None, None])
    plt.axis('on')
    plt.margins(0, .05)
    plt.tight_layout()
    plt.show()
