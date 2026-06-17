# Import OpenMS classes
# MSExperiment = container that holds all spectra/chromatograms
# MzMLFile = class used to load mzML files
from pyopenms import MSExperiment, MzMLFile


# Location of the mzML file we want to analyze
MZML_PATH = "data/sample.mzML"


# Create an empty experiment object
# Think of this as a container that will hold the entire run
exp = MSExperiment()


# Load the mzML file into the experiment container
MzMLFile().load(MZML_PATH, exp)


# Basic information about the file
print("Loaded:", MZML_PATH)
print("Number of spectra:", exp.getNrSpectra())
print("Number of chromatograms:", exp.getNrChromatograms())


# Display information for the first 5 spectra
for i, spectrum in enumerate(exp.getSpectra()[:5]):

    # Retention time in seconds
    rt = spectrum.getRT()

    # MS level (1 = MS1, 2 = MS/MS, etc.)
    ms_level = spectrum.getMSLevel()

    print(
        f"Scan {i}: "
        f"RT={rt:.2f} sec, "
        f"MS level={ms_level}"
    )