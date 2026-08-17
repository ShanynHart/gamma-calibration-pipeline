import csv
import pandas as pd
import sys
import ROOT
from pathlib import Path
from matplotlib import pyplot as plt
import random
import numpy as np
import os

########################
#HOW TO RUN: ~/miniconda/envs/my_root_env/bin/python Palmtop_AllDetectors_DAT2ROOT_Calibrate.py ../../../PANGoLINS/Measurements/DetectorAssemblies/SrI2/sn230912-04/
# ______________________________________________________________________________
# Read in data
dir_path = sys.argv[1]
calib_dir = Path(dir_path + 'calibrated/')
residuals_dir = Path(dir_path + 'residuals/')

if calib_dir.exists():
    print('\nThe directory {} already exists.'.format(calib_dir))
else:
    calib_dir.mkdir(parents=True, exist_ok=False)
    print('\nThe directory {} was created.'.format(calib_dir))

if residuals_dir.exists():
    print('\nThe directory {} already exists.'.format(residuals_dir))
else:
    residuals_dir.mkdir(parents=True, exist_ok=False)
    print('\nThe directory {} was created.'.format(residuals_dir))

rnd = random.Random()  
r = ROOT.TRandom3(1)

# Process all files in the directory
for file_path in Path(dir_path).glob('*.mca'):
    # ______________________________________________________________________________
    df = []
    with open(file_path, 'r') as f:
        # read all lines of the file from start to end
        lines = f.readlines()[16:-8]
        # delete the first 12 lines
        #lines = f.readlines() 
        data = []
        for line in lines:
            data.append(float(line.strip()))      
        df.append(data)

    df = pd.DataFrame(df)
    df = df.transpose()
    df.columns = ['Counts']
    # df = df.loc[(df['Counts'] > 0)]
    df = df.reset_index(drop=True)

    # ______________________________________________________________________________ residuals
    name = file_path.stem
    
    # xtract the folder name from the second last folder in the path
    date = file_path.parts[-3]

    # print the folder name
    print(' ')
    print(' ')
    print('Detector: {}'.format(file_path.parts[-2]))
    print(' ')
    print('Date: {}'.format(date))
    print(' ')
    print('R-value: {}'.format(file_path.parts[-1].split('.')[0]))
    print(' ')
    print(' ')

    detector = file_path.parts[-2]
    Rvalue = file_path.parts[-1].split('.')[0]
    
    if detector == 'sn230913-03': #CLYC #Palmtop_R6
        energy = [0,661.66, 1173.2, 1332.5]
        if date == '08052024':
            if Rvalue == 'palmtop_R6':
                channels = [0,2747, 4793, 5398]
            elif Rvalue == 'palmtop_R11':
                channels = [0,3326, 5799, 6536]
            elif Rvalue == 'palmtop_R10':
                channels = [0,1078, 1875, 2124]
            else :
                print('R-value does not have calibration data. Skipping')
                continue
    elif detector == 'sn230913-04': #CLYC #DO THIS MEASUREMENT
        energy = [0,661.66, 1173.2, 1332.5]
        continue
    elif detector == 'sn230824-04': #LaBr3  #DO THIS MEASUREMENT
        energy = [0,661.66, 1173.2, 1332.5]
        continue
    elif detector == 'sn230824-05': #LaBr3 #Palmtop_R5
        energy = [0,661.66, 1173.2, 1332.5]
        channels = [0,3930,5907,6361]
    elif detector == 'sn230912-04': #SrI2 #Palmtop_R3
        energy = [0,661.66, 1173.2, 1332.5]
        channels = [0,3084,5291,5914]
    elif detector == 'sn230912-05': #SrI2 #Palmtop_R13
        energy = [0,661.66, 1173.2, 1332.5]
        #channels = [0,2979,4939,5541]
        channels = [0,2748,4709,5299]
    elif detector == 'sn250219-03': #LaBr3Ce /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_300s_137Cs_sn250219-03_0p5us_20coarsegain':
            channels = [0,4560] # 0.5 us
        elif Rvalue == 'palmtop_300s_137Cs_sn250219-03_1us_3coarsegain':
            channels = [0,4560] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250219-03_noamplifier_2p5V':
            channels = [0,2321] # 0.5 us
        elif Rvalue == 'palmtop_300s_137Cs_sn250219-03_noamplifier_10V':
            channels = [0,529] 
    elif detector == 'sn250407-01': #LaBr3Ce /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_300s_137Cs_sn250407-01_0p5us_20coarsegain':
            channels = [0,4096] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-01_1us_23coarsegain':
            channels = [0,3850] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-01_noamplifier_2p5V':
            channels = [0,2129] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-01_noamplifier_10V':
            channels = [0,518] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-01_1us_12coarsegain_07102025':
            channels = [0,3798.78] 
        elif Rvalue == 'palmtop_197s_137Cs_sn250407-01_differntamp_10V_16gain_1us':
            channels = [0,4142]
        elif Rvalue == 'palmtop_172s_137Cs_sn250407-01_differntamp_10V_16gain_1us':
            channels = [0,3980]
    elif detector == 'sn250407-02': #LaBr3Ce /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_400s_137Cs_sn250407-02_0p5us_0coarsegain':
            channels = [0,4096] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-02_1us_4coarsegain':
            channels = [0,4.70804e+03] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-02_noamplifier_2p5V':
            channels = [0,2211] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-02_noamplifier_10V':
            channels = [0,498] 
    elif detector == 'sn250407-03': #LaBr3Ce /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_400s_137Cs_sn250407-03_0p5us_0coarsegain':
            channels = [0,4314] # 0.5 us
        if Rvalue == 'palmtop_300s_137Cs_sn250407-03_1us_4coarsegain':
            channels = [0,4696] # 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-03_noamplifier_2p5V':
            channels = [0,2074] # 0.5 us
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-03_noamplifier_10V':
            channels = [0,464] # 
    elif detector == 'sn250407-04': #CLYC /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_300s_137Cs_sn250407-04_2us_140coarsegain':
            channels = [0,4123] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-04_3us_160coarsegain':
            channels = [0,4327] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-04_6us_320coarsegain':
            channels = [0,4396] 
    elif detector == 'sn250407-05': #CLYC /Users/shanyn/Documents/PhD/Exp/2025/23042025
        energy = [0,661.66]
        if Rvalue == 'palmtop_300s_137Cs_sn250407-05_2us_155coarsegain':
            channels = [0,4423] 
        elif Rvalue == 'palmtop_300s_137Cs_sn250407-05_3us_180coarsegain':
            channels = [0,4478] 
        elif Rvalue == 'palmtop_R9':
            channels = [0,1488] 
    
    elif detector == 'sn250109-10': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4049]
    elif detector == 'NewFolder': #LaBr3Ce
        energy = [0,661.66]
        channels = [0, 4072]
    elif detector == 'sn250219-01': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4373] 
    elif detector == 'sn250219-02': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4257]
    elif detector == 'sn250219-06': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4257]
    elif detector == 'sn250109-03': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4234]
    elif detector == 'sn250109-09': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4165]
    elif detector == 'sn250109-01': #LaBr3Ce
        energy = [0,661.66]
        channels = [0,4211]
    elif detector == 'sn250218-07': #nEL CLYC 
        energy = [0,661.66]
        channels = [0,3725]
    elif detector == 'sn250218-04': #nEL CLYC  
        energy = [0,661.66]
        channels = [0,3725]
    elif detector == 'sn250218-05': #nEL CLYC  
        energy = [0,661.66]
        channels = [0,3309]
    elif detector == 'sn250218-06': #nEL CLYC 
        energy = [0,661.66]
        channels = [0,3401]
    elif detector == 'sn250218-08': #nEL CLYC 
        energy = [0,661.66]
        channels = [0,3586]
    elif detector == 'sn250218-09': #nEL CLYC 
        energy = [0,661.66]
        channels = [0,3656]
    elif detector == 'sn250218-03': #nEL CLYC 
        energy = [0,661.66]
        channels = [0,4049]
    
    else :
        print('Detector not defined in the code. Exiting.')
        break

    scale = channels[1]/energy[1]


    residuals1 = []
    x = ROOT.TCanvas("c", "c", 800, 600)
    x.SetGrid()
    pol1 = ROOT.TF1("pol1", "pol1", 0, 2000)
    pol2 = ROOT.TF1("pol2", "pol2", 0, 2000)
    pol3 = ROOT.TF1("pol3", "pol3", 0, 2000)

    pol1.FixParameter(0, 0)
    pol2.FixParameter(0, 0)
    pol3.FixParameter(0, 0)

    h = ROOT.TH2D("h", "h", 8000,0,8000,2000,0,2000)
    for i in range(len(energy)):
        h.Fill(channels[i], energy[i])
    h.Draw()
    h.GetXaxis().SetTitle("Channel (a.u.)")
    h.GetYaxis().SetTitle("Energy (keV)")
    h.Fit("pol1")
    h.GetFunction("pol1").SetLineColor(2)
    h.GetFunction("pol1").SetLineWidth(1)
    h.GetFunction("pol1").Draw("same")
    h.SetStats(0)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(2)
    h.SetMarkerColor(1)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.GetXaxis().SetTitleOffset(0.8)
    h.GetYaxis().SetTitleOffset(0.8)
    h.GetXaxis().SetTitleFont(22)
    h.GetYaxis().SetTitleFont(22)
    h.GetXaxis().SetLabelFont(132)
    h.GetYaxis().SetLabelFont(132)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    x.Update()
    x.SaveAs(str(residuals_dir / (name + '_pol1_fit.root')))
    x.SaveAs(str(residuals_dir / (name + '_pol1_fit.png')))
    x.Close()

    pol1_params = []
    for i in range(2):
        pol1_params.append(h.GetFunction("pol1").GetParameter(i))
    for i in range(len(energy)):
        residuals1.append([energy[i] - (pol1_params[0] + pol1_params[1]*channels[i])])
    with open(str(residuals_dir / (name + '_pol1_residuals.txt')), 'w') as f:
        for item in residuals1:
            f.write("%s\n" % item)
    print('Residuals saved to {}'.format(residuals_dir / (name + '_pol1_residuals.txt')))

    x1 = ROOT.TCanvas("c1", "c1", 800, 600)
    x1.SetGrid()
    h1 = ROOT.TH2D("h1", "h1", 2000, 0, 2000, 20, -10, 10)
    for i in range(len(energy)):
        h1.Fill(energy[i], residuals1[i][0])
    h1.Draw()
    h1.GetXaxis().SetTitle("Energy (keV)")
    h1.GetYaxis().SetTitle("Residuals (keV)")
    h1.SetStats(0)
    h1.SetMarkerStyle(20)
    h1.SetMarkerSize(2)
    x1.Update()
    x1.SaveAs(str(residuals_dir / (name + '_pol1_residuals.root')))
    x1.SaveAs(str(residuals_dir / (name + '_pol1_residuals.png')))
    x1.Close()

    residuals2 = []
    x2 = ROOT.TCanvas("c2", "c2", 800, 600)
    x2.SetGrid()
    h2 = ROOT.TH2D("h2", "h2", 8000,0,8000,2000,0,2000)
    for i in range(len(energy)):
        h2.Fill(channels[i], energy[i])
    h2.Draw()
    h2.GetXaxis().SetTitle("Channel (a.u.)")
    h2.GetYaxis().SetTitle("Energy (keV)")
    h2.Fit("pol2")
    h2.GetFunction("pol2").SetLineColor(2)
    h2.GetFunction("pol2").SetLineWidth(1)
    h2.GetFunction("pol2").Draw("same")
    h2.SetStats(0)
    h2.SetMarkerStyle(20)
    h2.SetMarkerSize(2)
    h2.SetMarkerColor(1)
    x2.Update()
    x2.SaveAs(str(residuals_dir / (name + '_pol2_fit.root')))
    x2.SaveAs(str(residuals_dir / (name + '_pol2_fit.png')))
    x2.Close()

    pol2_params = []
    for i in range(3):
        pol2_params.append(h2.GetFunction("pol2").GetParameter(i))
    for i in range(len(energy)):
        residuals2.append([energy[i] - (pol2_params[0] + pol2_params[1]*channels[i] + pol2_params[2]*channels[i]**2)])
    with open(str(residuals_dir / (name + '_pol2_residuals.txt')), 'w') as f:
        for item in residuals2:
            f.write("%s\n" % item)
    print('Residuals saved to {}'.format(residuals_dir / (name + '_pol2_residuals.txt')))

    x3 = ROOT.TCanvas("c3", "c3", 800, 600)
    x3.SetGrid()
    h3 = ROOT.TH2D("h3", "h3", 2000, 0, 2000, 20, -10, 10)
    for i in range(len(energy)):
        h3.Fill(energy[i], residuals2[i][0])
    h3.Draw()
    h3.GetXaxis().SetTitle("Energy (keV)")
    h3.GetYaxis().SetTitle("Residuals (keV)")
    h3.SetStats(0)
    h3.SetMarkerStyle(20)
    h3.SetMarkerSize(2)
    x3.Update()
    x3.SaveAs(str(residuals_dir / (name + '_pol2_residuals.root')))
    x3.SaveAs(str(residuals_dir / (name + '_pol2_residuals.png')))
    x3.Close()

    residuals3 = []
    x4 = ROOT.TCanvas("c4", "c4", 800, 600)
    x4.SetGrid()
    h4 = ROOT.TH2D("h4", "h4", 8000,0,8000,2000,0,2000)
    for i in range(len(energy)):
        h4.Fill(channels[i], energy[i])
    h4.Draw()
    h4.GetXaxis().SetTitle("Channel (a.u.)")
    h4.GetYaxis().SetTitle("Energy (keV)")
    h4.Fit("pol3")
    h4.GetFunction("pol3").SetLineColor(2)
    h4.GetFunction("pol3").SetLineWidth(1)
    h4.GetFunction("pol3").Draw("same")
    h4.SetStats(0)
    h4.SetMarkerStyle(20)
    h4.SetMarkerSize(2)
    h4.SetMarkerColor(1)
    x4.Update()
    x4.SaveAs(str(residuals_dir / (name + '_pol3_fit.root')))
    x4.SaveAs(str(residuals_dir / (name + '_pol3_fit.png')))
    x4.Close()

    pol3_params = []
    for i in range(4):
        pol3_params.append(h4.GetFunction("pol3").GetParameter(i))
    for i in range(len(energy)):
        residuals3.append([energy[i] - (pol3_params[0] + pol3_params[1]*channels[i] + pol3_params[2]*channels[i]**2 + pol3_params[3]*channels[i]**3)])
    with open(str(residuals_dir / (name + '_pol3_residuals.txt')), 'w') as f:
        for item in residuals3:
            f.write("%s\n" % item)
    print('Residuals saved to {}'.format(residuals_dir / (name + '_pol3_residuals.txt')))

    x5 = ROOT.TCanvas("c5", "c5", 800, 600)
    x5.SetGrid()
    h5 = ROOT.TH2D("h5", "h5", 2000, 0, 2000, 20, -10, 10)
    for i in range(len(energy)):
        h5.Fill(energy[i], residuals3[i][0])
    h5.Draw()
    h5.GetXaxis().SetTitle("Energy (keV)")
    h5.GetYaxis().SetTitle("Residuals (keV)")
    h5.SetStats(0)
    h5.SetMarkerStyle(20)
    h5.SetMarkerSize(2)
    x5.Update()
    x5.SaveAs(str(residuals_dir / (name + '_pol3_residuals.root')))
    x5.SaveAs(str(residuals_dir / (name + '_pol3_residuals.png')))
    x5.Close()

    # ______________________________________________________________________________ best fit
    # Get chi-square values for each fit
    chi2_1 = h.GetFunction("pol1").GetChisquare()
    chi2_2 = h2.GetFunction("pol2").GetChisquare()
    chi2_3 = h4.GetFunction("pol3").GetChisquare()

    # Handle zero chi-square values
    if chi2_1 == 0:
        residuals1 = [np.nan]
    if chi2_2 == 0:
        residuals2 = [np.nan]
    if chi2_3 == 0:
        residuals3 = [np.nan]

    # Determine which polynomial fit has the smallest residuals
    fits = [(residuals1, "pol1"), (residuals2, "pol2"), (residuals3, "pol3")]
    min_fit = min(fits, key=lambda x: sum(abs(val) if isinstance(val, (int, float)) else sum(abs(inner_val) for inner_val in val) for val in x[0]))

    # Print the fit with the smallest residuals
    print(' ')
    print(' ')
    print(f"The {min_fit[1]} fit has the smallest residuals.")
    print(' ')
    print(' ')

    # Assign the best fit function name
    bestfit = min_fit[1]

    # ______________________________________________________________________________ calibration
    # Constants for energy calculation as obtained from the best fit
    
    if min_fit[1] == 'pol1':
        p0 = pol1_params[0]
        p1 = pol1_params[1]
        p2 = 0
        p3 = 0
    elif min_fit[1] == 'pol2':
        p0 = pol2_params[0]
        p1 = pol2_params[1]
        p2 = pol2_params[2]
        p3 = 0
    elif min_fit[1] == 'pol3':
        p0 = pol3_params[0]
        p1 = pol3_params[1]
        p2 = pol3_params[2]
        p3 = pol3_params[3]


    h1 = ROOT.TH1D("h1", "h1", 8000, 0, 8000)
    h1.SetLineColor(1) # red    
    h1.SetLineWidth(1)
    h1.SetStats(0)
    for i in range(len(df)):
        h1.SetBinContent(i, df['Counts'][i])
    h1.Draw()
    h1.GetXaxis().SetTitle("Channel")
    h1.GetYaxis().SetTitle("Counts (a.u.)")

    calibrated = []
    pol1= []
    pol2= []
    pol3= []
    #create a root file with the name str(save_dir / (name + '_3rd_order_calibrated.root'))
    f = ROOT.TFile(str(calib_dir / (name + '_calibrated.root')), "RECREATE")
    h1.Write()
    h = ROOT.TH1D("h", "h", 2000, 0, 2000)
    scale = int(scale)
    scale = scale
    ranges = [-scale, scale]
    for i in range(len(df)):
        eN = h1.GetBinContent(i)
        e = h1.GetBinCenter(i)
        for j in range(int(eN)):
            # generate a random number between -scale and scale
            random = rnd.uniform(ranges[0], ranges[1])
            ea = e 
            ea = p0 + p1*ea + p2*ea**2 + p3*ea**3
            h.Fill(ea+ random)
            calibrated.append([ea, eN])
    h.Draw()
    h.SetLineColor(1) # red
    h.SetLineWidth(1)
    h.SetStats(0)
    h.GetXaxis().SetTitle("Energy (keV)")
    h.GetYaxis().SetTitle("Counts (keV^{-1})")
    h.Write()

    #plot the other not best fit polynomials
    h2 = ROOT.TH1D("h2", "pol1", 2000, 0, 2000)
    h2.SetLineColor(2) # blue
    h2.SetLineWidth(1)
    h2.SetStats(0)
    for i in range(len(df)):
        eN = h1.GetBinContent(i)
        e = h1.GetBinCenter(i)
        for j in range(int(eN)):
            # generate a random number between -scale and scale
            random = rnd.uniform(ranges[0], ranges[1])
            ea = e 
            ea = pol1_params[0] + pol1_params[1]*ea
            h2.Fill(ea+ random)
            pol1.append([ea, eN])
    h2.Draw()
    h2.GetXaxis().SetTitle("Energy (keV)")
    h2.GetYaxis().SetTitle("Counts (keV^{-1})")
    h2.GetXaxis().SetTitleSize(0.06)
    h2.GetYaxis().SetTitleSize(0.06)
    h2.GetXaxis().SetTitleOffset(0.8)
    h2.GetYaxis().SetTitleOffset(0.8)
    h2.GetXaxis().SetTitleFont(22)
    h2.GetYaxis().SetTitleFont(22)
    h2.GetXaxis().SetLabelFont(132)
    h2.GetYaxis().SetLabelFont(132)
    h2.GetXaxis().SetLabelSize(0.05)
    h2.GetYaxis().SetLabelSize(0.05)
    h2.GetXaxis().SetTitleSize(0.06)
    h2.GetYaxis().SetTitleSize(0.06)
    h2.GetXaxis().SetRangeUser(0, 1000)
    h2.Write()

    h6 = ROOT.TH1D("h6", "pol2", 2000, 0, 2000)
    h6.SetLineColor(2) 
    h6.SetLineWidth(1)
    h6.SetStats(0)
    for i in range(len(df)):
        eN = h1.GetBinContent(i)
        e = h1.GetBinCenter(i)
        for j in range(int(eN)):
            # generate a random number between -scale and scale
            random = rnd.uniform(ranges[0], ranges[1])
            ea = e 
            ea = pol2_params[0] + pol2_params[1]*ea + pol2_params[2]*ea**2
            h6.Fill(ea+ random)
            pol2.append([ea, eN])
    h6.Draw()
    h6.GetXaxis().SetTitle("Energy (keV)")
    h6.GetYaxis().SetTitle("Counts (keV^{-1})")
    h6.GetXaxis().SetTitleSize(0.06)
    h6.GetYaxis().SetTitleSize(0.06)
    h6.GetXaxis().SetTitleOffset(0.8)
    h6.GetYaxis().SetTitleOffset(0.8)
    h6.GetXaxis().SetTitleFont(22)
    h6.GetYaxis().SetTitleFont(22)
    h6.GetXaxis().SetLabelFont(132)
    h6.GetYaxis().SetLabelFont(132)
    h6.GetXaxis().SetLabelSize(0.05)
    h6.GetYaxis().SetLabelSize(0.05)
    h6.GetXaxis().SetTitleSize(0.06)
    h6.GetYaxis().SetTitleSize(0.06)
    h6.GetXaxis().SetRangeUser(0, 1000)
    h6.Write()

    h7 = ROOT.TH1D("h7", "pol3", 2000, 0, 2000)
    h7.SetLineColor(2)
    h7.SetLineWidth(1)
    h7.SetStats(0)
    for i in range(len(df)):
        eN = h1.GetBinContent(i)
        e = h1.GetBinCenter(i)
        for j in range(int(eN)):
            # generate a random number between -scale and scale
            random = rnd.uniform(ranges[0], ranges[1])
            ea = e 
            ea = pol3_params[0] + pol3_params[1]*ea + pol3_params[2]*ea**2 + pol3_params[3]*ea**3
            h7.Fill(ea+ random)
            pol3.append([ea, eN])
    h7.Draw()
    h7.GetXaxis().SetTitle("Energy (keV)")
    h7.GetYaxis().SetTitle("Counts (keV^{-1})")
    h7.GetXaxis().SetTitleSize(0.06)
    h7.GetYaxis().SetTitleSize(0.06)
    h7.GetXaxis().SetTitleOffset(0.8)
    h7.GetYaxis().SetTitleOffset(0.8)
    h7.GetXaxis().SetTitleFont(22)
    h7.GetYaxis().SetTitleFont(22)
    h7.GetXaxis().SetLabelFont(132)
    h7.GetYaxis().SetLabelFont(132)
    h7.GetXaxis().SetLabelSize(0.05)
    h7.GetYaxis().SetLabelSize(0.05)
    h7.GetXaxis().SetTitleSize(0.06)
    h7.GetYaxis().SetTitleSize(0.06)
    h7.GetXaxis().SetRangeUser(0, 1000)
    h7.Write()

    f.Close()

    #write the calibrated data to a txt file
    with open(str(calib_dir / (name + '_' + bestfit + '_calibrated.txt')), 'w') as f:
        for item in calibrated:
            f.write("%s\n" % item)
    print('Calibrated data saved to {}'.format(calib_dir / (name + '_' + bestfit + '_calibrated.txt')))

    #write the pol1, pol2, pol3 calibrated histograms to a txt file each in a separate file
    with open(str(calib_dir / (name + '_pol1_calibrated.txt')), 'w') as f:
        for item in pol1:
            f.write("%s\n" % item)
    print('Pol1 calibrated data saved to {}'.format(calib_dir / (name + '_pol1_calibrated.txt')))

    with open(str(calib_dir / (name + '_pol2_calibrated.txt')), 'w') as f:
        for item in pol2:
            f.write("%s\n" % item)
    print('Pol2 calibrated data saved to {}'.format(calib_dir / (name + '_pol2_calibrated.txt')))
    
    with open(str(calib_dir / (name + '_pol3_calibrated.txt')), 'w') as f:
        for item in pol3:
            f.write("%s\n" % item)
    print('Pol3 calibrated data saved to {}'.format(calib_dir / (name + '_pol3_calibrated.txt')))

    # ______________________________________________________________________________

