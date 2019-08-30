conda activate sangfroisEnv


ipython

import numpy as np
import matplotlib.pyplot as plt
import neurokit as nk
import biosppy as bio
from scipy.stats import moment
from scipy import signal

## import data
ecg_fmri=np.loadtxt('C:/Users/Sangfrois/Desktop/NeuroMod_tests/samples-data/ecg_ocean11.txt')
ecg_clean=np.loadtxt('C:/Users/Sangfrois/Desktop/NeuroMod_tests/samples-data/ecg_ocean11_clean.txt')
ecg_mock=np.loadtxt('C:/Users/Sangfrois/Desktop/NeuroMod_tests/mockExperiment/mockExp_sangfroisPart2.txt')

plt.plot(ecg_clean)

#### MOCK EXPERIMENT SIGNAL
## Preprocess and variables 
ecg_fmri_preproc=nk.ecg_preprocess(ecg_fmri, sampling_rate=5000, filter_type="FIR", filter_band="bandpass", filter_frequency=[3, 17], filter_order=0.3, segmenter="pekkanen")


ecg_preproc_df['df'].keys() # raw and filtered signal

ecg_target_df=ecg_preproc_df['ECG'] # extracted peaks and waveforms

rpeaks=ecg_target_df['R_Peaks']

# cardiac cycles
cardiac_cycles=ecg_target_df['Cardiac_Cycles']
plt.plot(cardiac_cycles)

tmp=cardiac_cycles.transpose()
plt.plot(np.mean(tmp))
# complexity measures
hrv_features=nk.ecg_hrv(rpeaks, sampling_rate=10000, hrv_features=['nonlinear', 'frequency'])


#### SCANNEROFF SIGNAL
## Resampling and 
data_sample=ecg_clean[:14900]



## Filter design

medfiltered=scipy.signal.medfilt()

time_window = 100
for time_window in range (0, len(data_sample), 10)
	kurtosis=moment(data_sample[:time_window],moment =4)
	if kurtosis < 3


