#dnanexus dx : Using your own applet, using an example file
.
├── README.md
├── conf.json #output directory structure #optional if not included in the python code
├── extras.json #extras file needed when you compile wdl
├── reorg_app #own applet, containing app build code (dxapp.json) and python script for reorganizing output files (code.py)
│   ├── code.py #python reorganizing script
│   └── dxapp.json #app build code
└── simple.wdl #wdl script

##STEPS taken
```
conda activate dx

dx login --token <token_id>

dx new project
#output
#Enter name for new project: <name_of_project>
#Created new project called "<name_of_project>" (<project-id>)
#Switch to new project now? [y/N]: y

dx build reorg_app
#output
#{"id": "<applet-id>"}

#edit extras.json to update the 'app_id'

java -jar /path/to/dxWDL.jar compile simple.wdl \
-project <project_id> -reorg -extras extras.json
#output
<workflow-id>

#to run the workflow
dx run <workflow-id> -y --brief
