from pathlib import Path
from pyopenms import MSExperiment, MzMLFile

MZML_PATH = Path("data/mzml/TC_2_Xlink.mzML")

if not MZML_PATH.exists():
    print(f"ERROR: File not found: {MZML_PATH}")
    exit()

exp = MSExperiment()

print("Loading mzML...")
MzMLFile().load(str(MZML_PATH), exp)

print(f"Loaded: {MZML_PATH}")
print(f"Number of spectra: {exp.getNrSpectra()}")
print(f"Number of chromatograms: {exp.getNrChromatograms()}")

for i, spectrum in enumerate(exp.getSpectra()[:5]):
    rt = spectrum.getRT()
    ms_level = spectrum.getMSLevel()

    print(
        f"Scan {i}: "
        f"RT={rt:.2f} sec "
        f"MS Level={ms_level}"
    )