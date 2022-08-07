# Experimenting with changes in Alex's code

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import fft

from adc import * 

# https://github.com/alexlib/engineering_experiments_measurements_course/blob/master/notebooks/a2d/Reconstruction_periodic_signal_Cardinal_series.ipynb

st.title('ADE solution: diffusion only')

@st.cache
def create_data():
    t = np.linspace(0,10,10000) # almost continuous
    y = t**2
    return (t,y)


t, y = create_data()

fs = st.slider('Sampling frequency (Hz)', 1, 100, 5)
N = st.slider('Number of bits, N', 1, 196, 4)
miny = st.slider('Lowest clipping value (V)', -20, 10, 0)
maxy = st.slider('Highest clipping value (V)', 0, 20, 10)
method = st.radio('Choose the sampling method',('Sample and hold','Zero and hold'))
if method == 'Sample and hold':
    method = 'soh'
else:
    method = 'zoh'

ts,yq,tr,yr = adc(t,y,fs=fs,N=N,miny=miny,maxy=maxy,method=method) # monopolar
fig, ax = plt.subplots(figsize=(6,6))
# ax.plot(t,y,'k--',lw=0.1)
ax.plot(ts,yq,'ro')
ax.plot(tr, yr,'b--',lw=.2)
ax.set_xlabel('$t$ (sec)')
ax.set_ylabel('$y$ (V)')
st.pyplot(fig)

