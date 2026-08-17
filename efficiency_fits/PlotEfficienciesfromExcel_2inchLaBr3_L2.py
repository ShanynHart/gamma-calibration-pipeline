import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import ROOT as ROOT
from scipy.optimize import curve_fit

# Data
distances = np.array([10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000,10.0000,30.0000,50.0000,100.0000,200.0000])
energy = np.array([121.7800,121.7800,121.7800,121.7800,121.7800,244.6900,244.6900,244.6900,244.6900,244.6900,344.2800,344.2800,344.2800,344.2800,344.2800,411.1200,411.1200,411.1200,411.1200,411.1200,443.9800,443.9800,443.9800,443.9800,443.9800,778.9000,778.9000,778.9000,778.9000,778.9000,867.4000,867.4000,867.4000,867.4000,867.4000,964.1300,964.1300,964.1300,964.1300,964.1300,1408.0100,1408.0100,1408.0100,1408.0100,1408.0100])
fepe = np.array([6.8245,4.9198,2.5917,1.0751,0.2994,4.9488,3.2556,2.1089,0.9025,0.2624,4.3155,2.7272,1.8498,0.7369,0.2209,3.5927,2.3558,1.5292,0.6131,0.1959,3.3294,2.0859,1.3747,0.5806,0.1809,1.8357,1.1426,0.7818,0.3961,0.1120,1.2613,0.9812,0.6785,0.3250,0.0920,0.9741,0.8840,0.6306,0.2744,0.0851,0.6717,0.7852,0.6174,0.2146,0.0539])
fepe_err = np.array([0.7634,0.5220,0.3850,0.2234,0.0302,0.5538,0.3304,0.2122,0.0907,0.0439,0.4827,0.2766,0.1860,0.0739,0.0227,0.4045,0.2402,0.1550,0.0793,0.0618,0.3743,0.2139,0.1396,0.0648,0.0458,0.2164,0.1166,0.0790,0.0411,0.0184,0.1547,0.1021,0.0695,0.0340,0.0294,0.1187,0.0901,0.0636,0.0281,0.0188,0.0754,0.0797,0.322,0.116,0.182])


def log_function(E, A, B):
    return A * np.log(E) + B

unique_distances = [10, 30, 50, 100, 200]

# Initialize plot
plt.figure(figsize=(12, 8))

# Colors for each distance
colors = ['red', 'blue', 'green', 'black', 'magenta']
labels = ['10 mm', '30 mm', '50 mm', '100 mm', '200 mm']
markers = ['s', 'o', '^', 'D', 'P']
 

h1 = ROOT.TH1F('h1', '10 mm', 1600, 0, 1600)
h2 = ROOT.TH1F('h2', '30 mm', 1600, 0, 1600)
h3 = ROOT.TH1F('h3', '50 mm', 1600, 0, 1600)
h4 = ROOT.TH1F('h4', '100 mm', 1600, 0, 1600)

c1 = ROOT.TCanvas('c1', 'c1', 800, 800)
for i in range(len(distances)):
    if distances[i] == 10:
        h1.Fill(energy[i], fepe[i])
        h1.SetBinError(h1.FindBin(energy[i]), fepe_err[i])
        c1.Draw()
    elif distances[i] == 30:
        h2.Fill(energy[i], fepe[i])
        h2.SetBinError(h2.FindBin(energy[i]), fepe_err[i])
    elif distances[i] == 50:
        h3.Fill(energy[i], fepe[i])
        h3.SetBinError(h3.FindBin(energy[i]), fepe_err[i])
    elif distances[i] == 100:
        h4.Fill(energy[i], fepe[i])
        h4.SetBinError(h4.FindBin(energy[i]), fepe_err[i])
h1.SetMarkerColor(1)#black
h1.GetXaxis().SetTitle('Energy (keV)')
h1.GetYaxis().SetTitle('#epsilon_{abs}')
h1.GetXaxis().SetLabelSize(0.05)
h1.GetYaxis().SetLabelSize(0.05)
h1.GetXaxis().SetTitleSize(0.06)
h1.GetYaxis().SetTitleSize(0.06)
h1.GetXaxis().SetTitleOffset(0.8)
h1.GetYaxis().SetTitleOffset(0.6)
h1.GetXaxis().SetLabelFont(132)
h1.GetYaxis().SetLabelFont(132)
h1.SetTitle('')
h1.SetStats(0)
h2.SetMarkerColor(2) #red
h2.SetStats(0)
h3.SetMarkerColor(6)
h3.SetStats(0)
h4.SetMarkerColor(4) #blue
h4.SetStats(0)
h1.SetMarkerStyle(20)
h2.SetMarkerStyle(21)
h3.SetMarkerStyle(22)
h4.SetMarkerStyle(23)
h1.SetMarkerSize(2)
h2.SetMarkerSize(2)
h3.SetMarkerSize(2)
h4.SetMarkerSize(2)
h1.SetLineColor(1)
h2.SetLineColor(2)
h3.SetLineColor(6)
h4.SetLineColor(4)

TF1 = ROOT.TF1('TF1', '[p0]*(TMath::Log(x)) + [p1]*(TMath::Log(x)*TMath::Log(x)) + [p2]*(TMath::Log(x)*TMath::Log(x)*TMath::Log(x)) + [p3]*(TMath::Log(x)*TMath::Log(x)*TMath::Log(x)*TMath::Log(x)) + [p4]*(TMath::Log(x)*TMath::Log(x)*TMath::Log(x)*TMath::Log(x)*TMath::Log(x))', 50, 1410)
# fit
h1.Fit('TF1', 'R')
h2.Fit('TF1', 'R')
h3.Fit('TF1', 'R')
h4.Fit('TF1', 'R')
h1.Draw()
h2.Draw("same")
h3.Draw("same")
h4.Draw("same")

# Add legend with marker styles and colors
l = ROOT.TLegend(0.1, 0.7, 0.48, 0.9)
l.AddEntry(h1, '10 mm', 'p')
l.AddEntry(h2, '30 mm', 'p')
l.AddEntry(h3, '50 mm', 'p')
l.AddEntry(h4, '100 mm', 'p')
l.SetTextSize(0.06)
l.SetBorderSize(0)
l.SetTextFont(132)
l.Draw("same")
c1.Update()
c1.SaveAs('/Users/shanyn/Documents/PhD/Exp/2024/timing_shaping_characterisation_june2024/Efficiency_2inchLaBr3/Energy_vs_FEPE_ALL.root') 



energy_uct_sources_30mm = np.array([122.0000,511.0000,662.0000,835.0000,1173.2000,1274.0000,1332.5000])
fepe_uct_sources_30mm = np.array([5.0489,2.0555,1.4062,1.1815,0.6005,0.6197,0.5907])
fepe_err_uct_sources_30mm = np.array([0.5274,0.2069,0.1424,0.3500,0.2628,0.1673,0.2600])

# plot energy vs. fepe for 30 mm distance of UCT sources and the distance of 30 mm for fepe using root with error bars
h5 = ROOT.TH1F('h5', '30 mm known activity sources', 1600, 0, 1600)
c2 = ROOT.TCanvas('c2', 'c2', 800, 800)
for i in range(len(energy_uct_sources_30mm)):
    h5.Fill(energy_uct_sources_30mm[i], fepe_uct_sources_30mm[i])
    h5.SetBinError(h5.FindBin(energy_uct_sources_30mm[i]), fepe_err_uct_sources_30mm[i])
    c2.Draw()
h5.SetMarkerColor(1)#black
h5.SetTitle('')
h5.SetStats(0)
h5.GetXaxis().SetTitle('Energy (keV)')
h5.GetYaxis().SetTitle('#epsilon_{abs} (%)')
h5.GetXaxis().SetLabelSize(0.05)
h5.GetYaxis().SetLabelSize(0.05)
h5.GetXaxis().SetTitleSize(0.06)
h5.GetYaxis().SetTitleSize(0.06)
h5.GetXaxis().SetTitleOffset(0.8)
h5.GetYaxis().SetTitleOffset(0.6)
h5.GetXaxis().SetLabelFont(132)
h5.GetYaxis().SetLabelFont(132)
h5.SetMarkerStyle(20)
h5.SetMarkerSize(2)
h5.SetLineColor(1)
h5.Draw()
h2.Draw("same")
l2 = ROOT.TLegend(0.1, 0.7, 0.48, 0.9)
l2.AddEntry(h5, 'Known Activity', 'p')
l2.AddEntry(h2, 'Unknown Activity', 'p')
l2.SetTextSize(0.06)
l2.SetBorderSize(0)
l2.SetTextFont(132)
l2.Draw("same")
c2.Update()
c2.SaveAs('/Users/shanyn/Documents/PhD/Exp/2024/timing_shaping_characterisation_june2024/Efficiency_2inchLaBr3/Energy_vs_FEPE_30mm_UCT_sources.root')

