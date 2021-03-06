# Preprocessing pipeline for ECG signals recorded in fMRI #
This repo details the different preprocessing steps required for denoising and amplification of target signal. 
The aim of this pipeline is to describe signal quality using operational criterion that will categorize the signal as usable or unusable.

From what I understand, there is currently no package available in _python_ that treats fMRI noise on ECG signal. The plan is to eventually add this feature to currently existing biosignal analysis packages.

## Background ##
I'm an undergrad in cognitive neuroscience, currently completing my last credits.
As part of Courtois-Neuromod project, the aim of my subproject is to eventually inform the AI model of physiological modalities. This repo could eventually be merged to the project's GitHub. ![Neuromod](logo-vector-rgb.png)


## Delivrables for brainhack ##
- [x] a markdown file that summarizes the intent of and principal refs for the project
- [x] a flow chart of preprocessing steps
- [x] a markdown detailing each step of the flow chart  in "scripts" directory
- [x] Use the detailed markdown and start a clean jupyter notebook with the code I know I can do, and will stay
- [x] a draft notebook in which I test specific filter design ~~TO BE ADDED AS A NEW FEATURE IN PACKAGE - 4th order central moment~~
	- [ ] Benchmark different basic preprocessing techniques - measure their detection perfo
	- [x] Raise issue on Neurokit's github for help
	- [x] Reach out to the authors who made the higher-order statistics filter design
- [ ] save parsed data in pickle
- [ ] ~~a post on twitter to share my repo, publicize the Montreal brainhack~~



## Python packages used ##
Of course, numpy, pandas, pickle, and matplotlib are imperative for data organization and vizualisation.
Specific packages for biosignal analysis include
* __Neurokit__ [docs](https://www.neurokit.readthedocs.io/en/latest/)
* __BioSPPy__ [docs](https://www.biosppy.readthedocs.io/en/stable/)



## Sources of interference to cancel out ##

### 1. fMRI - gradient artifacts ###
ECG signals recorded in fMRI are principally polluted by gradient artifacts related to the radio-frequency pulse and magnetism of scanner. Echo-planar imaging (brain imaging) uses Gradient-Echo sequences that often include multi-band factor (i.e. multiple slices at a time). Simple maths for a 60-slices sequence with multi-band factor of 4 and 1,490s repetition time : 60/4 = 15 shots per TR. How many gradients are there per TR? 15/1490 = 10.067 Hz. So approximately 100ms separate adjacent gradients.

![ ](https://i.imgur.com/2d9Wf8f.png)

![Polluted ECG](polluted-ecg-example.jpg "polluted ECG")

**This can be handled with 4th order central-moment filter** 

[Reference on this filter design](https://www.ncbi.nlm.nih.gov/pubmed/28981438/)

### 2. Impulsive noise/sudden large shifts in amplitude ###

Other noises include muscle contractions, movements, moving cables. 
**This can be handled by linear interpolation and non linear transformations**


## Preprocessing overview
![overall structure](preproc-flow-chart.jpg)



