# Gamma-ray calibration pipeline

Automated energy calibration and detection-efficiency fitting for gamma-ray spectrometers, from my PhD and postdoc work (University of Cape Town / iThemba LABS).

A spectrometer records counts per ADC channel. Before any physics can be done, channel numbers must be mapped to energies (calibration) and the fraction of emitted gammas actually detected must be modelled as a function of energy (efficiency). Both are regression problems with real-world complications: overlapping peaks, drifting gains, and count-rate dependent uncertainties.

## What is here

**`mca_pipeline/`**: `calib_palmtop_DAT2ROOT.py` (about 600 lines) is a complete pipeline for multichannel-analyser data. It reads raw instrument files, locates photopeaks, fits them with Gaussian-plus-background models, performs the channel-to-energy regression across multiple known source lines, propagates fit uncertainties into the calibration parameters, and writes calibrated ROOT histograms. `plot_palmtop_TXT2ROOT.py` handles the text-export variant.

**`efficiency_fits/`**: full-energy-peak efficiency curves for a 2-inch LaBr3:Ce detector. `fitLaBr3Ce2inchEff.C` fits the standard log-polynomial efficiency parameterisation to measured source data; the Python script compares measured efficiencies across detector configurations.

## Methods, in general terms

Peak detection, constrained nonlinear regression, error propagation, model parameterisation choices, and turning a manual lab procedure into a reproducible batch pipeline.

## Author

Shanyn Hart. All code in this repository is my own.
