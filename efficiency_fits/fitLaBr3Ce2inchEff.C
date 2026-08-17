#include <TMath.h>
#include <TF1.h>
#include <TGraph.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TH1.h>
#include <TLegend.h>
#include <iostream>
#include <string>

void fitLaBr3Ce2inchEff() {

    const char* dir = "/Users/shanyn/Documents/PhD/Exp/2024/timing_shaping_characterisation_june2024/Efficiency_2inchLaBr3/";
    std::string file1 = std::string(dir) + "Energy_vs_FEPE_ALL.root";
    const char* canvasName1 = "c1"; // Replace with the actual canvas name in the file1
    const char* hist10mm = "h1"; // Efficiency 10mm
    const char* hist30mm = "h2"; // Efficiency 30mm
    const char* hist50mm = "h3"; // Efficiency 50mm
    const char* hist100mm = "h4"; // Efficiency 100mm
    const char* hist200mm = "h5"; // Efficiency 200mm

    TFile *f1 = TFile::Open(file1.c_str());

    if (!f1) {
        std::cerr << "Failed to open file" << std::endl;
        return;
    }

    // Retrieve the canvas
    TCanvas *c1 = (TCanvas*)f1->Get(canvasName1);

    if (!c1) {
        std::cerr << "Failed to get canvas" << std::endl;
        return;
    }

    // Retrieve the histograms from the canvas
    TH1D *h1 = (TH1D*)c1->GetPrimitive(hist10mm);
    TH1D *h2 = (TH1D*)c1->GetPrimitive(hist30mm);
    TH1D *h3 = (TH1D*)c1->GetPrimitive(hist50mm);
    TH1D *h4 = (TH1D*)c1->GetPrimitive(hist100mm);
    TH1D *h5 = (TH1D*)c1->GetPrimitive(hist200mm);

    if (!h1 || !h2 || !h3 || !h4 || !h5) {
        std::cerr << "Failed to get histogram" << std::endl;
        return;
    }

    // Define separate efficiency functions for each histogram
    TF1 *effi_fit1 = new TF1("effi_fit1",
        "[0]*exp( (([1]+[2]*log(x/1000)+[3]*pow(log(x/1000),2))**(-[6]) + ([4]+[5]*log(x/1000000)+[6]*pow(log(x/1000000),2))**(-[6]))**(-1/[6]) )",
        0, 1600);

        TF1 * fit = new TF1("fit", "[p0]*x**[p1]*exp(-[p2]*x) + [p3]*x**[p4]*exp(-[p5]*x)", 0, 1600);

    TF1 *effi_fit2 = new TF1("effi_fit2",
        "[0]*exp( (([1]+[2]*log(x/1000)+[3]*pow(log(x/1000),2))**(-[6]) + ([4]+[5]*log(x/1000000)+[6]*pow(log(x/1000000),2))**(-[6]))**(-1/[6]) )",
        0, 1600);

    TF1 *effi_fit3 = new TF1("effi_fit3",
        "[0]*exp( (([1]+[2]*log(x/1000)+[3]*pow(log(x/1000),2))**(-[6]) + ([4]+[5]*log(x/1000000)+[6]*pow(log(x/1000000),2))**(-[6]))**(-1/[6]) )",
        0, 1600);

    TF1 *effi_fit4 = new TF1("effi_fit4",
        "[0]*exp( (([1]+[2]*log(x/1000)+[3]*pow(log(x/1000),2))**(-[6]) + ([4]+[5]*log(x/1000000)+[6]*pow(log(x/1000000),2))**(-[6]))**(-1/[6]) )",
        0, 1600);

    TF1 *effi_fit5 = new TF1("effi_fit5",
        "[0]*exp( (([1]+[2]*log(x/1000)+[3]*pow(log(x/1000),2))**(-[6]) + ([4]+[5]*log(x/1000000)+[6]*pow(log(x/1000000),2))**(-[6]))**(-1/[6]) )",
        0, 1600);

    // Set parameter names for each fit function
    effi_fit1->SetParName(0, "A");
    effi_fit1->SetParName(1, "B");
    effi_fit1->SetParName(2, "C");
    effi_fit1->SetParName(3, "D");
    effi_fit1->SetParName(4, "E");
    effi_fit1->SetParName(5, "F");
    effi_fit1->SetParName(6, "G");

    effi_fit2->SetParName(0, "A");
    effi_fit2->SetParName(1, "B");
    effi_fit2->SetParName(2, "C");
    effi_fit2->SetParName(3, "D");
    effi_fit2->SetParName(4, "E");
    effi_fit2->SetParName(5, "F");
    effi_fit2->SetParName(6, "G");

    effi_fit3->SetParName(0, "A");
    effi_fit3->SetParName(1, "B");
    effi_fit3->SetParName(2, "C");
    effi_fit3->SetParName(3, "D");
    effi_fit3->SetParName(4, "E");
    effi_fit3->SetParName(5, "F");
    effi_fit3->SetParName(6, "G");

    effi_fit4->SetParName(0, "A");
    effi_fit4->SetParName(1, "B");
    effi_fit4->SetParName(2, "C");
    effi_fit4->SetParName(3, "D");
    effi_fit4->SetParName(4, "E");
    effi_fit4->SetParName(5, "F");
    effi_fit4->SetParName(6, "G");

    effi_fit5->SetParName(0, "A");
    effi_fit5->SetParName(1, "B");
    effi_fit5->SetParName(2, "C");
    effi_fit5->SetParName(3, "D");
    effi_fit5->SetParName(4, "E");
    effi_fit5->SetParName(5, "F");
    effi_fit5->SetParName(6, "G");

    // Fit each histogram with its respective function
    h1->Fit(effi_fit1, "R");
    h2->Fit(effi_fit2, "R");
    h3->Fit(effi_fit3, "R");
    h4->Fit(effi_fit4, "R");
    h5->Fit(effi_fit5, "R");

    // Set line colors
    h1->SetLineColor(1);
    h2->SetLineColor(2);
    h3->SetLineColor(3);
    h4->SetLineColor(4);
    h5->SetLineColor(6);

    // Create a new canvas for plotting
    TCanvas *c2 = new TCanvas("c2", "Efficiency Fit", 800, 600);
    h1->Draw("AP");
    h1->GetXaxis()->SetTitle("Energy (keV)");
    h1->GetYaxis()->SetTitle("#epsilon_{abs}");
    h2->Draw("same");
    h3->Draw("same");
    h4->Draw("same");
    h5->Draw("same");

    // Set line colors for fit functions
    effi_fit1->SetLineColor(1);
    effi_fit2->SetLineColor(2);
    effi_fit3->SetLineColor(3);
    effi_fit4->SetLineColor(4);
    effi_fit5->SetLineColor(6);

    // Draw the fit functions
    effi_fit1->Draw("same");
    effi_fit2->Draw("same");
    effi_fit3->Draw("same");
    effi_fit4->Draw("same");
    effi_fit5->Draw("same");

    // Update the canvas
    c2->Update();
}
