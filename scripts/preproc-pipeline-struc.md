# Detailed structure of pipeline #

## 1. Data import ##
**Read BIOPAC files**, e.g. <name-of-file>.acq
BIOPAC has a software called acqknowledge; it allows to record multiple physiological modalities at a time.
Hardware is MR-compatible and recordings can include synchronization signal that specify the time index of each triggers (TTL, or radiofrequency pulse).

___file channels___ : Electrocardiogram, photoplethysmograph, respiration belt, electrodermal activity, and TTL

___neurokit/bioread function for reading .acq file___ : dataframe, sampling-rate = neurokit.read-acknowledge('file.acq', return-sampling-rate=True)

	* returns a pandas object and sampling rate of channels - dataframe.head() to visualize, or .dictkeys() to have the keys
	

## 2. Parse data according to TTL ##
**concatenate data points that correspond to scannerON segments of TTL. Build a pandas object for every block of the experimentation** ; a single block will be treated at a time.

	* Block00 - Clean ECG segments
	* Block01 - fMRI scannerON; 1st block of experiment
	* Blocknn - fMRI scannerON; nth block of experiment

TTL | ECG | PPG | RSP | EDA
----|-----|-----|-----|-----
 0  |  x  |  x  |  x  |  x
 1  |  y  |  y  |  y  |  y
 1  |  y  |  y  |  y  |  y
 0  |  x  |  x  |  x  |  x

Let's say

- [ ] 1st row is a scannerOFF segment :(0) parse and keep this clean segment for direct process, (1) extract cardiac cycles and (2) add/save to quality model, (3) pickle dump dataframe and name block00
	
- [ ] 2nd and 3rd rows are scannerON segments :(0) parse and keep noisy segment for preprocessing, (1) create pandas object containing every channel (2) pickle dump dataframe and name block01 (or blocknn)

_do this for every segment, so_ :

- [ ] ***Build a for loop that passes through TTL channel and that concatenates segments of maximal values while ignoring other segments***

- [ ] Give variable names to each channel, or dict keys.

## 3. Preprocessing blocks of noisy ECG ##
### Steps required ### 
 - [x] Linear interpolation to rescale large shifts in amplitude
 - [ ] 4th order central-moment filter
	1. time window definition: interval between 2 adjacent gradients, approx. a hundred samples
	2. filter design: transfer function that will compute the distribution of amplitudes in sliding time window ecg and normalize it.The following numpy function computes the statistic :
		
		numpy.moment (sample, moment=4)

	3. apply filter to timeseries (blocknn's ecg)

 - [x] Bandpass filter _4th order central-moment filtered ecg_ , or '4th-ecg' - returns 'bp-ecg'
 - [x] Segmenter: pekkanen segmentation based on first-order gaussian differentiaton
 - [ ] Cardiac cycles verification: sklearn functions to minimize mean square error of extracted cardiac cycles over quality
 - [ ] plot results as follows : plot superimposed quality model and extracted cardiac-cycles, plot tachogram that illustrates HRV in time - that allows visual inspection
 - [ ] dump feature data in pickle

***YAY***
