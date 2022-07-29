This model simulates how clozapine affects the firing rate of dopaminergic (DA) neurons—and therefore the production of dopamine—in schizophrenic patients. It is based on a multi-compartmental model of a DA neuron (cited below), in which the firing rate of the neuron is primarily based on the L-type Ca+2 current and the A-type K+ currents.

Kuznetsova, A. Y., Huertas, M. A., Kuznetsov, A. S., Paladini, C. A., & Canavier, C. C. (2010). Regulation of firing frequency in a computational model of a midbrain dopaminergic neuron. Journal of Computational Neuroscience, 28(3), 389–403. https://doi.org/10.1007/s10827-010-0222-y. These network models used in the present study were obtained from ModelDB (accession number 127507).

# Kuznetsova2010
 
A python version of the hoc code from Kuznetsova et al, 2010. This version is hybrid - loads in the cell morphology from dopamine.hoc. Many other commands are issued in hoc using h(). Some are directly in python, as is plotting.

## Running the model

Make sure to compile the mechanisms first:

In the directory of the model code, compile the *.mod mechanisms by running the following command in a terminal:

On Windows, run `mknrndll`
On Mac and Linux, run `nrnivmodl`

Alternatively, open the NEURON Application folder (or program folder from the Start menu on Windows) and launch the mknrndll tool. When the gui appears, select the folder containing the code for Kuznetsova et al 2010. Then click the button to make nrnmech.dll.

After the mechanisms are successfully compiled, run `main.py` to receive a prompt asking which figure you would like to view. Answer the prompt with an input such as `2a2` or `6`. You will need to wait several minutes for the simulation to run and then generate the figure.

You can continue to plot as many figures as you want before answering the prompt with `q` or `quit`.

The control trace (Figure 2a2) is slightly different than the screen shot provided in the original model repository. However, so is the hoc version when I run it; perhaps the authors made a change to their model after preparing the publication figures and before uploading to ModelDB.


