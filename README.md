# MATS64662-2021-GRP1
The final repository for Group 1 of MATS64662 2021, to show code for the *connectivity of hydrides software project* in the University of Manchester module MATS64662, for Research Software Engineering. This Python package aims to carry out preliminary characterisation of Zirconium Hydride connectivity from sample micrographs by:

- Carrying out image processing to reduce small objects, noise and then convert sample micrographs into binary format.
- Estimate the Radial Hydride Fraction (RHF) of the sample micrographs, to charactertise hydride morphology.

# How to install
 - We recommend installing a python conda distribution using the free open-source [Anaconda Individual Edition](https://www.anaconda.com/products/individual).
 - This will allow you to easily manage installed python packages in `Anaconda Navigator` *then* `Environments`, and searching for the respective packages.

Ensure that you install and update the following packages (some of these may be installed by default):
  - `Matplotlib`
  - `Numpy`
  - `Scikit-image`
  - `Scipy`

# How to use
 - Download the repository.
 - Open *Anaconda Navigator* and open `Jupyter Notebook`.
 - Navigate to the repository folder you have downloaded, and open the example notebook included here.
 - This includes a walkthrough on how to use the python functions.

# Documentation
## Pyfunctions
 - This folder contains all the python functions as .py files.
 - Each function has a convenient docstring which describe the inputs and outputs concisely.
 - This can be accessed by simply importing the function into your Jupyter environment, or running it in your terminal, and then typing `help("function name")`. This will print the docstring.

## data
This contains the data used for the project, in the form of images. Here there is a folder for:
 - Sample micrographs that were analysed.
 - Test micrographs (artificial) used to test the code.

# Credits
The following software packages were used in or provided guidance for this project:
 - [Jupyter Notebook](https://jupyter.org/)
 - [Spyder IDE](https://www.spyder-ide.org/)
 - [Matplotlib](https://matplotlib.org/stable/index.html#)
 - [Numpy](https://numpy.org/)
 - [Scipy ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
 - [Scitkit Image](https://scikit-image.org/)
 - [HAPPy](https://zenodo.org/record/4627146)
