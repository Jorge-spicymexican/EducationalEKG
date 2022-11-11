import tkinter as tk


read_info = """Welcome to DIY-ECG Waveform analyzer.Coded in python!\nThis page is for instructions on the application!
        Supplies needed:
            ECK Circuit
            Electrodes pads and Electrodes wires
            Audio Jack 
            Computer with DIY-ECK App \n(1) Setup ECK Circuit and connect electrodes w/ pads to the \n    Circuit.\n(2) Locate your audio jack port for Computer and ECG \n    circuit and connect components.\n(3) In the app insert your name and Date.\n(4) Select your digital filter, these filters are digital \n    programmed to eliminate any noise that you may \n    experience each designed specifically for ECGs. \n    More information about the filters can be found\n
            About->About Filter\n\nNOTE: The ECG Circuit can also implement analog a low pass \t\t and high pass filter using the buttons to select.\n\n(5)Select file path for any waveforms you may want to \n   capture. This feature can be disabled in:
             Scope->Save Waveforms.\n   This is automatically off whenever you state the app.\n(6)Finally Start Graph  
        """

author_info = """
Jorge Jurado-Garcia is a student in Milwaukee School of Engineering (MSOE).\nWhere he is pursing a degree in Electrical Engineering with an emphassis in Analog Electronics and DSP. After College \nJorge hopes to pusure a masters degree in Marquette or \nUW-Madison for a speciality in digital filters.\n\nDuring his Free time Jorge likes to learn python and build projects for his youtube channel.\n 
Expected year to of graduation is 2023.
"""

filter_info = """
In signal processing, a filter is a device or process that removes some unwanted components or features from a signal. Filtering is a class of signal processing, the defining 
feature of filters being the complete or partial 
suppression of some aspect of the signal. Most often, 
this means removing some frequencies or frequency bands. 
However, filters do not exclusively act in the frequency 
domain; especially in the field of image processing many 
other targets for filtering exist. Correlations can be 
removed for certain frequency components and not for 
others without having to act in the frequency domain. 
Filters are widely used in electronics & telecommunication, 
This includes radio, television, audio recording, radar, 
control systems, music synthesis, & image processing.
\n
An active filter is a type of analog circuit implementing 
an electronic filter using active components,(amplifier).
Amplifiers included in a filter design can be used to 
improve the cost, performance and predictability of the 
filter. An amplifier prevents the load impedance of the 
following stage from affecting the characteristics of 
the filter. An active filter can have complex poles 
and zeros without using a bulky or expensive inductor. 
The shape of the response, the Q (quality factor), and 
the tuned frequency can often be set with inexpensive 
variable resistors. In some active filter circuits, one
parameter can be adjusted without affecting the others.

High-Pass/LowPass Filter
A high-pass filter (HPF) is an electronic filter that 
passes signals with a frequency higher than a certain 
cutoff frequency and attenuates signals with 
frequencies lower than the cutoff frequency.The amount 
of attenuation for each frequency depends on the filter 
design. A high-pass filter is usually modeled as a 
linear time-invariant system. It is sometimes called a 
low-cut filter or bass-cut filter in the context of 
audio engineering.[1] High-pass filters have many uses,
such as blocking DC from circuitry sensitive to non-zero
average voltages or radio frequency devices. They can 
also be used in conjunction with a low-pass filter to 
produce a bandpass filter.In the optical domain filters 
are often characterised by wavelength rather than frequency 
High-pass and low-pass have the opposite meanings, with a 
"high-pass" filter (more commonly "long-pass") passing only 
longer wavelengths (lower frequencies), and vice versa for
"low-pass" (more commonly "short-pass").

Notch Filer
n signal processing, a band-stop filter or band-rejection 
filter is a filter that passes most frequencies unaltered,
but attenuates those in a specific range to very low 
levels. It is the opposite of a band-pass filter. A notch
filter is a band-stop filter with a narrow stopband (high 
Q factor).Other names include "band limit filter", 
"T-notch filter", "band-elimination filter", and "band-
reject filter".Typically, the width of the stopband is 
1 to 2 decades (that is, the highest frequency attenuated 
is 10 to 100 times the lowest frequency attenuated). 
However, in the audio band, a notch filter has high and 
low frequencies that may be only semitones apart.
"""

ecg_info = """
An electrocardiogram records the electrical signals in your 
heart. It's a common and painless test used to quickly 
detect heart problems and monitor your heart's health.
Electrocardiograms — also called ECGs or EKGs — are often 
done in a doctor's office, a clinic or a hospital room. ECG 
machines are standard equipment in operating rooms and 
ambulances. Some personal devices, such as smart watches, 
offer ECG monitoring.

An electrocardiogram is a painless, noninvasive way to help 
diagnose many common heart problems in people of all ages. 
Your doctor may use an ECG to determine or detect:

Abnormal heart rhythm (arrhythmias)
* If blocked or narrowed arteries in your heart 
* Whether you have had a previous heart attack
* How well certain heart disease treatments, such as a
  pacemaker.

You may need an ECG if you have the following:
* Chest pain
* Dizziness, lightheadedness or confusion
* Heart palpitations
* Rapid pulse
* Shortness of breath
* Weakness, fatigue or a decline in ability to exercise

The American Heart Association doesn't recommend using 
electrocardiograms to assess adults at low risk who don't
have symptoms. But if you have a family history of heart 
disease, your doctor may suggest an electrocardiogram as a 
screening test, even if you have no symptoms.

If your symptoms tend to come and go, they may not be 
captured during a standard ECG recording. In this case 
your doctor may recommend remote or continuous monitoring.
There are several different types.

This program micks a - Holter monitor. 
A Holter monitor is a small, wearable device that records 
a continuous ECG, usually for 24 to 48 hours. It can also 
automatically record when an abnormal rhythm is detected.
"""

def text_window(str,info):
    win = tk.Toplevel()

    window_width = 500
    window_height = 350

    # get screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # create the screen on window console
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    win.title(str)
    win.resizable(False, False)
    win.iconbitmap('./Imports/msoe.ico')
    win.attributes('-topmost', 1)

    # create a text widget and specifiy size
    T = tk.Text(win, height=18, width=70)

    # create a label
    l = tk.Label(win, text=str)
    l.config(font=("Courier", 16))

    # create an exit button
    b_exit = tk.Button(win, text="Exit", command=win.destroy)

    # create a Scrollbar and associate it with txt
    scrollb = tk.Scrollbar(win, command=T.yview)
    l.pack(side=tk.TOP)
    scrollb.pack(side=tk.RIGHT)
    T.pack()
    T.insert(tk.END, info)
    b_exit.pack()