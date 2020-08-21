#dnanexus dx : Using your own applet, using an example file


.
├── README.md
├── conf.json #output directory structure #optional if not included in the python code
├── extras.json #extras file needed when you compile wdl
├── reorg_app #own applet, containing app build code (dxapp.json) and python script for reorganizing output files (code.py)
│   ├── code.py #python reorganizing script
│   └── dxapp.json #app build code
├── simple.wdl #wdl script
