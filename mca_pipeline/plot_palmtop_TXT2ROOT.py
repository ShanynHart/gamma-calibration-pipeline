import csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import ROOT
from pathlib import Path
import random
import scienceplots

########################
#HOW TO RUN: ~/miniconda/envs/my_root_env/bin/python Palmtop_plot_TXT_as_ROOT.py ../../PANGoLINS/Measurements/DetectorAssemblies/SrI2/sn230912-04/08052024/

# ______________________________________________________________________________
# Read in data
dir_path = sys.argv[1]
save_dir = Path(dir_path )

if save_dir.exists():
    print('\n\nThe directory {} already exists.'.format(save_dir))
else:
    save_dir.mkdir(parents=True, exist_ok=False)
    print('\n\nThe directory {} was created.'.format(save_dir))

# Process all files in the directory
for file_path in Path(dir_path).glob('*.mca'):

    # ______________________________________________________________________________
    df = []
    with open(file_path, 'r') as f:
        lines = f.readlines()[14:-8] 
        data = []
        for line in lines:
            data.append(float(line.strip()))      
        df.append(data)

    df = pd.DataFrame(df)
    df = df.transpose()
    df.columns = ['Channel']
    # df = df.loc[(df['Channel'] > 0)]
    df = df.reset_index(drop=True)

    # ______________________________________________________________________________
    # Calibration
    # energy = 4.969 * channel - 613.2
    # create a random number generator where the random number is between 0 and 1
    rnd = random.Random()
    # generate a random number
    rnd.random()
    rnd.uniform(0, 1)

    # ______________________________________________________________________________
    # Plotting with matplotlib
    name = file_path.stem
    fig = plt.figure(figsize=(10, 8))
    plt.plot(df['Channel'], label='Channel')
    plt.ylabel('Counts', fontsize=22)
    plt.xlabel('Channel', fontsize=22)
    plt.legend(fontsize=22, loc='upper right')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlim(0, 8190)
    plt.style.use(['science','ieee'])
    plt.show()
    plt.savefig(str(save_dir / (name + '.png')))
    plt.close(fig)

    # ______________________________________________________________________________
    # Plotting with ROOT
    c = ROOT.TCanvas("c", "c", 800, 600)
    c.SetGrid()

    # ROOT TH1D histogram
    hist = ROOT.TH1D("hist", "hist", 8190, 0, 8190)
    for i in range(0, 8190):
        hist.SetBinContent(i, df['Channel'][i])
    hist.Draw()
    hist.SetTitle(name)
    hist.GetXaxis().SetTitle("Channel (bin)")
    hist.GetYaxis().SetTitle("Counts (1/bin)")
    c.Update()
    c.SaveAs(str(save_dir / (name + '.root')))
    c.Close()

print("Processing complete.")

