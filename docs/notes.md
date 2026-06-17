\# MassSpecAI Developer Notes



\## Project Vision



MassSpecAI is a local-first mass spectrometry analysis platform.



Goals:



\* Vendor-neutral data processing

\* mzML support

\* Deconvolution workflows

\* Impurity identification

\* AI-assisted interpretation

\* Local processing only



\---



\## Development Environment



Activate environment:



```cmd

.venv\\\\Scripts\\\\activate

```



Deactivate environment:



```cmd

deactivate

```



Check installed packages:



```cmd

pip list

```



Update requirements:



```cmd

pip freeze > requirements.txt

```



\---



\## Git Workflow



Check status:



```cmd

git status

```



Stage changes:



```cmd

git add .

```



Create commit:



```cmd

git commit -m "Description of changes"

```



Upload to GitHub:



```cmd

git push

```



Download latest changes:



```cmd

git pull

```



\---



\## OpenMS Concepts



\### MSExperiment



Represents an entire LC-MS run.



Contains:



\* Spectra

\* Chromatograms



Think of it as the top-level container.



\---



\### Spectrum



Represents a single scan.



Contains:



\* m/z values

\* intensity values



\---



\### Retention Time (RT)



Time during chromatographic separation.



OpenMS stores RT in seconds.



Examples:



60 sec = 1.0 min



300 sec = 5.0 min



\---



\### MS Level



MS1 = Full scan



MS2 = Fragmentation scan



MS3 = Fragment of fragment



Most TIC calculations use MS1 scans.



\---



\## Roadmap



Phase 1



\* Read mzML

\* Display TIC



Phase 2



\* Display spectra



Phase 3



\* Peak selection



Phase 4



\* Deconvolution



Phase 5



\* Impurity identification



Phase 6



\* AI interpretation



Phase 7



\* Report generation



```

```

