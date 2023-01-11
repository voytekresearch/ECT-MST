# ECT-MST

`ECT-MST` project repository: investigating the roles of aperiodic activity and slow oscillations in electroconvulsive therapy (ECT) and magnetic seizure therapy (MST) as a treatment for Major Depressive Disorder (MDD)

[![Preprint]()]

## Overview

ECT is an incredibly effective treatment for patients with treatment-resistant depression (TRD), but it is only used as a last-resort treatment due to its stigma and adverse cognitive side effects. MST is a promising alternative treatment with a comparable remission rate and fewer side effects. Despite ECT being introduced to psychiatry more than 80 years ago, we still do not understand its neural mechanisms, although clinical "EEG slowing" has been associated with these treatments for decades. In our previous longitudinal study (Smith et al., 2023),  we found EEG slowing in ECT is better explained by a novel yet unexplored EEG signal: aperiodic activity. 

In this manuscript we replicate and extend these findings, and we identified aperiodic activity as a potential shared therapeutic mechanism in both ECT and MST. We demonstrate this in resting state EEG from two clinical TRD populations receiving ECT (n=22), and MST (n=23) using a novel, robust spectral parameterization method that disambiguates the contributions of aperiodic activity and oscillations to the EEG signal.

## Project Guide

`00-ECT` contains notebooks used to preprocess, analyze, & visualize scalp EEG data from patients who received ECT

`01-MST` contains notebooks used to preprocess, analyze, & visualize scalp EEG data from patients who received MST 

`02-Combined` contains notebooks used to analyze clinical data and run multiple linear regressions using EEG features from both ECT and MST patients


## Reference

This project is described in the following preprint:


## Requirements

This project was written in Python 3 and requires Python >= 3.7 to run.

To re-run this project, you will need some external dependences.

Dependencies include 3rd party scientific Python packages:
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [scipy](https://github.com/scipy/scipy)
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [statsmodels](https://github.com/statsmodels/statsmodels)
- [seaborn](https://github.com/mwaskom/seaborn)


You can get and manage these dependencies using the [Anaconda](https://www.anaconda.com/distribution/) distribution, which we recommend.

In addition, this project requires the following dependencies:

 - [mne](https://github.com/mne-tools/mne-python) >= 0.24.1
 - [fooof](https://github.com/fooof-tools/fooof) >= 1.0.0
 
You can install the extra required dependencies by running:

```
pip install mne, fooof
```


## Data

This project uses data protected under HIPAA and any identifying features have been removed. Data is not available at this time. 
